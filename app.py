from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import connexion
import requests
import myapi

#Create the application instance!
app = connexion.App(__name__, specification_dir='./')
auth = HTTPBasicAuth()


users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


#Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

#Create a URL route in our application for "/"
@app.route('/', methods=["GET","POST"])
@auth.login_required
def home():
    #return "Hello, {}!".format(auth.current_user())
    if(auth.current_user()):
        #uname = auth.current_user()
        return render_template('home.html', username=auth.username())
    else:
        print("ERROR")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



