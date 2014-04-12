from slistener import SListener
import time, tweepy, sys, traceback

## auth. 
## TK: Edit the username and password fields to authenticate from Twitter.
username = ''
password = ''
#auth     = tweepy.BasicAuthHandler(username, password)
#api      = tweepy.API(auth)

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main( mode = 1 ):
    track = []
    f = open('url_0412.txt')
    for line in f:
        track.append(line.strip('\n'))
    f.close()
    print track
    follow = []
            
    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(follow), len(track))

    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print "*** print_tb:"
        traceback.print_tb(exc_traceback, limit=20, file=sys.stdout)
        print "*** print_exception:"
        traceback.print_exception(exc_type, exc_value, exc_traceback, limit=20, file=sys.stdout)
        #print >> sys.stderr, 'Encountered Exception:', e
        #print "error!"
        stream.disconnect()

   # results = api.search(q="obama", until="2013-01-01")
#    results = api.search(q="o")
#    for r in results:
#        print r.text
if __name__ == '__main__':
    main()
