from tkinter import *
from PIL import ImageTk, Image
import requests
from datetime import date
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from suntime import Sun

def fetch_weather():
    city = user_name_input_area.get()
    
    url = "https://www.google.com/search?q=weather" + city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str_data = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str_data.split('\n')
    time = data[0]
    sky = data[1]

    today = date.today()
    current_date = today.strftime("%x")

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude

    sun = Sun(latitude, longitude)
    time_zone = today
    sun_rise = sun.get_local_sunrise_time(time_zone)
    sun_dusk = sun.get_local_sunset_time(time_zone)

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(city)

    print("")
    print("HI EVERYONE, WELCOME TO TODAY'S WEATHER REPORT......")
    print("")
    print("****", city.upper(), "*****")
    print("")
    print("Date: ", current_date)
    print("Time : ", time)
    print("Temperature : ", temp)
    print("Sky Description : ", sky)
    print("Sun rise at : ", sun_rise.strftime('%H:%M'))
    print("Dusk at : ", sun_dusk.strftime('%H:%M'))
    print("Latitude : ", latitude)
    print("Longitude : ", longitude)
    print("")
    print("Description of the Location :")
    print(getLoc.address)
    print("")
    print("Have a nice day :) :)")

# GUI setup
win = Tk()
win.geometry("500x313")

i = Image.open("C:\\Users\\shreenithi\\Downloads\\imgonline.gif")
back_end = ImageTk.PhotoImage(i)
lbl = Label(win, image=back_end)
lbl.place(x=0, y=0)

text = Label(win, text="HI !! HERE IS TODAY'S WEATHER REPORT", font="Vijaya,18 ")
text.place(x=60, y=110)

user_name = Label(text="ENTER THE CITY ", bg="orange")
user_name.place(x=40, y=60)

user_name_input_area = Entry(win, width=50)
user_name_input_area.place(x=150, y=60)

enter_button = Button(win, text="Tell Weather!! ", width=15, bg="orange", command=fetch_weather)
enter_button.pack(pady=145)

win.mainloop()
