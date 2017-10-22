import genomelink
import os
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from randomname import random_user
import httplib2
import json
import sys

app = Flask(__name__)

#print(os.environ['GENOMELINK_CLIENT_ID'])
#print(os.environ['GENOMELINK_CLIENT_SECRET'])

app.config.from_pyfile('config.py')


os.environ['GENOMELINK_CLIENT_ID'] = '4VZK1tAlsGsX9ZKiz9joKPrMG0RNlE9RgmRRq22k'
os.environ['GENOMELINK_CLIENT_SECRET'] = 'LrJOsChTOUBoi86MZ0MH1paMxIxlNyFs5CW9LPHwT5DENlP2pFnGPDUoOJkwSgDiDikRtxNDRUl7o1jzP82MmCopndnPhCfc6vMzbUYDoRL2CGYIMIFARghNoFdugSaK'
os.environ['GENOMELINK_CALLBACK_URL'] = "http://127.0.0.1:5000/callback"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['get', 'post'])
def search():
    # get all the form properties
    if request.method == 'post':
        name = request.form.get('name')
        phone = request.form.get('phone')
        typ = request.form.get('type')
        opp = request.form.get('opp')
        reports = reports
    username ="astaning@ucsd.edu"
    password="docusign"
    integratorKey = "64395163-6917-4fec-b65c-98ac839869f8"
    authenticateStr = "<DocuSignCredentials>" \
                        "<Username>" + username + "</Username>" \
                        "<Password>" + password + "</Password>" \
                        "<IntegratorKey>" + integratorKey + "</IntegratorKey>" \
                        "</DocuSignCredentials>";
    #
    # STEP 1 - Login
    #
    url = 'https://demo.docusign.net/restapi/v2/login_information';
    headers = {'X-DocuSign-Authentication': authenticateStr, 'Accept': 'application/json'};
    http = httplib2.Http();
    response, content = http.request(url, 'GET', headers=headers);

    status = response.get('status');
    if (status != '200'): 
        print("Error calling webservice, status is: %s" % status); sys.exit();

    # get the baseUrl and accountId from the response body
    data = json.loads(content);
    loginInfo = data.get('loginAccounts');
    D = loginInfo[0];
    baseUrl = D['baseUrl'];
    accountId = D['accountId'];
    #construct the body of the request in JSON format  
    # accountId="3916191"
    # username="alex.staninger@gmail.com"
    templateId="626d55c7-86dd-4c27-8154-23fc5176867d"
    baseUrl="https://demo.docusign.net/restapi/v2/accounts/3916191"
    requestBody = "{\"accountId\": \"" + accountId + "\"," + \
                    "\"status\": \"sent\"," + \
                    "\"emailSubject\": \"Liability release form pending signature\"," + \
                    "\"emailBlurb\": \"This comes from GenMatch.tech\"," + \
                    "\"templateId\": \"" + templateId + "\"," + \
                    "\"templateRoles\": [{" + \
                    "\"email\": \"" + username + "\"," + \
                    "\"name\": \"Name\"," + \
                    "\"roleName\": \"Signer\" }] }";

    # append "/envelopes" to baseURL and use in the request
    url = baseUrl + "/envelopes";
    headers = {'X-DocuSign-Authentication': authenticateStr, 'Accept': 'application/json'}
    http = httplib2.Http()
    response, content = http.request(url, 'POST', headers=headers, body=requestBody);
    status = response.get('status');
    if (status != '201'): 
        print("Error calling webservice, status is: %s" % status); sys.exit();
    data = json.loads(content);
    envId = data.get('envelopeId');

    return render_template('search.html')

@app.route('/twilio')
def twilio():
    return render_template('twilio.html')

@app.route('/twilio_token')
def video():
    identity = random_user()
    scat = AccessToken(app.config['TWILIO_ACCOUNT_SID'], \
        app.config['TWILIO_API_KEY'], app.config['TWILIO_API_SECRET'], identity=identity)
    scat.add_grant(VideoGrant(room="Room1"))
    token = scat.to_jwt()
    value = str(token)
    value2 = value[2:-1]
    return jsonify(dict(identity=identity, token=value2))

@app.route('/callback')
def callback():
    token = genomelink.OAuth.token(request_url=request.url)
    session['oauth_token'] = token
    return redirect(url_for('index'))

# authorize_url = genomelink.OAuth.authorize_url(scope=['report:eye-color report:beard-thickness report:morning-person report:childhood-intelligence']) #report:beard-thickness report:morning-person
#
#
# # Fetching a protected resource using an OAuth2 token if exists.
# reports = []
# if session.get('oauth_token'):
#     for name in ['eye-color', 'beard-thickness', 'morning-person', 'childhood-intelligence']:
#         reports.append(genomelink.Report.fetch(name=name, population='european', token=session['oauth_token']))
#
# return render_template('index.html', authorize_url=authorize_url, reports=reports)

if __name__ == '__main__':
    # This allows us to use a plain HTTP callback.
    import os
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Run local server on port 5000.
    app.secret_key = os.urandom(24)
    app.run(debug=True)
