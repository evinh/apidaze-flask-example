# Simple Flask application to get started using Apidaze.

## Requirements:  
- Python 2.7
- a command line
- a basic knowledge of Python.

## How it works with Apidaze

Clone, modify, and deploy this example application to a publicly accessible server. Instructions below under "Install and run".

For Inbound calls, add the "External Script" URL of your application (this example application wherever you deploy it) with /receiveCall at the end. Example: http://yourappurl/recieveCall.  You can do this via the VoIP Innovations portal.  Make sure to add a phone number to it in the VoIP Innovations portal.  https://backoffice.voipinnovations.com

Call Flow:

Inbound Call -> GET request to your app with URL params of the call detail -> Your app generates the response based on the app generating the XML response based on the call.xml template found in the templates directory.

In this example, there are no variables being used in the call.xml template, but you can pass in variables in the receiveCall function in app.py... you can see an example there in this line, where it renders the template:  
template = render_template('call.xml', some_variable=example_variable) -- replace "some_variable" with whatever you want to pass, then you can use {{some_variable}} in the call.xml template to render that dynamic variable.

For inbound SMS, the call flow is the same, however the SMS sent from Apidaze is a POST with JSON as the content.  To just receive SMS and not calls, you can set your URL in Apidaze as the same for calls, but /receiveSMS instead of /receiveCall at the end of your URL.  To receive both SMS and Calls, you'll need to update the receiveCall function in app.py to accept POST and also look for the Content-Type of JSON, then process accordingly.  This is easily done with an "if" statement.

## Install and run
git clone https://github.com/evinh/apidaze-flask-example.git

cd apidaze-flask-example

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt (just in case)

To run:  python app.py


## API Docs for Apidaze:

https://vi-api.trybelabs.com


You can publish this to the web for testing by running it on Heroku or Dokku.
