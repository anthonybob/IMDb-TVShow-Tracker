# IMDb TV Show Tracker
This script scrapes IMDb urls to find new episodes of TV shows you want to
keep up with. It reads the urls in the *urls.txt*, finds new episodes, 
and appends it to the *episodes.txt* file. You can specify the date to start
adding episodes from as a command line argument. The default day is the current
day. This option was added so that you can automate this script to run everyday,
and append any new episodes from the current date. 

---

## Files
- **urls.txt**
	- This is the input file for the code
	- The urls need to be the tv shows home page
	- Each url needs to go on a new line
	- Ensure that there are no empty lines

- **episodes.txt**
	- This is the output file for the code
	- Each new episode found is appended to the end of the file
	- You can delete or move the file if you want to restart it

- **imdbscrape.py**
	- This file is the script that finds new episodes
	- You can run it with Python with or without command line arguments

---

## Formatting
- **Command line Arguments**
	- Option 1 (Default)
		- No Arguments will append any new tv shows from the current day
	- Option 2 (year month day)
		- year month day should be represented as integers in that order
		- Will append any new tv shows beginning from the specified date 
