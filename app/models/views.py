import os, sys
import random, string
from app import db
from flask_login import current_user
from flask import flash, redirect, render_template, url_for
from datetime import date, datetime, timedelta
from sqlalchemy import func

from .model import AiToolsAdmin, AiToolsMember, AiToolsSubmit, AiToolsSearchData


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
        site.category = site_data['category']
        site.rating = site_data['rating']
        site.pricing = site_data['pricing']
        site.image_url = site_data['image_url']
        

        db.session.commit()

    return True


def get_submissions():
    """
    Get all Submissions for User
    """
    submissions = AiToolsSubmit.query.all()

    return submissions


def search_submissions():
    my_submission = db.session.query(AiToolsSubmit).filter(AiToolsSubmit.status == 1).limit(5).all()

    if my_submission is not None:
        # Your code to process the query results goes here
        # For example, you can loop through the results or perform other operations.
        return my_submission
    else:
        # Handle the case when the query returns no results
        print("No results found.")


def submit_search(search_text, search_ip, result_id):
    """
    Submit new Tool
    """
    search_item = AiToolsSearchData(
        search_term=search_text,
        search_ip=search_ip,
        search_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        result_ids=result_id
    )
    # add user to the database
    if search_text and search_text is not None:
        db.session.add(search_item)
        db.session.commit()

    return True


def recent_search():
    """
    """
    query = db.session.query(AiToolsSearchData.result_ids).\
                filter(AiToolsSearchData.search_term != '').\
                filter(AiToolsSearchData.result_ids != '0').\
                group_by(AiToolsSearchData.result_ids).\
                limit(5)

    # Execute the query and fetch the results
    results = query.all()

    return results


def category_group():
    """
    """
    # Query to group by category and return category name and its count
    query = db.session.query(AiToolsSubmit.category, func.count(AiToolsSubmit.category).label('count_category')).\
        group_by(AiToolsSubmit.category)

    # Execute the query and fetch the results
    results = query.all()

    return results


def query_by_ids(ids_list):
    # Convert the input list of IDs to a flat list of strings
    flat_ids = [str(item[0]) for item in ids_list]

    # Query the AiToolsSubmit table using the IDs
    query = db.session.query(AiToolsSubmit).filter(AiToolsSubmit.id.in_(flat_ids))

    # Execute the query and fetch the results
    results = query.all()

    return results


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