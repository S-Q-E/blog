class Post:
    __slots__ = (
        'id', 
        'creation_date', 
        'update_date', 
        'user_id', 
        'title', 
        'description'
    )

    def __init__(
        self, 
        user_id, 
        title, 
        id = None, 
        creation_date = None, 
        update_date = None,
        description = None
    ):
        self.id = id
        self.user_id = user_id
        self.creation_date = creation_date
        self.update_date = update_date
        self.title = title
        self.description = description


    @classmethod
    def from_dict(cls, data):
        return Post(**data)