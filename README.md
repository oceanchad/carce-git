# carce-git
part-time

# Using Googlemaps as Web Crawler to find Taiwn Depot and output the .csv

## Overview

  The company is looking for the all Taiwan Depot for the advertisement purpose.

  Traditionally, they ask part-time employee to manually search relevant information on Google maps, then copy the address, name,
and phone to the excel. During the work, the data collection of depot takes about 50% time.

  Due to the boring stuff, I decide to create the side project of data collection on google maps.

  Besides, user can type in keyword to search anything they like with filter list.

IDE: VSCODE
ENV: virtualenv
API: Googlemaps

## Installation Dependencies:
* Python 3
* pandas
* bs4
* Googlemaps

## How to Run

1. Preparing THE following material
* Google API
* searchword
* filter list folder path (severl lists in the folder are available) -> this will drop the row if column "name" contains any information in filter
* region list folder path (severl lists in the folder are available) -> this will drop the row if column "formatted_address" contains any information in region
* the folder location of raw data
* the data name
* the output file name you want

2. Notice
* during the process, you will encounter the steps require information above
* Output will show on your desktop
