import urllib.parse
import requests
from datetime import datetime, date

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, MD"
key = "PL3t1O9pauSij1Lk1GYAYNwbGeRVlXT4"


now = date.today()


name = input("What is Your Name, Traveller?: ")
vehicle = input("What vehicle are you using?: ")
while True:

   
   orig = input("Source Location: ")

   if orig == "quit" or orig == "q":

        break

   dest = input("End Location: ")

   if dest == "quit" or dest == "q":

        break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

   print("URL: " + (url))

   json_data = requests.get(url).json()

   json_status = json_data["info"]["statuscode"]

   if json_status == 0:

       
       print("API Status: " +  str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("Welcome to GROUP 3 4ITH")
       print("The Date Today is: ")
       print(now)
       print("**********************************************")
       print("                                              ")
       print("Hello there,  " +(name))
       print("Your vehicle is: " +(vehicle))
       print("Directions from " +  (orig) + " to " + (dest))
       print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
       print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("Fuel Used (Liter): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
       print("                                              ")
       print("=============================================")
   elif json_status == 402:
          print("**********************************************")

          print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

          print("**********************************************\n")

   elif json_status == 611:
         print("**********************************************")

         print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

         print("**********************************************\n")
   else:
         print("************************************************************************")

         print("For Staus Code: " + str(json_status) + "; Refer to:")

         print("https://developer.mapquest.com/documentation/directions-api/status-codes")

         print("************************************************************************\n")


