import os, sys
from . import aitools_app
from flask import flash, render_template, redirect, url_for, request, make_response, session
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from ..functions.views import func_submission, func_get_submission, func_admin_dashboard, func_login, func_get_website, \
    func_search, func_recent_search, func_category_group


@aitools_app.route('/', methods=['GET', 'POST'])
def login():
    """
    Login Page
    """
    error=""
    if request.method == "POST":
        user_data = request.form.to_dict() 
        user_exist = func_login(user_data)

        if user_exist:
            return redirect(url_for('.dashboard', stk=1200))
        else:
            error = "Invalid Access Details!!!"

    response = make_response( 
        render_template(
            "login.html",
            error=error
        )
    )       
    return response  


@aitools_app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Registration Page
    """
    submission=func_get_submission()
    all_submissions, approved_submission, not_approved = func_admin_dashboard()
    return render_template(
        "dashboard.html",
        submission=submission,
        all_submissions=all_submissions,
        approved_submission=approved_submission,
        not_approved=not_approved
    )


###Logout###############################################################
@aitools_app.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an customer out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('.login'))


###Submission###############################################################
@aitools_app.route('/submissions/<string:aid>', methods=['GET', 'POST'])
@login_required
def submission(aid):
    """
    Submit New AI Tool
    """
    if request.method == "POST":
        site_data = request.form.to_dict() 
        print(site_data)
        submit_url = func_submission(site_data)
    
        if submit_url:
            return redirect(url_for('.dashboard', stk=1800))
        else:
            info = "There is error with the submission"
    else:
        site_data = func_get_website(aid)

    return render_template(
        "submission.html",
        site_data=site_data
    )


###search###############################################################
@aitools_app.route('/search', methods=['GET', 'POST'])
def search():
    """
    """
    response = None
    if request.method == "POST":
        search_text = request.form.to_dict() 
        search_ip = request.remote_addr
        response  = func_search(search_text['search'], search_ip)

    return response


@aitools_app.route('/recent_search', methods=['GET', 'POST'])
def recent_search():
    """
    """
    return func_recent_search()


@aitools_app.route('/category_group', methods=['GET', 'POST'])
def category_group():
    """
    """
    return func_category_group()