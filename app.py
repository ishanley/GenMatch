import genomelink
import os
from flask import Flask, render_template, request, redirect, session, url_for
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
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

@app.route('/search', methods=['POST'])
def search():
    # get all the form properties
    redirect(url_for('search_results'))

@app.route('/twilio')
def video():
    scat = AccessToken(app.config['TWILIO_ACCOUNT_SID'], \
        app.config['TWILIO_API_KEY'], app.config['TWILIO_API_SECRET'])
    scat.add_grant(VideoGrant(room='RM123'))
    token = scat.to_jwt()
    return render_template('twilio.html', identity="need random", token=token)
    
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

# @app.route('/callback')
# def callback():
#     # The user has been redirected back from the provider to your registered
#     # callback URL. With this redirection comes an authorization code included
#     # in the request URL. We will use that to obtain an access token.
#     token = genomelink.OAuth.token(request_url=request.url)
#
#     # At this point you can fetch protected resources but lets save
#     # the token and show how this is done from a persisted token in index page.
#     session['oauth_token'] = token
#     return redirect(url_for('index'))
#
if __name__ == '__main__':
    # This allows us to use a plain HTTP callback.
    import os
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Run local server on port 5000.
    app.secret_key = os.urandom(24)
    app.run(debug=True)
