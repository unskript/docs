#!/usr/bin/env python

import os
import json
from pathlib import Path 
"""
This script walks through Awesome Repo and finds out all README.md files
in each Connector page and then creates a nice list of Action Name
and its corresponding README.md file
"""
def create_action_and_readme_list(path_to_awesome_dir: str) -> list:
    retVal = []
    if not path_to_awesome_dir:
        return retVal
    
    for root, dirs, files in os.walk(path_to_awesome_dir):
        if os.path.basename(root) == "__pycache__":
            continue
        action_file = readme_file = title = description = None
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                action_file = os.path.basename(os.path.join(root, file).replace('.py', ''))
            if file == "README.md":
                readme_file = os.path.join(root, file)
            if file.endswith(".json"):
                with open(os.path.join(root, file), 'r') as f:
                    contents = json.load(f)
                    title = contents.get('action_title')
                    description = contents.get('action_description')
            if action_file != None and readme_file != None and title != None and description != None:
                k = [title.strip(), description.strip(), action_file.strip(), readme_file.strip()]
                if k not in retVal:
                    retVal.append(k)

    return retVal


"""
Update Given Readme with the contents that was sent. items_to_update i  list
comprising of Title, Description, Action Name and Action Readme file.  This
is the list that is returned by the create_action_readme_list() function
"""
def update_readme(path_to_readme: str, 
                  connector_name: str, 
                  items_to_update: list):
    if not path_to_readme:
        return 
    items_to_update.sort()
    awesome_repo_url = "https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/"
    print(f"Updating README at {path_to_readme}")
    _r = Path(os.path.abspath(path_to_readme))
    if not _r.is_file():
        print(f"CREATING {path_to_readme}")
        _r.touch()
    
    with open(path_to_readme, 'w') as f:
        contents = ''
        for item in items_to_update:
            title,description,action,readme = item
            readme = readme.replace("/tmp/Awesome-CloudOps-Automation/", awesome_repo_url)
            contents += f'* [{title}]({readme}) : {description}' + '\n'
        f.write(f"# {connector_name} Actions" + '\n')
        f.write(contents)


"""
Main function that gets called to update the list of Actions in the respective
README.md file.
"""
def main(repo_path: str):
    if not repo_path:
        return []
    
    # This dictionary maps the Connector Name to the local directory where
    # the README file exists
    readme_to_connector_map = {"aws": "AWS", 
                          "airflow": "Airflow", 
                          "apache-kafka": "Kafka", 
                          "azure": "Azure", 
                          "datadog": "Datadog",
                          "elasticsearch": "ElasticSearch", 
                          "gcp": "GCP", 
                          "github": "Github", 
                          "grafana": "Grafana", 
                          "hadoop": "Hadoop", 
                          "jenkins": "Jenkins",
                          "jira": "Jira", 
                          "kubernetes": "Kubernetes", 
                          "mongodb": "Mongo", 
                          "ms-sql": "MsSQL", 
                          "mysql": "MySQL", 
                          "netbox": "Netbox", 
                          "nomad": "Nomad", 
                          "opensearch": "opensearch", 
                          "pingdom": "Pingdom", 
                          "postgres": "Postgresql", 
                          "prometheus": "Prometheus",
                          "redis": "Redis", 
                          "rest": "Rest", 
                          "salesforce": "SalesForce", 
                          "slack": "Slack", 
                          "snowflake": "Snowflake", 
                          "splunk": "Splunk",
                          "ssh": "SSH", 
                          "stripe": "Stripe"}
    
    local_action_base_dir = "../../connnecting/connectors/"
    for local_dir,connector in readme_to_connector_map.items():
        print(f"Processing {local_dir} for {connector}")
        connector_action_dir = local_action_base_dir + local_dir + f'/action_{connector.lower()}'
        if os.path.exists(connector_action_dir) == False:
            print(f"Creating {connector_action_dir}...")
            os.makedirs(connector_action_dir)
        readme_file_name = connector_action_dir + f'/README.md'
        update_readme(readme_file_name,
                      connector,
                      create_action_and_readme_list(os.path.join(repo_path, connector, "legos")))


if __name__ == '__main__':
    if os.path.exists("/tmp/Awesome-CloudOps-Automation"):
        main("/tmp/Awesome-CloudOps-Automation")
    else:
        print("Awesome Repo not found: Check if it is checked out!")
