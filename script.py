import csv
from operator import length_hint
'''
id: the unique identifier from Hacker News for the post
title: the title of the post
url: the URL that the posts links to, if the post has a URL
num_points: the number of points the post acquired, calculated as the total number of upvotes minus the total number of downvotes
num_comments: the number of comments on the post
author: the username of the person who submitted the post
created_at: the date and time of the post's submission
'''



# Read the `artworks_clean.csv` file
opened_file = open('HN_posts_year_to_Sep_26_2016.csv')
read_file = csv.reader(opened_file)
hacker = list(read_file)
hacker_filtered = []




for row in hacker:
    num_comments = row[4]
    if isinstance(num_comments, int) is not True:
        hacker.remove(row)
        if num_comments == 0:
            hacker.remove(row)
        else:
            pass


#moma = moma[1:]
print(len(hacker))