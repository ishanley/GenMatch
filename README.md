The deployed site can be visited [here](genmatch.tech).
The devpost blog can be visited [here](https://devpost.com/software/genmatch).

### Installation
After downloading the zip, create a virtual environment by running 
```
$ virtualenv venv 
```
Then, activate the virtual environment by running 
```
$ source venv/bin/activate
```
Finally, download the dependencies by running 
```
$ pip install -r requirements.txt
```
Next, you set up environment variables by running
```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
```
You can then run the app locally using
```
$ flask run
```
