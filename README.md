# scraping_retrosheet
My python files that scrape data from [Retrosheet](http://www.retrosheet.org/).

### scrape_retrosheet.py
The file 'scrape_retrosheet.py' downloads every player's page from http://www.retrosheet.org/ and saves the pages either in the 'pitchers' or the 'position_players' folder.

Some Retrosheet player pages have extra info at the bottom. If there, these data are saved in the 'misc_data' folder.

### form_scraped.py
The file 'form_scraped.py' creates a new directory called 'pitching_data' that only contains the regular season pitching records for players, where applicable.

### form_scraped_further.py
The file 'form_scraped_further.py' forms the pitching files in the 'pitching_data' directory into .csv files for consumption by JavaScript.

### JS Usage
The first JS example using one of these pitching csv files is [here](http://bl.ocks.org/dhoboy/fe4f34b6debb7021105b5d8a1e514676)