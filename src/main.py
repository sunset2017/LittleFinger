# -*- coding: utf-8 -*-
'''
Created on Nov 23, 2017
@author: double_kingdoms
@attention: This code is for learning purpose. Don't propagate it for commercial use or without the consent of author
'''

from basics.ReponseAnalysis import Starter
from basics.DataStore import CsvFileWriter
import csv
from basics.DataType import SaleHistory, Product

if __name__=="__main__" :
    Starter().startDomesticTravelAnalysis("http://vacations.ctrip.com/")


'''
issues:
Have the connection established, but went to 404 page. So exception happens

(1). Have some metrics to see which ip works, which didn't work。
(2). For those returning None, store the page source. To see if it is returning empty data or just not fetching correctly.
(3). Data storage problem. File writing/creating/reading.
(4). Is there any reliable fake IP address
(5). Multi-threading.
'''
