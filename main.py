import sys
import subprocess
import json
import requests
import snyk
from scripts import utils

snykCustomBaseImageAPI="https://api.snyk.io/rest/custom_base_images?&version=2023-06-19~beta"

def onboardCustomImagestoSnykOrg(orgId,filename):

    snykOrgURI="https://api.snyk.io/rest/orgs/" + orgId + "/projects?version=2023-06-22&names[]=SnykCBIR2"
    snykMonitorCommand="snyk container monitor --project-name=SnykCBIR2 --org=" + orgId

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                command = f'{snykMonitorCommand} {line}'
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                output = result.stdout.strip()
                if result.returncode == 0:
                    print(f"Snyk container monitor executed for {line}.")
                else:
                    print(f"Error running snyk command for {line}: {result.stderr}")
                
                api_url = f"{snykOrgURI}"
                api_response = utils.make_get_rest_api_call(api_url)
                if api_response:
                    #print(f" GET Projects API response received: {api_response}")
                    id_field = utils.fetch_id_from_json(api_response)
                    if id_field:
                        #print(f"Project ID for {line}: {id_field}")
                        api_url = f"{snykCustomBaseImageAPI}"
                        utils.make_post_rest_api_call(api_url,id_field)
                    else:
                        print(f"No Project ID found for {line}.")

    except FileNotFoundError:
        print("File not found.")

# Check if filename argument is provided
if len(sys.argv) < 3:
    print("Please provide a filename as an argument.")
else:
    # Get the filename from the command-line argument
    orgId = sys.argv[1]
    filename = sys.argv[2]
    onboardCustomImagestoSnykOrg(orgId,filename)

