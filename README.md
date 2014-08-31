Redditbot - a simple bot for filtering posts and posting to them
=========
-v 0.01

ABOUT
=====

Redditbot was originally created as a bot for r/starcraft. It finds posts from users asking for help and then 
links them to available resources by searching for keywords in the 100 newest posts of a target subreddit
and submitting a comment if any of the keywords are found in the post title. Feel free to disect
and use Redditbot for your own projects.

GET STARTED
===========

1. Create a reddit account for your bot to use
2. Create settings.py
      1. Assign myUsername to your reddit account name
      2. Assign myPassword to your reddit account password
3. Edit variables in bot.py to match your goals
      1. 'user_agent' should be set in accordance with Reddit's rules: https://github.com/reddit/reddit/wiki/API
      2. 'subreddit' should be assigned to the name of the subreddit you wish to watch
      3. 'post' should be assigned to the text you wish to post
      4. 'keywords'should be a list containing the words you are searching for
      5. 'pollingVal' should be set to the number of posts you want to pull every 'time' minutes
      6. 'time' should be the number of minutes you want the program to wait after exhausting the list of keywords to search

Comments, suggestions, questions: ejmurra2@illinois.edu
