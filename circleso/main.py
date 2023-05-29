# main.py
# author: Container Nerds LLC.

# Python dependencies
import json
import os
import sys
from dotenv import load_dotenv
from circleso import CircleRestClient
from models.SpaceGroup import SpaceGroup
from utils import preflight_checks

DEBUG = True

# TEMPORARY
def read_workflow(api_key):
    client = CircleRestClient(api_key)

    me = client.get_me()
    if me is not None:
        if DEBUG:
            print(json.dumps(me, indent=4))

    communities = client.get_communities_index()
    if communities is not None:
        if DEBUG:
            print(json.dumps(communities, indent=4))

    print('Community ID: ' + str(communities[0]['id']))
    print('Community Slug: ' + str(communities[0]['slug']))

    community = client.get_show_community(str(communities[0]['id']), params={'slug': str(communities[0]['slug'])})
    if community is not None:
        if DEBUG:
            print(json.dumps(community, indent=4))

    space_groups = client.get_space_groups_index(str(communities[0]['id']))
    if space_groups is not None:
        if DEBUG:
            print(json.dumps(space_groups, indent=4))

def write_workflow(api_key):
    client = CircleRestClient(api_key) # GrowthCommunity (Push)

def test_workflow(api_key):
    client = CircleRestClient(api_key) # GrowthCommunity (Push)

    communities = client.get_communities_index()
    if communities is not None:
        if DEBUG:
            print(json.dumps(communities, indent=4))

    print('Community ID: ' + str(communities[0]['id']))
    print('Community Slug: ' + str(communities[0]['slug']))

    community = client.get_show_community(str(communities[0]['id']), params={'slug': str(communities[0]['slug'])})
    if community is not None:
        if DEBUG:
            print(json.dumps(community, indent=4))

    # Get all space groups
    # space_groups = client.get_space_groups_index(str(communities[0]['id']))
    # if space_groups is not None:
    #     if DEBUG:
    #         print(json.dumps(space_groups, indent=4))

    sgroup = SpaceGroup(name='GrowthCommunity', slug='growth-community').to_json()
    created_sgroup = client.create_space_group(str(communities[0]['id']), sgroup)
    if created_sgroup is not None:
        if DEBUG:
            print(json.dumps(created_sgroup, indent=4))

# Main method
def main():

    load_dotenv() # Load environment variables from .env file

    preflight_checks() # Check for Python version and environment variables

    api_key = os.getenv('CIRCLESO_API_KEY')

    # read_workflow(api_key)
    # write_workflow(api_key)
    test_workflow(api_key)
    

# Main application entrypoint
if __name__ == '__main__':
    main()
