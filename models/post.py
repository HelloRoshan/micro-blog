__author__ = 'Roshan Budhathoki'

class Post(object):
    def __init__(self, blog_id, title, content, author, create_date, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.create_date = create_date
        self.id = id #post id which is unique

    def save_to_mongo(self):
        Database.insert(collection= 'posts', data=self.json())

    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.create_date
        }

    @staticmethod
    def from_mongo(id):
        #Post.from mongo('123')
        return Database.find_one(collection = 'posts',query = {'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection ='posts', query ={'blog_id': id})]