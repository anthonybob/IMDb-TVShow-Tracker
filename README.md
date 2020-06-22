# IMDb TV Show Tracker
This script scrapes IMDb urls to find new episodes of TV shows you want to
keep up with. It reads the urls in the *urls.txt*, finds new episodes, 
and appends it to the *episodes.txt* file. You can specify the date to start
adding episodes from as a command line argument. The default day is the current
day. This option was added so that you can automate this script to run everyday,
and append any new episodes from the current date. 

---

## Formatting
- **urls.txt**
	- The urls need to be the tv shows home page
	- Each url needs to go on a new line
	- Ensure that there are no empty lines

- **Command line Arguments**
	- Option 1 (Default)
		- No Arguments will append any new tv shows from the current day
	- Option 2 (year month day)
		- year month day should be represented as integers in that order
		- Will append any new tv shows beginning from the specified date 
