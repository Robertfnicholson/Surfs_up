# Surfs Up Challenge – 
## Overview of Project
The challenge involved providing a potential investor with requested information on a business venture. 
The investor required running some analytics on a weather dataset. I used SQLite, SQLAlchemy, Flask & 
Python to develop these analytics. My code can be found in “SurfsUp_Challenge.ipynb.  </p>

## Project Steps
The investor requested information about temperature trends before opening the venture. Specifically, 
he requested multitemperature data for the months of June and December in Oahu, HI in order to 
determine if the surf and ice cream shop business is sustainable year-round. The project consisted of 
two technical analysis deliverables: (1) the June historical weather summary statistics and (2) the 
December historical weather summary statistics. To complete these I used Python, Pandas functions and 
methods, and SQLAlchemy to filter the date column of the measurements table in the hawaii.sqlite 
database to retrieve all the temperatures for the month of June and December. I then converted those 
temperatures to respective lists, created DataFrames from each list, and generated the summary 
statistics from each dataframe. </p>

## Challenges
I experienced challenges in learning SQLite and SQLAlchemy. These were much less intuitive than using 
PostgresSQL and pgAdmin. There were additional steps required for SQLite and SQLAlchemy to complete 
the challenge as compared to PostgreSQL and pgAdmin. I much prefer to develop databases and queries 
using PostgresSQL and pgAdmin. </p>

## Results

### Deliverables
I developed two deliverables to complete the process:

* the June historical weather summary statistics (see image below) and 

	![jun_temps.png](https://github.com/Robertfnicholson/Surfs_up/blob/5cff673e2af7715b86debb5439489bc1aa661a70/jun_temps.png)

* the December historical weather summary statistics (see image below).

	![dec_temps.png](https://github.com/Robertfnicholson/Surfs_up/blob/c228cec56070d5037b5910c96595961af4f07e87/dec_temps.png) </p>

### Key Differences in Weather Between June and December
There are three key differences in the weather between June and December:
*	June has higher temperatures than December, 3.9 degrees using the average and 4.0 degrees using 
	the median.
*	June has much higher minimum temperature than December, 8.0 degrees higher, but only 2.0 degrees 
	higher for the maximum temperature.
*	June has a lower standard deviation, 3.26, than December, 3.75. </p>

## Summary
The Oahu, HI weather analysis indicates that June has higher temperatures than December as measured 
by the mean, median, minimum and maximum temperatures. Also, June temperatures have a lower standard 
deviation than December temperatures. That is, June temperatures are more clustered around June’s 
mean temperature than December temperatures are around its respective mean.  </p>
