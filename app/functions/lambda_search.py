import requests
import urllib.parse

def lambda_handler(event, context):
    # Replace 'YOUR_API_ENDPOINT_URL' with the actual URL of your API endpoint
    api_endpoint_url = 'YOUR_API_ENDPOINT_URL'

    # Retrieve the data from the Lambda event
    search_text = event.get('search_text', 'default_search_value')

    # Data to be sent to the API endpoint as form data
    data = {
        "search": search_text
    }

    # Encode the form data
    encoded_data = urllib.parse.urlencode(data)

    # Set headers for the request (if needed)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        # Send the POST request to the API endpoint
        response = requests.post(api_endpoint_url, data=encoded_data, headers=headers)

        # Check the response status code and handle accordingly
        if response.status_code == 200:
            return {
                "statusCode": 200,
                "body": response.text  # Return the response from the server
            }
        else:
            # Handle other status codes or errors as needed
            return {
                "statusCode": response.status_code,
                "body": "Error: Request failed with status code {}".format(response.status_code)
            }
    except Exception as e:
        # Handle exceptions if any
        return {
            "statusCode": 500,
            "body": "Error: {}".format(str(e))
        }
