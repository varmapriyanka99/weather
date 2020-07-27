from tkinter import *
import requests
import json

master=Tk()

def weather_display():
    api_key="a10f7334b6d4f531b6ae18d8fe12bc2e"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    city=city_name.get()
    complete_url=base_url+"&q="+city.title()+"&APPID="+api_key

    response=requests.get(complete_url)

    x=response.json()
    t1.delete("1.0", END)
    if x["cod"]!="404":
        s=''
        z=x["weather"]
        y=z[0]
        des=y["description"]
        '''t1.insert(END, des.title())'''
        s=s+des.title()
        i=y["main"]
        if i=="Clear":
           s=s+"\nIt's a sunny day."
           t1.insert(END, s)
        elif i=="Clouds":
            s=s+"It's cloudy today."
            t1.insert(END, s)
        elif i=="Thunderstorm" or i=="Rain" or i=="Drizzle":
            s=s+"\nCarry an umbrella."
            t1.insert(END, s)
        elif i=="Snow":
            s=s+"\nWear a sweater."
            t1.insert(END, s)
        elif i=="Fog" or i=="Haze":
            s=s+"\nChances of low visiblity."
            t1.insert(END, s)
        elif i=="Mist":
            s=s+"\nPleasant weather"
            t1.insert(END, s)
        elif i=="Smoke" or i=="Sand" or i=="Dust" or i=="Ash":
            s=s+"\nCover your face."
            t1.insert(END, s)
        elif i=="Squall":
            s=s+"\nBe careful."
            t1.insert(END, s)
        elif i=="Tornado":
            s=s+"\nTornado Alert. Stay inside"
            t1.insert(END, s)
    else:
        t1.insert(END, "City not found")

'''city_name=input()'''



Label(master, text="Enter city name: ").grid(row=0, column=0)
city_name=StringVar()
e1=Entry(master,textvariable=city_name)
e1.grid(row=0,column=1)

b1=Button(master, text="Get weather", command=weather_display)
b1.grid(row=0,column=2)

t1=Text(master, height=2, width=40)
t1.grid(row=1, column=0)

master.mainloop()
