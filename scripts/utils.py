import sys
import os
import json
import requests
import subprocess

TOKEN = os.getenv('SNYK_TOKEN')

headerGet = {"Content-Type": "application/json"}
headerGet["Authorization"] = 'token ' + TOKEN

headerPost = {"Content-Type": "application/vnd.api+json"}
headerPost["Authorization"] = 'token ' + TOKEN


jsonBody = {
    "data": 
       {"attributes": 
         {
           "include_in_recommendations": True,
           "versioning_schema": {"type": "semver"}
         },
       "type": "custom_base_image"}
    }



def fetch_id_from_json(json_data):
    if json_data:
       # Extract data elements with type: "project"
        projects = [data for data in json_data.get('data', []) if data.get('type') == 'project']

        # Extract ids for each project
        project_ids = [project.get('id') for project in projects]
   
        return project_ids
    return None

def make_get_rest_api_call(url):
    try:
        response = ''
        response=requests.get(url, headers=headerGet)
        if response.status_code == 200 or response.status_code == 201:
            json_data = response.json()
            return json_data
        else:
            print(f"Failed to make GET REST API call. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error making REST API call: {str(e)}")
    return None

def make_post_rest_api_call(url,projectIds):
    try:
        for projectId in projectIds:
          print(f"Marking Project: {projectId} as Custom base image")
          response = ''

          jsonBody["data"]["attributes"]["project_id"] = projectId
          postBody=jsonBody

          response=requests.post(url, json=postBody, headers=headerPost)
          if response.status_code == 200 or response.status_code == 201:
             json_data = response.json()
             return json_data
          else:
             print()
    except requests.exceptions.RequestException as e:
        print(f"Error making REST API call: {str(e)}")
    return None
