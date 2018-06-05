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
    # Then adds the counts to existing amounts saved and stores them in a file.
    
    # Records the count number for each hero in the existing txt file.
    file_name = 'hero_mentions.txt'
    with open(file_name) as f:
        lines = [x.strip() for x in f]  # Records as hero:count
        existing_count = [x.split(':')[1] for x in lines]

    # Counts new appearances found in recently scraped data.
    new_count = []
    for hero in heroes:
        count = len(re.findall("|".join(sorted(
            heroes[hero],reverse=True)),messages))
        new_count.append(int(count))
       
    # Sums the existing counts with the new finds.
    updated_count = []
    for num in range(len(existing_count)):
        updated_count.append(int(existing_count[num]) + new_count[num])

    # Writes the file in a human-readable format of the total hero:count
    updated_file = []
    f = open(file_name, 'w+')
    count = 0
    for hero in heroes:
        entry = f'{hero}:{str(updated_count[count])}'
        updated_file.append(entry)
        count += 1
    for entry in updated_file:
        f.write(f'{entry}\n')

loops = 0
# Repeat forever, giving console updates every 2 hours.
while True:
    count(scrape_messages())
    loops += 1
    print(f'{loops * 2} hours have been recorded.')
    time.sleep(7200)  # Wait 2 hours until next check.
