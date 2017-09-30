# Academic lineage network in D3.js

This code lets you put an interactive tree of your academic lineage on a website. The website code is entirely in `HTML` and `JavaScript`, so it should work fine on any web host. There's a working example on [my website here](http://www-personal.umich.edu/~jwlock/lineage/lineage.html).

# How to use
- Clone or download the files in this github repository.
- Test that the code works for you.
	- Upload `lineage.html` and `data.json` to your web host.
	- Go to that webpage (e.g. `www.examle.edu/~yourname/lineage.html`) to see if it displays.
- Enter your lineage information.
	- Edit the `people.csv` file and replace the example data. 
		- The `name` column is displayed online, while `full_name` is just to help keep track of who is who in case of common names. 
		- You can enter any ID number you want for people, so long as each is unique.
	- Edit the `links.csv` file and replace the example data. 
		- Enter the advisee's ID number into the `target` column, and their advisor's number into the `source` column. 
		- Advisees may have multiple advisors: just enter multiple rows with the same target and different sources.
	- Save both files (again as `.csv` format).
- Run the `format_data.py` code to convert the information in the CSV files into `data.json` for the website to read.
	- In mac and linux, simply open this folder in the terminal / command prompt and type `python format_data.py`
		- Windows users can run python too, but it's a little more complicated. 
- Edit the `lineage.html` file. 
	- There are places for google analytics code and adding your own name/text.
- Upload the `lineage.html` and `data.json` files to your web host.


# Requirements
## Web page
- Nothing special. Any website host that lets you upload the `lineage.html` and `data.json` file will do. 

## Python
- Just for converting the data you enter into a format the web code can easily understand.
- pandas
- numpy
- sys
- json
- titlecase (optional, disabled by default)
