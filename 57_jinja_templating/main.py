from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    result = response.json()
    return render_template("index.html", post = result)

@app.route('/post/<num>')
def post(num):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    result = response.json()
    return render_template("post.html", result_title = result[int(num)]["title"], result_subtitle = result[int(num)]["subtitle"], result_body = result[int(num)]["body"])

if __name__ == "__main__":
    app.run(debug=True)


#! Her Solution

# from flask import Flask, render_template
# from post import Post
# import requests
#! [1]
#? Get the JSON once and make an object using the Post class.
#? Then make a list / dict and load all of those post objects inside
# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
# post_objects = []
# for post in posts:
#     post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
#     post_objects.append(post_obj)

# app = Flask(__name__)

#! [2]
#? Send the list of post objects
# @app.route('/')
# def get_all_posts():
#     return render_template("index.html", all_posts=post_objects)

#! [4]
#? If the index matches with any post object's id or post.id
#? Send the entire post object to the post.html
# @app.route("/post/<int:index>")
# def show_post(index):
#     requested_post = None
#     for blog_post in post_objects:
#         if blog_post.id == index:
#             requested_post = blog_post
#     return render_template("post.html", post=requested_post)


# if __name__ == "__main__":
#     app.run(debug=True)

#* The index.html
#! [3]
#? Look at the for loop. It is outside two divs
#? Also, get the index (domain/.../index) using the post.id
# <body>
# <div class="wrapper">
#     <div class="top">
#         <div class="title"><h1>My Blog</h1></div>
#     </div>

#     {% for post in all_posts: %}
#     <div class="content">
#         <div class="card ">
#             <h2>{‌{ post.title }}</h2>
#             <p>{‌{ post.subtitle }}</p>
#             <a href="{‌{ url_for('show_post', index=post.id) }}">Read</a>
#         </div>

#     </div>
#     {% endfor %}

# </div>
# </body>