# This is a reddit bot that browses /r/starcraft and posts helpful links for new players
# V 0.03

import pdb
import time
import praw
from settings import myUsername,myPassword,myPost,mySub,myPoll,myAgent,myTime,myKeys

print "Please see README for documentation"

debug = False

runDebug = raw_input("Debug tools? (Y/N)")
def debug():
    if runDebug == 'y' or runDebug == 'Y':
        return True
    else:
        return False
        
print "Debug set to: ", debug()

if debug() == True:
    sleepTime = str(raw_input("How many seconds should we wait before we pull topics? \n")) or int(myTime)
    hibernate = int(sleepTime)
    
else:
    sleepTime = str(raw_input("How many minutes should we wait before we pull topics? \n")) or int(myTime)
    hibernate = int(sleepTime) * 60

prewords = raw_input('What keywords are we looking for? \n --separate keywords with a space\n')

dir = {'userName':str(raw_input("Username: \n")) or str(myUsername),
'myPassword':str(raw_input("Password: \n")) or str(myPassword),
'userAgent':str(raw_input("State your user agent: \n")) or str(myAgent),
'subreddit':str(raw_input("Subreddit to search: \n")) or str(mySub),
'post':str(raw_input("Text to post: \n")) or str(myPost),
'pollingVal':raw_input("How many topics should we pull? \n") or int(myPoll),
}

words= map (str, prewords.split()) or myKeys
dir.update({'keywords':words})
dir.update({'snooze':str(hibernate) + ' seconds'})

r = praw.Reddit(user_agent = dir['userAgent'])

def debugger(debug):
    if debug() == True:
        with open('debug.log', 'w') as file:
            file.write(str(dir))
        with open('debug.log', 'r') as els:
            for var in dir.keys():
                myvalue  = dir[var]
                print var,"is equal to", myvalue
debugger(debug)

#myUsername = str(raw_input("Username: \n")) or str(myUsername)



#myPassword = str(raw_input("Password: \n")) or str(myPassword)



#user_agent = str(raw_input("State your user agent: \n")) or str(myAgent)




#subreddit = str(raw_input("Subreddit to search: \n")) or str(mySub)


#post = str(raw_input("Text to post: \n")) or str(myPost)


#prewords = raw_input('What keywords are we looking for? \n (separate keywords with a space)')
#keywords = map(str, prewords.split()) or myKeys


#pollingVal = raw_input("How many topics should we pull? \n") or int(myPoll)


if debug() == False:
    r.login(myUsername,myPassword)
else:
    print "No login during debug"

def collect():
    return r.get_content(url = 'http://www.reddit.com/r/'+str(dir['subreddit']+'/new/'),
    limit = int(dir['pollingVal'])) #collects posts to search for keywords

cycle = 0

while True:
    if cycle == 1 and debug() == True:
        print "Cycled from hibernate"   
    x = 1
    while x < 2:
         #pulls page data based on subreddit
        titles = r.get_subreddit(dir['subreddit']) #pulls titles out of page data
        print titles
        for title in titles.get_hot(limit = dir['pollingVal']):
            print title.title
            keywordFound = 0
            for keyword in dir['keywords']:
                if x < 2:
                    if keyword in title.title.lower(): #If the title contains a keyword
                        title.add_comment(dir['post']) #post comment
                        keywordFound = 1
                        print "posted"
                        break
                    else:
                        x = 3
                else:
                    break
            if not keywordFound:
                print "No key words found, hibernating for ", hibernate, " seconds."
                time.sleep(int(hibernate))
                cycle = 1
                break

