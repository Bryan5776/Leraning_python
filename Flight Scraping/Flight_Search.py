
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
    
    def __init__(self,date1,date2,price,layover_duration,departure,arrival):
        
        self.date1 = date1
        self.date2 = date2
        self.price = price
        self.layover_duration = layover_duration
        self.departure =  departure
        self.arrival = arrival

    @staticmethod
    def convert(n):
        return str(datetime.timedelta(minutes = n)).replace(',','')
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
    def main(self):
        date_lst=[]
        year1 = self.date1[0]
        month1 = self.date1[1]
        day1 = self.date1[2]
        year2 = self.date2[0]
        month2 = self.date2[1]
        day2 = self.date2[2]



        start_date = date(year1,month1,day1)
        end_date = date(year2,month2,day2)
        for single_date in daterange(start_date, end_date):
            date_lst.append(single_date.strftime("%Y-%m-%d"))
    #json to pandas tutorial = https://github.com/MrFuguDataScience/JSON/tree/master
        if len(date_lst) > 6:
            sys.exit()
        print(date_lst)



if __name__ == '__main__':
    main()


'''
        def main():     
            r = requests.get('https://serpapi.com/search.json?engine=google_flights&departure_id=PEK&arrival_id=AUS&outbound_date=2024-04-28&return_date=2024-05-04&currency=USD&hl=en')



            for dates in date_lst:
                params = {
                  "engine": "google_flights",
                  "departure_id": self.departure ,
                  "arrival_id": self.arrival,
                  "type": 2,
                  "max-price": self.price,
                  "layover_duration": self.layover_duration,
                  "outbound_date": "2024-07-18",
                  "return_date": None,
                  "currency": "USD",
                  "hl": "en",
                  "api_key": "ced838a8b3bbbfab06a1ace2fedae5861c000f70741a82c08c33adb613f7dffa"
                }

                search = serpapi.search(params)



                read_content = search
                #with open ('flight.json') as access_json:
                #    read_content = json.load(access_json)

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
                def sep_info():

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
                            dur = convert(dur)
                            f_dur.append(dur)

                            line = flight['airline']
                            airln.append(line)

                        lay_durlst =[]
                        lay_airptlst=[]
                        for l in lay:
                          lay_dur = l['duration']
                          lay_dur = convert(lay_dur)
                          lay_durlst.append(lay_dur)

                          lay_airpt = l['id']
                          lay_airptlst.append(lay_airpt)


                        price.append(f'${p}')

                        total_dur=convert(tot_dur)
                        total_duration.append(total_dur)
                        layover_airport.append(lay_airptlst)
                        layover_duration.append(lay_durlst)
                        departure_airports.append(dep_airports[0])
                        arrival_airports.append(arr_airports[-1])
                        flight_duration.append(f_dur)
                        airline.append(airln[0])
                        departure_time.append(dep_time[0])
                        arrival_time.append(arr_time[-1])

                        #dep = f['departure_airport']
                        #print(f)
                        #flightj = pd.json_normalize(flight)
                        #flight = flightj['flights']
                        #dep = flight['departure_airport']
                        #print(dep)

                    sep_info()
                    #print(departure_airports)
                    #print(arrival_airports)
                    #print(flight_duration)
                    #print(airline)
                    #print(departure_time)
                    #print(arrival_time)
                    #print(price)
                    #print(total_duration)
                    #print(layover_duration)
                    #print(layover_airport)

                    flight_dict={'Airline':airline,  'Departure':departure_airports, 'Destination':arrival_airports, 'Total Duration':total_duration, 'Price':price, 'Layovers':layover_airport}

                    flight_df = pd.DataFrame(flight_dict)

                    print(flight_df)
                    return flight_df
'''