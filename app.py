import genomelink
import os
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from operator import attrgetter
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from randomname import random_user
from docusign import docusign

import traits

app = Flask(__name__)

const_traits = traits.generate_random_users(n=1)[0]['traits']

#print(os.environ['GENOMELINK_CLIENT_ID'])
#print(os.environ['GENOMELINK_CLIENT_SECRET'])

app.config.from_pyfile('config.py')


os.environ['GENOMELINK_CLIENT_ID'] = '4VZK1tAlsGsX9ZKiz9joKPrMG0RNlE9RgmRRq22k'
os.environ['GENOMELINK_CLIENT_SECRET'] = 'LrJOsChTOUBoi86MZ0MH1paMxIxlNyFs5CW9LPHwT5DENlP2pFnGPDUoOJkwSgDiDikRtxNDRUl7o1jzP82MmCopndnPhCfc6vMzbUYDoRL2CGYIMIFARghNoFdugSaK'
os.environ['GENOMELINK_CALLBACK_URL'] = "http://127.0.0.1:5000/callback"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    
    reports = []
    print(request.method)
    # get all the form properties
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        trait_type = request.form.get('type')
        opp = request.form.get('opp')
        docusign()
    
#        authorize_url = genomelink.OAuth.authorize_url(scope=['report:eye-color report:beard-thickness report:morning-person report:childhood-intelligence'])

        # Fetching a protected resource using an OAuth2 token if exists.
#        p1 = []
#        if session.get('oauth_token'):
#            for name in ['eye-color', 'beard-thickness', 'morning-person', 'childhood-intelligence']:
#                p1.append(genomelink.Report.fetch(name=name, population='european', token=session['oauth_token']))
        p1 = {'name': name, 'traits': const_traits}
        reports = traits.get_reports(p1, trait_type)
        reports = sorted(reports, key=lambda x: x['similarity'], reverse=opp=='similar')
        
        for report in reports:
            report['similarity'] = '{:.2f} %'.format(report['similarity'] * 100)
            
    return render_template('search.html', reports=reports)

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
    return redirect(url_for(''))


if __name__ == '__main__':
    # This allows us to use a plain HTTP callback.
    import os
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Run local server on port 5000.
    app.secret_key = os.urandom(24)
    app.run(debug=True)