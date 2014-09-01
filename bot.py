# This is a reddit bot that browses new threads in a target subreddit and posts comment on threads that contain user-defined keywords
#V 0.1

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
    sleepTime = str(raw_input("How many seconds should we wait between topic pulls? \n")) or int(myTime)
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


if debug() == False:
    r.login(myUsername,myPassword)
else:
    print "No login during debug"

def handleRateLimit(cycle=1):
    while True:
        try:
            if cycle > 1 and debug() == True:
                print "Cycled", cycle, "times"   
            x = True
            found = 0
            
            while x == True:
            
                submissionPuller = r.get_content(url = 'http://www.reddit.com/r/'+str(dir['subreddit']+'/new/'),
                limit = int(dir['pollingVal'])) #grabs comments
                
                for submission in submissionPuller:
                    title = submission.title #locates title
                    
                    print title
                    b = True
                    for keyword in dir['keywords']:
                    
                        if b == True:
                            name = ''
                            if keyword in submission.title.lower(): 
                                #submission.add_comment(dir['post'])
                                name = submission.title
                                del (submission) #checks for keywords in the title; if found, posts comment and deletes submission from list
                                
                                print "posted"
                                b = False
                                found += 1
                            else:
                                print "no post"
                                b = False
                                cycle += 1
                                print cycle, found
                                with open('hotlist.log', 'w') as burn:
                                    burn.write(str(name))
                                time.sleep(.1)
                                if cycle + found == 1000:
                                    print "finished them all"
                                    time.sleep(100)
                                    x = False
                                
                                
        except praw.errors.RateLimitExceeded as error:
            print '\tSleeping for %d seconds' % error.sleep_time
            time.sleep(error.sleep_time)
            
handleRateLimit()
