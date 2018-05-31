# Python 3.6.5
# Counts any mention of Overwatch heroes. Then compares to see which
# heroes are the most popular.
import praw  # Reddit API
import re    # Regex (to parse comments)
import time  # To loop program every 2 hours

heroes = {'genji':['genji','gengu'],
        'mccree':['cree'],
        'pharah':['pharah'],
        'reaper':['reaper'],
        'soldier':['soldier'],
        'tracer':['tracer'],
        'bastion':['bastion'],
        'hanzo':['hanzo'],
        'junkrat':['junk'],
        'mei':['mei'],
        'torbjorn':['torb'],
        'widowmaker':['widow'],
        'd.va':['d.va','dva'],
        'reinhardt':['rein'],
        'roadhog':['hog'],
        'winston':['winston','monkey','gorilla','ape', 'harambe'],
        'zarya':['zarya'],
        'lucio':['lucio'],
        'mercy':['mercy', 'moth'],
        'symmetra':['sym'],
        'zenyatta':['zen'],
        'ana':['ana'],
        'sombra':['sombra'],
        'orisa':['orisa'],
        'doomfist':['doom'],
        'moira':['moira'],
        'brigette':['brig'],
        }  # Heroes and their nicknames. Fullname not needed.

def scrape_messages():
    # Scrapes all comments into a string
    messages = ''  # Where all comments we examine are kept.
    r = praw.Reddit('OW_Research')  # As defined in praw.ini
    subreddit = r.subreddit('overwatch')  # scrape /r/overwatch
    
    comments = subreddit.comments(limit=200)
    for comment in comments:
        messages += comment.body  # .body is the comment text.
        
    return messages


def count(messages):
    # Counts all mentions of every hero.
    # NOTE: Does not store the data anywhere yet!
    
    # --ADD HERE-- Read the hero_count.txt file and record numbers.
    for hero in heroes:
        count = len(re.findall("|".join(sorted(
            heroes[hero],reverse=True)),messages))
        print(f'{hero}:{count}')
        # --ADD HERE-- add new numbers to files found in txt file.
        # --ADD HERE-- then close and save file.
        
        
while True:
    count(scrape_messages())
    time.sleep(7200)  # Wait 2 hours until next check.
