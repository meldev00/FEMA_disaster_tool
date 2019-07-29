# Project_5

## Problem Statement

In the event of a disaster, it is essential for goverment and private forces to rapidly identify potential threats and communicate effectively about damage and rescue efforts if needed. FEMA has developed a list of seven life-lines that are deemed essential to successfully address the most pressing issues with the most clarity across the board. Using these seven life-lines as search criteria, this study was conducted for New Light Technologies with two goals:

  - to predict where the largest threat is to the life-lines prior to a disaster
  - build a tool that takes in a zip code and returns the potential impact of a disaster to the lifelines

## Data Dictionary


## Repository Structure


## Executive Summary

In the early stages of this study, we outlined the data that would be most important for FEMA if a natural disaster were to hit. We determined there are two stages of a disaster preparedness plan that we found of importance. The first stage is a preemptive look at what areas of a given location are already in danger of low life-line support. This is done by clustering the life-lines using ____________ and can give insight for support systems that FEMA can put in place for when/if an event occurs. The second stage is a  reactionary approach to an event shortly after it begins. We created a tool that takes the event(disaster) center and radius as inputs and returns the life-lines and their respective categories in that area. The life-lines are ordered by proximity to the event center, so the operator can make assumptions about which may be affected depending on the type of disaster.

(extras) 
- potential danger due to population size?
- historical data for that area

Our group decided to use Google Maps and the Google Place Search API to locate places that may fall into one of the seven life-line categories. We chose Google Maps over other sources like Yelp because we thought that Google might be able to provide places that would not show up on Yelp. Louisiana was picked as the prototype city because of its history of unfortunate weather and potential access to historical data.

- Google APIs obtained to pull location of lifelines in a given area
- Research done on FEMA lifelines and previous disasters
- Dataset found: https://www.ncdc.noaa.gov/stormevents/ftp.jsp

## Findings and Conclusions

## Resources
https://www.fema.gov/media-library-data/1543953591582-d3437147e8954b5c9b8469dc2d173531/Revised_Community_Lifelines_Information_Sheet.pdf
