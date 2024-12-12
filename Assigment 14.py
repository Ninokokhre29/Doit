class User():
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.comments = []
        self.friends = set()
        self.likes = []

    def add_friends(self, user):
        self.friends.add(user)

    def create_post(self, content):
        post = Post(content,self)
        self.posts.append(post)

    def create_comment(self, post, content):
        comments = Comments(content,self)
        post.comments.append(comments)
        self.comments.append(Comments)

    def like_post(self, post):
        post.likes.append(self)

    def like_comment(self, comment):
        comment.likes.append(self)

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = []

class Comments:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []

user1 = User("Ana")
user2 = User("Gio")
user3 = User("Lika")
user1.create_post("I posted")
user1.add_friends(user2)
user1.add_friends(user3)
user2.create_comment(user1.posts[0], "I commented")
user1.like_comment(user1.posts[0].comments[0])

print(f"{user1.username}'s friends are : {[friend.username for friend in user1.friends]}")
print(f"{user1.username} posted: {[post.content for post in user1.posts]}")
comment_dict = {comment.author.username : comment.content for comment in user1.posts[0].comments}
print(f"Comments on post '{user1.posts[0].content}' : {comment_dict}")
for comment in user1.posts[0].comments:
    print(f"comment : '{comment.content}' liked by : {[user.username for user in comment.likes]}")

