# lta-datamall-crawler

[![Build Status](https://travis-ci.org/hiimivantang/ltadatamallcrawler.svg?branch=master)](https://travis-ci.org/hiimivantang/ltadatamallcrawler)

LTA is responsible for planning, operating, and maintaining Singapore's land transport and systems.

This repository contains a python module to get data from LTA's [datamall][1] (free). Maybe I should not name this repository as LTA-datamall-crawler but you can always create a simple cronjob for crawling purposes.



### Installation

```python

pip install ltadatamallcrawler

```

Or, you can always clone this project and run the script directly.



### Requirements

You will need LTA datamall API key and GUUID.
To get the API key, click "Request for API Access" on the [LTA datamall page][3]. API key will be granted immediately. Using the API key, you can generate a GUUID on [this page][4].


### Usage

```bash
# to view the available APIs:

lta-datamall-crawler -h




# Expected output:

Usage: lta-datamall-crawler [options]

#Options:
#  -h, --help            show this help message and exit
#
#  Available APIs:
#    Please select one!
#
#    --traffic-incidents
#    --bus-arrival       
#    --bus-routes        
#    --estimated-travel-times
#    --road-openings     
#    --erp-rates         
#    --vms-emas          
#    --taxi-availability
#    --faulty-traffic-lights
#    --carpark-availability
#    --bus-stops         
#    --traffic-images    
#    --traffic-speed-bands
#    --bus-services      
#    --road-works 
 



# to get 'real-time' traffic incidents data 
 
lta-datamall-crawler --traffic-incidents

 
```




### Motivation

Sometimes it can be quite labourous to create boilerplate codes for doing HTTP get requests to different APIs even though the [requests package][2] can make life slightly easier. I've created this project to make life easier for people who are interested in getting traffic data from Singapore LTA datamall. 


### Available API

| description            | freq     | url                                                                 |
|------------------------|----------|---------------------------------------------------------------------| 
| Bus Arrival            | 1m       | http://datamall2.mytransport.sg/ltaodataservice/BusArrival          | 
| Bus Services           | ad-hoc   | http://datamall2.mytransport.sg/ltaodataservice/BusServices         | 
| Bus Routes             | ad-hoc   | http://datamall2.mytransport.sg/ltaodataservice/BusRoutes           | 
| Bus Stops              | ad-hoc   | http://datamall2.mytransport.sg/ltaodataservice/BusRoutes           |
| Taxi Availability      | 2m       | http://datamall2.mytransport.sg/ltaodataservice/Taxi-Availability   |
| Carpark Availability   | 1m       | http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailability |
| ERP Rates              | ad-hoc   | http://datamall2.mytransport.sg/ltaodataservice/ERPRates            |
| Estimated Travel Times | 5m       | http://datamall2.mytransport.sg/ltaodataservice/EstTravelTimes      |
| Faulty Traffic Lights  | 2m       | http://datamall2.mytransport.sg/ltaodataservice/FaultyTrafficLights |
| Road Openings          | 1d       | http://datamall2.mytransport.sg/ltaodataservice/RoadOpenings        |
| Road Works             | 1d       | http://datamall2.mytransport.sg/ltaodataservice/RoadWorks           |
| Traffic Images         | 5m       | http://datamall2.mytransport.sg/ltaodataservice/Traffic-Images      |
| Traffic Incidents      | 2m       | http://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents    |
| Traffic Speed Bands    | 5m       | http://datamall2.mytransport.sg/ltaodataservice/TrafficSpeedBands   |
| VMS / EMAS             | 2m       | http://datamall2.mytransport.sg/ltaodataservice/VMS                 |





### Project Roadmap

* use as a library in python script
* allow HTTP requests with parameters for filtering results
* create appropriate unittests



[1]:https://www.mytransport.sg/content/mytransport/home/dataMall.html
[2]:https://pypi.python.org/pypi/requests/2.11.1
[3]:https://www.mytransport.sg/content/mytransport/home/dataMall.html
[4]:http://datamall.mytransport.sg/tool.aspx
