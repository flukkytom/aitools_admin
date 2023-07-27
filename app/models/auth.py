
import os, sys
import random, string
from app import db
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from .model import AiToolsAdmin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta



def login_admin_user(user_data):
    """
    Attempt to log in a user based on the provided user_data dictionary.

    Args:
        user_data (dict): A dictionary containing the 'username' and 'password' keys.

    Returns:
        bool: True if the login is successful, False otherwise.
    """
    # Set a default value for the result (login status)
    result = False

    # Retrieve the user from the database based on the provided username
    try:
        user = AiToolsAdmin.query.filter_by(username=user_data['username']).first()

        # Check if the user exists and if the provided password matches the one in the database
        if user is not None and user.password == user_data['password']:
            # Perform login using Flask-Login's login_user function
            login_user(user)
            result = True
        else:
            result = False

    except Exception as e:
        # Handle other potential exceptions that may occur during the login process
        print(e)
        result = False

    return result
