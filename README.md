# lta-datamall-crawler

[![Build Status](https://travis-ci.org/hiimivantang/ltadatamallcrawler.svg?branch=master)](https://travis-ci.org/hiimivantang/ltadatamallcrawler)

LTA is responsible for planning, operating, and maintaining Singapore's land transport and systems.

This repository contains a python script to get data from LTA's [datamall][1] (free). 


### Available APIs and project status

| description            | freq   | url                                                                 |status|  
|------------------------|--------|---------------------------------------------------------------------|------| 
| Bus Arrival            | 1m     | http://datamall2.mytransport.sg/ltaodataservice/BusArrival          | TODO | 
| Bus Services           | ad-hoc | http://datamall2.mytransport.sg/ltaodataservice/BusServices         | TODO | 
| Bus Routes             | ad-hoc | http://datamall2.mytransport.sg/ltaodataservice/BusRoutes           | TODO | 
| Bus Stops              | ad-hoc | http://datamall2.mytransport.sg/ltaodataservice/BusRoutes           | TODO |
| Taxi Availability      | 2m     | http://datamall2.mytransport.sg/ltaodataservice/Taxi-Availability   | TODO |
| Carpark Availability   | 1m     | http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailability | TODO |
| ERP Rates              | ad-hoc | http://datamall2.mytransport.sg/ltaodataservice/ERPRates            | TODO |
| Estimated Travel Times | 5m     | http://datamall2.mytransport.sg/ltaodataservice/EstTravelTimes      | TODO |
| Faulty Traffic Lights  | 2m     | http://datamall2.mytransport.sg/ltaodataservice/FaultyTrafficLights | TODO |
| Road Openings          | 1d     | http://datamall2.mytransport.sg/ltaodataservice/RoadOpenings        | TODO |
| Road Works             | 1d     | http://datamall2.mytransport.sg/ltaodataservice/RoadWorks           | TODO |
| Traffic Images         | 5m     | http://datamall2.mytransport.sg/ltaodataservice/Traffic-Images      | TODO |
| Traffic Incidents      | 2m     | http://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents    | DONE |
| Traffic Speed Bands    | 5m     | http://datamall2.mytransport.sg/ltaodataservice/TrafficSpeedBands   | TODO |
| VMS / EMAS             | 2m     | http://datamall2.mytransport.sg/ltaodataservice/VMS                 | TODO |

[1]:https://www.mytransport.sg/content/mytransport/home/dataMall.html

