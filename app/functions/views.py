import os, sys, re, json

from ..models.views import manage_site, get_submissions, get_dashboard_data, get_website
from ..models.auth import login_admin_user


def func_login(user_data):
    """
    """
    user_exist = login_admin_user(user_data)

    return user_exist


def func_submission(site_data):
    """
    """
    save_site = manage_site(site_data)

    return save_site


def func_get_submission():
    """
    """
    get_submission = get_submissions()

    return get_submission


def func_get_website(aid):
    """
    """
    get_submission = get_website(aid)

    return get_submission


def func_dashboard():
    """
    """
    all_submissions, my_submission, approved_submission = get_dashboard_data()
    
    not_approved = my_submission - approved_submission

    return all_submissions, my_submission, approved_submission, not_approved


def func_admin_dashboard():
    """
    """
    all_submissions, approved_submission = get_dashboard_data()
    
    not_approved = all_submissions - approved_submission

    return all_submissions, approved_submission, not_approved

