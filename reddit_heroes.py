# Python 3.6.5
# Counts any mention of Overwatch heroes. Then compares to see which
# heroes are the most popular.
import praw
import re

heroes = {'genji':['genji','gengu'],
        'mccree':['mccree', 'cree'],
        'pharah':['pharah'],
        'reaper':['reaper'],
        'soldier':['soldier','soldier76', 's76'],
        'tracer':['tracer'],
        'bastion':['bastion'],
        'hanzo':['hanzo', 'hanjo'],
        'junkrat':['junkrat', 'junk','rat'],
        'mei':['mei'],
        'torbjorn':['torb'],
        'widowmaker':['widow'],
        'd.va':['d.va','dva'],
        'reinhardt':['rein'],
        'roadhog':['roadhog', 'hog'],
        'winston':['winston','monkey','gorilla','ape'],
        'zarya':['zarya'],
        'lucio':['lucio'],
        'mercy':['mercy', 'moth'],
        'symmetra':['sym'],
        'zenyatta':['zen'],
        'ana':['ana'],
        'sombra':['sombra'],
        'orisa':['orisa','horse','cow'],
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
    for hero in heroes:
        count = len(re.findall("|".join(sorted(
            heroes[hero],reverse=True)),messages))
        print(f'{hero}:{count}')

count(scrape_messages())
