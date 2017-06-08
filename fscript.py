from app.models import User, Post
from app import db

import whoosh

import datetime
u = User.query.get(1)
p = Post(body='my first post', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
p = Post(body='my second post', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
p = Post(body='my third and last post', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()

posts = Post.query.filter(Post.body== 'my first').first()
print(posts)

posts = Post.query.filter(Post.body.contains('last')).first()
print(posts)
