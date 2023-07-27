from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class AiToolsSubmit(UserMixin, db.Model):
    """
    Tools table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'submissions'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    title = db.Column(db.String(64))
    website = db.Column(db.String(64))
    description = db.Column(db.String(64))
    keywords = db.Column(db.String(64))
    business_email = db.Column(db.String(64))
    business_phone = db.Column(db.String(64))
    submission_date = db.Column(db.String(64))
    sub_data = db.Column(db.String(64))
    status = db.Column(db.String(64))
    category = db.Column(db.String(64))
    pricing = db.Column(db.String(64))
    rating = db.Column(db.String(64))
    image_url = db.Column(db.String(256))


class AiToolsAdmin(UserMixin, db.Model):
    """
    Admin Table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'admin_access'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    login_status = db.Column(db.String(64))
    date_added = db.Column(db.String(64))


class AiToolsSearchData(UserMixin, db.Model):
    """
    Admin Table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'search_data'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String(64), index=True)
    search_date = db.Column(db.String(64))
    search_ip = db.Column(db.String(64))
    result_ids = db.Column(db.String(64))