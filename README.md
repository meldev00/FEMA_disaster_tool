# Project_5

## Problem Statement

In the event of a disaster, it is essential that goverment and private forces rapidly identify potential threats and communicate damage and rescue efforts effectively. The Federal Emergency Management Agency, known as FEMA, has developed a list of seven lifelines which represent establishments most essential to supporting human populations during times of crisis. The lifelines are as follows: safety and security; food, water, and sheltering; health and medical; energy; communications; transportation; and hazardous waste. With these seven lifelines in mind, our study was conducted for New Light Technologies with two goals:

  - to predict where the largest threat is to the lifelines prior to a disaster
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

New Light Technologies has tasked our team with creating a tool to identify vulnerable areas in a community and project possible effects if a disaster event were to hit that area. The metrics we used to estimate community vunlerablility are the status of the seven lifelines provided by FEMA. These metrics were established after multiple large scale disasters in 2017. "...[T]he lifeline construct can help responders and decision-makers rapidly determine the scope, complexity, and
interdependent impacts of an incident."[2]   

Our group decided to use Google Maps and the Google Place Search API to locate places that may fall into one of the seven lifeline categories. We chose Google Maps over other sources like Yelp, due in part to the fact that Google provides many more businesses than Yelp's API. New Orleans was picked as our prototype city due to its history of severe weather. Using the Google API, we wrote a function in order to pull businesses within a specified radius of a user-inputed latitude an longitude. Each business has a corresponding categorical "type" assigned by Google: this was used to determine into which of the seven lifelines each business would fall.[3] Useful information pulled from the Google API included: business name, address, type, and latitude/longitude. This information did have to be re-engineered in order to be used with our classification and clustering algorithms.

In the early stages of this study, we outlined the data that would be most important for FEMA if a natural disaster were to hit. We determined there are two stages of a disaster preparedness plan that we found important:

The first stage is a preemptive look at what areas of a given location are already in danger of low lifeline support. We tried to accomplish this task by using KMeans clustering; however, an un-clustered heatmap of lifeline-businesses proved to be more representational in this context. Given this, FEMA can put in place support systems for when/if an event occurs. Based on our model you can see below the areas in New Orleans that have high concentrations of specific lifelines.

[Insert picture here]  

As expected the highest concentration of lifelines is in the downtown area. Nevertheless, it is worth noting the other areas in which there are concentrations in the surrounding areas. In preparing for possible natural disasters it is suggested that FEMA consider these locations as highly vulnerable.

The second stage is a reactionary approach to an event shortly after it begins. We created a tool that takes the event (disaster) center and radius as inputs and returns the lifelines and their respective categories within that area. The lifelines are ordered by proximity to the event center, so the operator can make assumptions about which may be affected depending on the type of disaster. In order to determine proximity from a central event center, each lifeline's distance was calculated using a function utilizing latitude and longitude. This infomation can then be visualized for the user in multiple ways. Using map pop-ups, the user can see information about individual lifeline locations. Looking at the heatmap, the user can also see how individual lifelines are distributed in a given area.

[Insert Images here]  


- Google APIs obtained to pull location of lifelines in a given area
- Research done on FEMA lifelines and previous disasters
- Dataset found: https://www.ncdc.noaa.gov/stormevents/ftp.jsp

## Findings and Conclusions

## Resources
[1] https://www.fema.gov/media-library-data/1543953591582-d3437147e8954b5c9b8469dc2d173531/Revised_Community_Lifelines_Information_Sheet.pdf  
[2] https://www.fema.gov/media-library-data/1550596625129-99b1671f270c18c934294a449bcca3ce/Tab2a.CommunityLifelinesToolkitPresenterGuide_508.pdf  
[3] https://developers.google.com/places/web-service/supported_types  
