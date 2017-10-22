import httplib2
import json
import sys

def docusign():
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