from Flight_Search import *
import datetime
import pandas as pd

#Aeropuertos
departure = "ALB"
arrival = "BQN"


#Rango de fecha en la que piensas salir 
depar_year1= 2024
depar_month1= 10
depar_day1 = 1

depar_year2= 2024
depar_month2= 10
depar_day2 = 5

#Cuantos dias piensas irte
vacation_duration = 7 

#Variabilidad  torelable en la duracion +/-
variability = 2

#Precio maximo dispuesto a pagar
price = 2000

#tiempo maximo de escala en horas
escala = 24


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


date_depar = f'{depar_year1-2000}/{depar_month1}/{depar_day1}'
date_depar = datetime.datetime.strptime(date_depar,"%y/%m/%d")

date_return1 = date_depar + datetime.timedelta(days = vacation_duration - variability)

return_year1 = date_return1.year
return_month1 = date_return1.month
return_day1 = date_return1.day

date_return2 = date_depar + datetime.timedelta(days = vacation_duration + variability)

return_year2 = date_return2.year
return_month2 = date_return2.month
return_day2 = date_return2.day

escala = f"30,{str(escala*60)}"
escala = str(escala)

#ida
date1 = (depar_year1, depar_month1, depar_day1)
date2 = (depar_year2, depar_month2, depar_day2)
ida = flight(date1,date2,2000,"30,1440", "ALB", "BQN").find()
#print(ida)

#vuelta
date3 = (return_year1, return_month1, return_day1)
date4 = (return_year2, return_month2, return_day2)
vuelta = flight(date3,date4,price,escala,arrival,departure).find()
#print(vuelta)

#full_trip = pd.DataFrame()

full_trip=pd.concat([ida,vuelta], ignore_index=True)
print(full_trip)

full_trip.to_excel("trip.xlsx")


