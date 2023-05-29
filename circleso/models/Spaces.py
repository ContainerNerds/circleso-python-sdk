import json

class Spaces:
    
    def __init__(self,
                    id=None,
                    name=None,
                    slug=None,
                    emoji=None,
                    space_group_id=54575,
                    space_group_name="Raphy's Test",
                    url="https://app.circle.so/c/api-test-purposes",
                    community_id=11111,
                    is_private=True,
                    hide_post_settings=None,
                    display_view="posts",
                    post_ids=[],
                    is_post_disabled=None,
                    space_type="basic",
                    hide_topic_settings=None,
                    is_topic_disabled=None,
                    topic_ids=[]
                    ) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.emoji = emoji
        self.space_group_id = space_group_id
        self.space_group_name = space_group_name
        self.url = url
        self.community_id = community_id
        self.is_private = is_private
        self.hide_post_settings = hide_post_settings
        self.display_view = display_view
        self.post_ids = post_ids
        self.is_post_disabled = is_post_disabled
        self.space_type = space_type
        self.hide_topic_settings = hide_topic_settings
        self.is_topic_disabled = is_topic_disabled
        self.topic_ids = topic_ids
    
    def to_json(self):
        return json.dumps(self.__dict__)

    def to_pretty_json(self):
        return json.dumps(self.__dict__, indent=4)
