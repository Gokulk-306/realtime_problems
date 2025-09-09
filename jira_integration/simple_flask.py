# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://ceecgokul2024.atlassian.net/rest/api/3/issue"

    API_TOKEN = os.getenv("YOUR_API_TOKEN")   # ✅ get from environment variable
    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "project": {
                "key": "GOK"
            },
            "issuetype": {
                "id": "10012"
            },
            "summary": "Main order flow broken",
        },
        "update": {}
    })

    # Read JSON body from request
    body = request.get_json(silent=True) or {}
    comment_body = body.get("comment", {}).get("body", "")

    if comment_body.strip() == "/jira":
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return "Enter correct command: /jira to create a new Jira ticket", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
