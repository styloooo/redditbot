# This is a reddit bot that browses /r/starcraft and posts helpful links for new players

#Basic functionality: scan newly submitted posts for keywords, if keyword found post comment with links
#Needs to poll /r/starcraft/new/ every 15 minutes
#Structure: Scan /r/starcraft/new/
           #If title contains keyword
                #post comment
           #Else wait 15 mins and check for new posts

import time
import praw
from settings import myUsername,myPassword

user_agent = ("Script to inform new users of"
    " r/starcraft about available"
     " resources. -/u/Eli_Murray") #sets user agent
     
r = praw.Reddit(user_agent = user_agent) #sets r to PRAW module

subreddit = 'starcraft'

post = "Test text." #sets text to be submitted as comment

keywords = ["new player", "noob", "beginner", "help"] #keywords to search for in post title

pollingVal = 100
time = 10
hibernate = time * 60


r.login(myUsername,myPassword) #logs in

def collect(subreddit):
    return r.get_new(pollingVal) #collects posts to search for keywords

while True:
    generator = r.get_subreddit(subreddit) #assigns subbreddit to search
    titles = collect(generator) #takes submissions and assigns them to title
    for title in titles:
        keywordFound = 0
        for keyword in keywords:
            if keyword in title.title.lower(): #If the title contains a keyword
                title.title.add_comment(post) #post comment
                keywordFound = 1
                break
            else:
                break
        if not keywordFound:
            print "No key words found, hibernating"
            time.sleep(hibernate)

