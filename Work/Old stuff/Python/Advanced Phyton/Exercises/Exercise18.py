blog_posts = [
    {"Photos" : 3,"Likes": 21, "Comments" : 2},
    {"Likes" : 13,"Comments" : 2,"Shares" : 1},
    {"Photos" : 5,"Likes" : 33,"Comments" : 8,"Shares" : 3},
    {"Comments" : 4,"Shares" : 2},
    {"Photos" : 8,"Comments" : 1,"Shares" : 1},
    {"Photos" : 3,"Likes" : 19, "Comments" : 3},
]
max_likes = 0
max_shares = 0
for index in blog_posts:
    try:
        max_likes += index["Likes"]
    except KeyError:
        index["Likes"] = 0
    try:
        max_shares += index["Shares"]
    except KeyError:
        index["Shares"] = 0
print(f"All posts combined have {max_likes} likes")
print(f"All posts combined have {max_shares} shares")


