from bs4 import BeautifulSoup
import urllib2
import re

BASE_URL = "http://www.retrosheet.org/boxesetc/";

# top level page
home_page = urllib2.urlopen(BASE_URL)
soup = BeautifulSoup(home_page, "lxml")

# it groups names like AU - AZ...
player_pages_grouping_anchors = soup.find_all(href=re.compile("MISC/PLD"))
player_page_urls = []

# digs into the name category pages of player page urls and
# creates an array of every player page
for player_anchor_group in player_pages_grouping_anchors:
  page = urllib2.urlopen(BASE_URL + player_anchor_group['href'])
  page_soup = BeautifulSoup(page, "lxml")
  player_anchor = page_soup.find_all(href=re.compile("\.\.\/[A-Z]+\/[A-Za-z0-9]*\.htm"))
  player_page_urls += player_anchor

for player_page_anchor in player_page_urls:
  page = urllib2.urlopen(BASE_URL + player_page_anchor['href'][3:])

  # open page
  page_soup = BeautifulSoup(page, "lxml")

  # get player name from title of page
  title = page_soup.find('title').get_text().split(" ")
  title = "_".join(title)

  # player's stats are in pre tags
  pres = page_soup.find_all('pre') # pres as in pre's

  # figure out if the player has a pitching record
  pitcher = False
  for elem in pres:
    if 'Pitching Record' in elem.get_text():
      pitcher = True

  # create file with that player name, open for writing
  if pitcher == True:
    f = open('pitchers/' + title, 'w')
  else:
    f = open('position_players/' + title, 'w')

  # also open that player's misc file
  f_misc = open("misc_data/" + title, 'w')

  for elem in pres:
    if 'Record' in elem.get_text(): # batting record, pitching record...
      f.write(elem.get_text())
    else:
      f_misc.write(elem.get_text()) # extra information: trades, etc...

  f.close()
  f_misc.close()

