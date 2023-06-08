import json

class SpaceGroup:
    
    def __init__(self,
                    id=None,
                    name=None,
                    slug=None,
                    add_members_to_space_group_on_space_join=False,
                    allow_members_to_create_spaces=True,
                    automatically_add_members_to_new_spaces=False,
                    hide_non_member_spaces_from_sidebar=True,
                    is_hidden_from_non_members=False,
                    space_order_array=[],
                    position=1) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.add_members_to_space_group_on_space_join = add_members_to_space_group_on_space_join
        self.allow_members_to_create_spaces = allow_members_to_create_spaces
        self.automatically_add_members_to_new_spaces = automatically_add_members_to_new_spaces
        self.hide_non_member_spaces_from_sidebar = hide_non_member_spaces_from_sidebar
        self.is_hidden_from_non_members = is_hidden_from_non_members
        self.space_order_array = space_order_array
        self.position = position
    
    def to_json(self):
        return json.dumps(self.__dict__)

    def to_pretty_json(self):
        return json.dumps(self.__dict__, indent=4)
