import os, sys, re, json
import nltk

from ..models.views import manage_site, get_submissions, get_dashboard_data, get_website, search_submissions, submit_search, \
                            recent_search, query_by_ids, category_group
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




def search_table(search_text, table_data):
    # Step 1: Eliminate adjectives and qualifiers using NLTK
    # Tokenize the search text and get the part-of-speech tags
    words = nltk.word_tokenize(search_text)
    pos_tags = nltk.pos_tag(words)

    # Filter out adjectives and qualifiers
    filtered_words = [word for word, pos in pos_tags if pos not in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']]

    # Combine filtered words back to form the modified search text
    modified_search_text = " ".join(filtered_words)

    # Step 2: Search the table for matches in title and description
    matches = []
    for row in table_data:
        title = row.title
        description = row.description

        if modified_search_text.lower() in title.lower() or modified_search_text.lower() in description.lower():
            matches.append(row)

    # Convert the results into a JSON-serializable format
    serialized_results = []
    for row in matches:
        serialized_results.append({
            'id': row.id,
            'title': row.title,
            'description': row.description,
            'keywords': row.keywords,
            'website': row.website,
            'business_email': row.business_email,
            'business_phone': row.business_phone,
            'category': row.category,
            'image_url': row.image_url,
            'rating': row.rating,
            'pricing': row.pricing
            # Add other attributes as needed
        })

    # Serialize the results to JSON
    response_json = json.dumps(serialized_results)

    return response_json


def func_search(search_text, search_ip):
    """
    """
    table_data = search_submissions()

    result = search_table(search_text, table_data)

    # print("result:", result)
    if not result:
        # empty JSON
        print("list:", result, search_text)
        submit_search(search_text, search_ip, 0)
    else:
        print("listex:", result, search_text)
        # data_dict = json.loads(result)
        data_dict = json.loads(result)

        if len(data_dict) > 0:
            # Access the 'id' key from the first dictionary in the list
            result_id = data_dict[0]['id']
            submit_search(search_text, search_ip, result_id)
            print(result_id)
        else:
            print("The data list is empty.")
            submit_search(search_text, search_ip, 0)

    return result


def func_recent_search():
    """
    """
    recent_search
    # Call the function to fetch the data
    data_list = recent_search()

    # Convert the data_list to JSON format
    data_json = json.dumps(data_list)

    get_tools = query_by_ids(data_json)

    # Convert the results into a list of dictionaries
    search_data = [{
        'id': result.id,
        'member_id': result.member_id,
        'title': result.title,
        'website': result.website,
        'description': result.description,
        'keywords': result.keywords,
        'business_email': result.business_email,
        'business_phone': result.business_phone,
        'submission_date': result.submission_date.isoformat(),
        'sub_data': result.sub_data,
        'status': result.status,
        'category': result.category,
        'pricing': result.pricing,
        'rating': result.rating,
        'image_url': result.image_url
    } for result in get_tools]

    # Convert the data_list to JSON format
    data_result = json.dumps(search_data)

    return data_result


def func_category_group():
    """
    """
    results = category_group()
    # Convert the results into a list of dictionaries
    category_data = [{
        'category_name': result.category,
        'category_count': result.count_category
    } for result in results]

    # Convert the data_list to JSON format
    data_result = json.dumps(category_data)

    return data_result