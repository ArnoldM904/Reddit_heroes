# Python 3.6.5
# Counts any mention of Overwatch heroes. Then compares to see which
# heroes are the most popular.
import praw  # Used for interaction with Reddit
import re    # Used for sorting through names and nicknames.

subreddit = 'overwatch'
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
        }  # Lists heroes and their popular aliases.

def scrape_messages(subreddit):
    # Scrapes all comments into a string
    messages = ''
    r = praw.Reddit('OW_Research')  # As defined in praw.ini
    subreddit = r.subreddit(subreddit)
    # Scrape content and add it into messages here.
    return messages


def count(messages):
    # Counts all mentions of every hero.
    # NOTE: Does not store the data anywhere yet!
    for hero in heroes:
        count = len(re.findall("|".join(sorted(
            heroes[hero],reverse=True)),messages))
        print(f'{hero}:{count}')

count(scrape_messages(subreddit))
