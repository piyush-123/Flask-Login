from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required
from ..models import User
from ..extensions import db
from .forms import RegisterForm,LoginForm

auth_bp = Blueprint("auth",__name__,url_prefix="/auth")

@auth_bp.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created ! You can now Login","success")
        return redirect(url_for("auth.login"))
    
    return render_template("register.html",form=form)

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and User.check_password(form.password.data):
            login_user(user)
            flash("Logged in success!!","success")
        else:
            flash("Invalid!!!","danger")
    return render_template("login.html",form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged Out!!","info")
    return redirect(url_for("auth.login"))