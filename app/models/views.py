import os, sys
import random, string
from app import db
from flask_login import current_user
from flask import flash, redirect, render_template, url_for
from datetime import date, datetime, timedelta

from .model import AiToolsAdmin, AiToolsMember, AiToolsSubmit


def manage_site(site_data):
    """
    Submit new Tool
    """
    site = db.session.query(AiToolsSubmit).filter_by(id=site_data['id']).first()
    if site:
        # Update data
        site.title = site_data['title']
        site.website = site_data['website']
        site.description = site_data['description']
        site.keywords = site_data['keywords']
        site.business_email = site_data['business_email']
        site.status = site_data['status']

        db.session.commit()

    return True


def get_submissions():
    """
    Get all Submissions for User
    """
    submissions = AiToolsSubmit.query.all()

    return submissions


def get_website(id):
    """
    Get all Submissions for User
    """
    website = AiToolsSubmit.query.filter_by(id=id).first()

    return website


def get_dashboard_data():
    """
    Dashboard Stats
    """
    all_submissions = AiToolsSubmit.query.count()

    approved_submission = db.session.query(AiToolsSubmit).filter(AiToolsSubmit.status==1).count()

    return all_submissions, approved_submission