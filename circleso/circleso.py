import requests
import json

class CircleRestClient():

    def __init__(self, api_key):
        self.base_url = 'https://app.circle.so/api/v1'

        self.rest_client = requests.Session()
        self.rest_client.headers = {
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json',
        }
        self.rest_client.verify = True

    # Base HTTP Methods
    def _get(self, endpoint, params=None):
        url = self.base_url + endpoint
        r = self.rest_client.get(url, params=params)
        return r

    def _post(self, endpoint, params=None, data=None):
        url = self.base_url + endpoint
        r = self.rest_client.post(url, params=params, data=data)
        return r

    def _put(self, endpoint, params=None, data=None):
        url = self.base_url + endpoint
        r = self.rest_client.put(url, params=params, data=data)
        return r

    def _delete(self, endpoint, params=None, data=None):
        url = self.base_url + endpoint
        r = self.rest_client.delete(url, params=params, data=data)
        return r

    # "Me" methods
    # @doc: https://api.circle.so/#ae81bd02-ad31-4c83-b17d-34d377bfb929
    # @url: https://app.circle.so/api/v1/me
    def get_me(self):
        r = self._get('/me')
        if r.status_code == 200:
            return r.json()
        else:
            return None
    
    # "Communities" methods
    # @doc: https://api.circle.so/#ad5f356e-0038-4706-a30a-ed4a0fcd306a
    # @url: https://app.circle.so/api/v1/communities
    def get_communities_index(self):
        r = self._get('/communities')
        if r.status_code == 200:
            return r.json()
        else:
            return None

    # @doc: https://api.circle.so/#2c3224e1-f3bb-49b4-b84a-9f7c64496c6c
    # @url: https://app.circle.so/api/v1/communities/{{community_id}}?slug=super-community
    def get_community(self, cid, params=None):
        if params is None:
            return None

        r = self._get('/communities/' + cid, params=params)
        if r.status_code == 200:
            return r.json()
        else:
            return None

    # "Space group" methods
    # @doc: https://api.circle.so/#014e5b0f-22ef-4b24-a012-8b2adccedcf6
    # @url: https://app.circle.so/api/v1/space_groups?community_id={{community_id}}
    def get_space_groups_index(self, cid):
        r = self._get('/space_groups', params={
            'community_id': cid
        })
        if r.status_code == 200:
            return r.json()
        else:
            return None

    # @doc: https://api.circle.so/#1fc9cbd1-6b59-44b9-8026-e82516df7191
    # @url: https://app.circle.so/api/v1/space_groups/:id?community_id={{community_id}}
    def get_space_group(self, cid, sgid):
        r = self._get('/space_groups/' + sgid, params={
            'community_id': cid
        })
        if r.status_code == 200:
            return r.json()
        else:
            return None

    # @doc: https://api.circle.so/#5d3e5d71-6813-40e2-9953-f6b7811a4ed9
    # @url: https://app.circle.so/api/v1/space_groups?community_id={{community_id}}
    def create_space_group(self, cid, data):

        payload = json.loads(data)

        if 'name' not in payload or 'slug' not in payload:
            return None

        print(payload)

        r = self._post('/space_groups', params={
            'community_id': cid
        }, data=data)

        print(r.status_code)

        if r.status_code == 200:
            return r.json()
        else:
            return None


    # "Space group members" methods

    # "Spaces" methods
    def get_spaces_index(self, cid):
        r = self._get('/spaces', params={
            'community_id': cid,
        })

        if r.status_code == 200:
            return r.json()
        else:
            return None

    # @doc: https://api.circle.so/#b0e5503e-e553-4b7a-bcfc-2d092b9a1cb0
    # @url: https://app.circle.so/api/v1/spaces/:id?community_id={{community_id}}
    def get_space(self, cid, sgid):

        if cid is None or sgid is None:
            return None

        r = self._get('/spaces/' + str(sgid), params={
            'community_id': str(cid),
        })

        print(r.text)
        print(r.status_code)

        if r.status_code == 200:
            return r.json()
        else:
            return None

    def create_space(self, cid, data):

        payload = json.loads(data)

        r = self._post('/spaces', params={
            'community_id': cid,
            'name': payload['name'],
            # 'is_private': payload['is_private'],
            # 'is_hidden_from_non_members': payload['hide_post_settings'],
            # 'is_hidden': False,
            'slug': payload['slug'],
            'space_group_id': payload['space_group_id'],
            # 'space_type': 'basic',
            # 'display_view': 'list',
        })

        if r.status_code == 200:
            return r.json()
        else:
            print(r.text)
            return None

    # "Space members" methods

    # "Posts" methods
    # def get_posts_index(self, cid, sid):
    #     r = self._get('/spaces/' + sid + '/posts', params={
    #         'community_id': cid,
    #     })

    #     if r.status_code == 200:
    #         return r.json()
    #     else:
    #         return None

    # "Comments" methods
    # def get_comments_index(self, cid, sid):
    #     r = self._get('/spaces/' + sid + '/comments', params={
    #         'community_id': cid,
    #     })

    #     if r.status_code == 200:
    #         return r.json()
    #     else:
    #         return None
