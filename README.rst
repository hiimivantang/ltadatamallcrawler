===============================
LTA Datamall Crawler
===============================

.. image:: https://img.shields.io/travis/hiimivantang/ltadatamallcrawler.svg
        :target: https://travis-ci.org/hiimivantang/ltadatamallcrawler

.. image:: https://img.shields.io/pypi/v/ltadatamallcrawler.svg
        :target: https://pypi.python.org/pypi/ltadatamallcrawler


LTA is responsible for planning, operating, and maintaining Singapore’s
land transport and systems.

This repository contains a python script to get data from LTA’s
`datamall`_ (free).

Available APIs and project status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+-------+-----------------------------------------------+------+
| description      | freq  | url                                           | stat |
|                  |       |                                               | us   |
+==================+=======+===============================================+======+
| Bus Arrival      | 1m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  |       | ce/BusArrival                                 |      |
+------------------+-------+-----------------------------------------------+------+
| Bus Services     | ad-ho | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  | c     | ce/BusServices                                |      |
+------------------+-------+-----------------------------------------------+------+
| Bus Routes       | ad-ho | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  | c     | ce/BusRoutes                                  |      |
+------------------+-------+-----------------------------------------------+------+
| Bus Stops        | ad-ho | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  | c     | ce/BusRoutes                                  |      |
+------------------+-------+-----------------------------------------------+------+
| Taxi             | 2m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
| Availability     |       | ce/Taxi-Availability                          |      |
+------------------+-------+-----------------------------------------------+------+
| Carpark          | 1m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
| Availability     |       | ce/CarParkAvailability                        |      |
+------------------+-------+-----------------------------------------------+------+
| ERP Rates        | ad-ho | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  | c     | ce/ERPRates                                   |      |
+------------------+-------+-----------------------------------------------+------+
| Estimated Travel | 5m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
| Times            |       | ce/EstTravelTimes                             |      |
+------------------+-------+-----------------------------------------------+------+
| Faulty Traffic   | 2m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
| Lights           |       | ce/FaultyTrafficLights                        |      |
+------------------+-------+-----------------------------------------------+------+
| Road Openings    | 1d    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  |       | ce/RoadOpenings                               |      |
+------------------+-------+-----------------------------------------------+------+
| Road Works       | 1d    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  |       | ce/RoadWorks                                  |      |
+------------------+-------+-----------------------------------------------+------+
| Traffic Images   | 5m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  |       | ce/Traffic-Images                             |      |
+------------------+-------+-----------------------------------------------+------+
| Traffic          | 2m    | http://datamall2.mytransport.sg/ltaodataservi | DONE |
| Incidents        |       | ce/TrafficIncidents                           |      |
+------------------+-------+-----------------------------------------------+------+
| Traffic Speed    | 5m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
| Bands            |       | ce/TrafficSpeedBands                          |      |
+------------------+-------+-----------------------------------------------+------+
| VMS / EMAS       | 2m    | http://datamall2.mytransport.sg/ltaodataservi | TODO |
|                  |       | ce/VMS                                        |      |
+------------------+-------+-----------------------------------------------+------+

.. _datamall: https://www.mytransport.sg/content/mytransport/home/dataMall.html
