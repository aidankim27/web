from flask import render_template, request, url_for, flash, redirect
from schooltldr.forms import RegistrationForm
from schooltldr.models import User
from schooltldr import app, db


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/signup", methods=["GET", "POST"])
@app.route("/sorv", methods=["GET", "POST"])
def sorv():
    form = RegistrationForm()
    if form.validate_on_submit():
        accs = open("accs.txt", "a")
        accs.write(f"\n{form.email.data},{form.grade.data}")
        user = User(
            name=form.username.data, email=form.email.data, grade=form.grade.data
        )
        db.session.add(user)
        db.session.commit()
        flash(f"You will now be notified!", "success")
        return redirect(url_for("home"))
    else:
        flash(f"Check over your information", "error")
    return render_template("signup.html", title="School or virtual", form=form)

