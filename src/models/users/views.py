from flask import Flask, Blueprint, request, session, redirect, url_for, render_template

from src.models.users.user import User

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route("/login", methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["hashed"]

        if User.is_valid_login(email, password):
            print("is valid")
            session['email'] = email
            return redirect(url_for(".user_alerts"))
    print("not valid")
    return render_template("users/login.html")  # send the user an error if their login was invalid.


@user_blueprint.route("/register")
def register_user():
    pass


@user_blueprint.route("/alerts")
def user_alerts():
    return 'This is the alerts page.'


@user_blueprint.route("/logout")
def logout_user():
    pass


@user_blueprint.route("/check_alerts/<string:user_id>")
def check_user_alerts(user_id):
    pass
