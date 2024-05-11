
from datetime import date, timedelta
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import sys
import requests
import json
import datetime
import serpapi


class flight:
    
    def __init__(self,date1 ,date2,price,layover_duration,departure,arrival):
        
        self.date1 = date1
        self.date2 = date2
        self.price = price
        self.layover_duration = layover_duration
        self.departure =  departure
        self.arrival = arrival
        self.year1 = self.date1[0] 
        self.month1 = self.date1[1]
        self.day1 = self.date1[2]
        self.year2 = self.date2[0]
        self.month2 = self.date2[1]
        self.day2 = self.date2[2]
    
        self.main()

    def convert(self,n):
        return str(datetime.timedelta(minutes = n)).replace(',','')
    
    def daterange(self,start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def sep_info(self,params):
        search = serpapi.search(params)

        read_content = search

        read_content['other_flights']
        flight_info = []
        flightdfs = []
        masterdf = pd.DataFrame()
        departure_airports = []
        arrival_airports = []
        flight_duration=[]
        airline=[]
        departure_time=[]
        arrival_time = []
        price=[]
        total_duration= []
        layover_duration = []
        layover_airport = []
        all_flight = read_content['other_flights']
        #print(all_flight)
        for flight in all_flight:
            p = flight['price']
            tot_dur = flight['total_duration']
            lay= flight['layovers']
            f = flight['flights']
            dep_airports=[]
            arr_airports =[]
            f_dur=[]
            airln=[]
            dep_time=[]
            arr_time = []
            for flight in f:
                dep = flight['departure_airport']['id']
                dep_airports.append(dep)

                dp_tm= flight['departure_airport']['time']
                dep_time.append(dp_tm)

                arr= flight['arrival_airport']['id']
                arr_airports.append(arr)

                arr_tm = flight['arrival_airport']['time']
                arr_time.append(arr_tm)

                dur = flight['duration']
                dur = self.convert(dur)
                f_dur.append(dur)

                line = flight['airline']
                airln.append(line)

            lay_durlst =[]
            lay_airptlst=[]
            for l in lay:
                lay_dur = l['duration']
                lay_dur = self.convert(lay_dur)
                lay_durlst.append(lay_dur)

                lay_airpt = l['id']
                lay_airptlst.append(lay_airpt)


            price.append(f'${p}')

            total_dur=self.convert(tot_dur)
            total_duration.append(total_dur)
            layover_airport.append(lay_airptlst)
            layover_duration.append(lay_durlst)
            departure_airports.append(dep_airports[0])
            arrival_airports.append(arr_airports[-1])
            flight_duration.append(f_dur)
            airline.append(airln[0])
            departure_time.append(dep_time[0])
            arrival_time.append(arr_time[-1])
            

        flight_dict={'Airline':airline,  'Departure':departure_airports, 'Destination':arrival_airports, 'Total Duration':total_duration, 'Price':price, 'Layovers':layover_airport}
        flight_df = pd.DataFrame(flight_dict)
        return flight_df
    
    def main(self):
        date_lst=[]
        maindf = pd.DataFrame()
        start_date = date(self.year1,self.month1,self.day1)
        end_date = date(self.year2,self.month2,self.day2)
        for single_date in self.daterange(start_date, end_date):
            date_lst.append(single_date.strftime("%Y-%m-%d"))
    #json to pandas tutorial = https://github.com/MrFuguDataScience/JSON/tree/master
        print(date_lst)
        if len(date_lst) > 6:
            sys.exit()

        #r = requests.get('https://serpapi.com/search.json?engine=google_flights&departure_id=PEK&arrival_id=AUS&outbound_date=2024-04-28&return_date=2024-05-04&currency=USD&hl=en')
        i=0
        while i < len(date_lst):
            params = {
                "engine": "google_flights",
                "departure_id": self.departure ,
                "arrival_id": self.arrival,
                "type": 2,
                "max-price": self.price,
                "layover_duration": self.layover_duration,
                "outbound_date": date_lst[i],
                "return_date": None,
                "currency": "USD",
                "hl": "en",
                "api_key": "ced838a8b3bbbfab06a1ace2fedae5861c000f70741a82c08c33adb613f7dffa"
            }

            x = self.sep_info(params)
            maindf=pd.concat([maindf,x], ignore_index=True)
            i += 1
            print(x)
        return print(maindf)

date1 = (2024, 10,20)
date2 = (2024,10,22)
y = flight(date1,date2,2000,"30,1440","ALB","BQN")
print(y)