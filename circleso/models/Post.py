import json

class Post:
    
    def __init__(self,
                    id=None,
                    status=None,
                    name=None,
                    body={},
                    slug=None,
                    url=None,
                    space_name=None,
                    space_slug=None,
                    space_id=None,
                    user_id=None,
                    user_email=None,
                    user_name=None,
                    comments_count=0,
                    community_id=None,
                    hide_meta_info=False,
                    user_avatar_url=None,
                    published_at=None,
                    created_at=None,
                    updated_at=None,
                    cover_image=None,
                    cover_image_url=None,
                    cardview_thumbnail=None,
                    cardview_thumbnail_url=None,
                    is_comments_enabled=True,
                    is_comments_closed=False,
                    is_liking_enabled=True,
                    flagged_for_approval_at=None,
                    custom_html=None,
                    likes_count=0,
                    user_posts_count=0,
                    user_topics_count=0,
                    user_likes_count=0,
                    user_comments_count=0
                    ) -> None:
        self.id = id
        self.name = name
        self.status = status
        self.slug = slug
        self.body = body
        self.url = url
        self.space_name = space_name
        self.space_slug = space_slug
        self.space_id = space_id
        self.user_id = user_id
        self.user_email = user_email
        self.user_name = user_name
        self.comments_count = comments_count
        self.community_id = community_id
        self.hide_meta_info = hide_meta_info
        self.user_avatar_url = user_avatar_url
        self.published_at = published_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.cover_image = cover_image
        self.cover_image_url = cover_image_url
        self.cardview_thumbnail = cardview_thumbnail
        self.cardview_thumbnail_url = cardview_thumbnail_url
        self.is_comments_enabled = is_comments_enabled
        self.is_comments_closed = is_comments_closed
        self.is_liking_enabled = is_liking_enabled
        self.flagged_for_approval_at = flagged_for_approval_at
        self.custom_html = custom_html
        self.likes_count = likes_count
        self.user_posts_count = user_posts_count
        self.user_topics_count = user_topics_count
        self.user_likes_count = user_likes_count
        self.user_comments_count = user_comments_count
    
    def to_json(self):
        return json.dumps(self.__dict__)

    def to_pretty_json(self):
        return json.dumps(self.__dict__, indent=4)
