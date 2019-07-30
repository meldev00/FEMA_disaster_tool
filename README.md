# Project_5

## Problem Statement

In the event of a disaster, it is essential for goverment and private forces to rapidly identify potential threats and communicate effectively about damage and rescue efforts if needed. FEMA has developed a list of seven life-lines that are deemed essential to successfully address the most pressing issues with the most clarity across the board. Using these seven life-lines as search criteria, this study was conducted for New Light Technologies with two goals:

  - to predict where the largest threat is to the life-lines prior to a disaster
  - build a tool that takes in a zip code and returns the potential impact of a disaster to the lifelines

## Data Dictionary
|Feature|Type|Dataset|Description|
|-------|----|-------|-----------|
|FEMA Lifeline|string|full_dataset.csv|Description of one of FEMA's seven lifelines.|
|geometry|dictionary|full_dataset.csv|Multiple variations on latitude and Longitude information about a location.|
|name|string|full_dataset.csv|Name of business or location.|
|types|string|full_dataset.csv|Google categorical type.|
|vicinity|string|full_dataset.csv|Address of location.|
|lat|float|full_dataset.csv|Latitude of location.|
|lng|float|full_dataset.csv|Longitude of location.|
|Website_FEMA|int|full_dataset.csv|Numeric representation FEMA categorical lifelines.|
|YEARMONTH|int|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|Year and month of storm event.|
|EPISODE_ID|int|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|Episode identifying number.|
|EVENT_ID|int|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|Event identifying number.|
|LOCATION_INDEX|int|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|?|
|RANGE|float|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|?|
|AZIMUTH|string|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|?|
|LOCATION|string|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|City of event.|
|LATITUDE|float|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|?|
|LONGITUDE|float|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|?|
|LAT2|int|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|?|
|LON2|int|StormEvents_locations-ftp_v1.0_d2019_c20190716.csv|?|

## Repository Structure


## Executive Summary  

In the event of a natural disaster it is important to be prepared. To this end New Light Technologies has tasked our team with creating a tool to identify vulnerable areas in a community and project possible effects if a disaster event were to hit that area.  

The metrics we will be using to estimate community vunlerablility are set forth by FEMA's(Federal Emergency Management Agency) seven lifelines: Safety and Security, food water and sheltering, health and medical, energy, communication, transportation, and hazardous material. These metrics were implemented after multiple large scale disasters of 2017. "...the lifeline construct can help responders and decision-makers rapidly determine the scope, complexity, and
interdependent impacts of an incident."[2]   

In the early stages of this study, we outlined the data that would be most important for FEMA if a natural disaster were to hit. We determined there are two stages of a disaster preparedness plan that we found of importance. The first stage is a preemptive look at what areas of a given location are already in danger of low life-line support. This is done by clustering the life-lines using a spacial aglorithm, KMeans clustering. Given this, FEMA can put in place support systems for when/if an event occurs.  

The second stage is a  reactionary approach to an event shortly after it begins. We created a tool that takes the event(disaster) center and radius as inputs and returns the life-lines and their respective categories in that area. The life-lines are ordered by proximity to the event center, so the operator can make assumptions about which may be affected depending on the type of disaster.  

Our group decided to use Google Maps and the Google Place Search API to locate places that may fall into one of the seven life-line categories. We chose Google Maps over other sources like Yelp because we thought that Google might be able to provide places that would not show up on Yelp. Louisiana was picked as the prototype city because of its history of unfortunate weather and potential access to historical data. Using the google API we wrote a function in order to pull businesses within a specified radius of a user inputed latitude an longitude. Each business is has a corresponding categorical "type" 

- Google APIs obtained to pull location of lifelines in a given area
- Research done on FEMA lifelines and previous disasters
- Dataset found: https://www.ncdc.noaa.gov/stormevents/ftp.jsp

## Findings and Conclusions

## Resources
[1] https://www.fema.gov/media-library-data/1543953591582-d3437147e8954b5c9b8469dc2d173531/Revised_Community_Lifelines_Information_Sheet.pdf  
[2] https://www.fema.gov/media-library-data/1550596625129-99b1671f270c18c934294a449bcca3ce/Tab2a.CommunityLifelinesToolkitPresenterGuide_508.pdf  
[3] https://developers.google.com/places/web-service/supported_types  
