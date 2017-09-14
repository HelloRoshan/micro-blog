__author__ = 'Roshan Budhathoki'

from models.post import Post
from database import Database

post = Post('Hello World', 'Beginning of Programming Journey', 'Miguel')
post2 = Post('Language', 'What language to choose?', 'Anonymous')

print(post.title)
print(post2.content)
