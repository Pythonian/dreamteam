from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app.extensions import db
from app.models import Employee

from . import auth
from .forms import LoginForm, RegistrationForm


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register/ route
    Add a user to the database through the registration form
    Also redirects to appropriate dashboard if user is already logged in
    """
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('home.admin_dashboard'))
        else:
            return redirect(url_for('home.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add user to the database
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered! You may now login')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login/ route and logs a user in
    """
    # Redirect to appropriate dashboard if user is already logged in
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('home.admin_dashboard'))
        else:
            return redirect(url_for('home.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        # check whether the user exists in the database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            # log user in
            login_user(employee, remember=form.remember_me.data)
            # Obtain the value of the next query string argument
            next_page = request.args.get('next')
            # if the login URL doesn't have a next argument
            # or it's argument is set to a full URL that includes a domain name
            if not next_page or url_parse(next_page).netloc != '':
                # redirect to the appropriate dashboard page after login
                if current_user.is_admin:
                    next_page = url_for('home.admin_dashboard')
                else:
                    next_page = url_for('home.dashboard')
            return redirect(next_page)
        # when login details are incorrect
        else:
            flash('Invalid email or password.')
    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout/')
@login_required
def logout():
    """
    Handle requests to the /logout/ route and logs a user out
    """
    logout_user()
    flash('You have successfully been logged out.')
    # redirect to the login page
    return redirect(url_for('auth.login'))
