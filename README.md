Redditbot - a simple bot for filtering posts and posting to them
=========
-v 0.03

ABOUT
=====

Redditbot was originally created as a bot for r/starcraft. It finds posts from users asking for help and then 
links them to available resources by searching for keywords in the 100 newest posts of a target subreddit
and submitting a comment if any of the keywords are found in the post title. Feel free to disect
and use Redditbot for your own projects.

GET STARTED
===========

1. Create a reddit account for your bot to use
2. (optional)Create settings.py
      1. Assign myUsername to your reddit account name
      2. Assign myPassword to your reddit account password
      3. Assign myAgent to your desired User Agent
      4. Assign mySub to your targeted subreddit
      5. Assign myPost to your desired content for submit
      6. Assign myPoll to the number of submissions you are requesting
      7. Assign myTime to the number of minutes between requests (debugging mode returns seconds)
      8. Assign myKeys to a list of your desired keywords
3. Run bot.py

Comments, suggestions, questions: ejmurra2@illinois.edu
