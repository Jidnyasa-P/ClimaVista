from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title("ClimaVista")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExcercises")
        location=geolocator.geocode(city)
        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        timezone.config(text=result)
        long_lat.config(text=(location.latitude,"°N,",location.longitude,"°E"))
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"{YOUR_API_KEY}"
           # Replace {YOUR_API_KEY} with your openweather api key.
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        humidity=json_data['main']['humidity']
        pressure=json_data['main']['pressure']
        wind=json_data['wind']['speed']

        
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))
        t.config(text=(temp,"°C"))
        h.config(text=(humidity,"%"))
        p.config(text=(pressure,"hPa"))
        w.config(text=(wind,"m/s"))
        d.config(text=description)

    except Exception as e:
        messagebox.showerror("Weather App","City not found")

##logo
logo_image=PhotoImage(file="logo.png")
root.iconphoto(False,logo_image)

##search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify='center',width=17,font=('poppins',25,'bold'),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

##icon
image_icon=PhotoImage(file="icon.png")
icon=Label(image=image_icon)
icon.place(x=150,y=100)

#bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

##label
label1=Label(root,text="WIND",font=('Helvetica',15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=('Helvetica',15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=('Helvetica',15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=('Helvetica',15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=('arial',70,'bold'),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
p.place(x=670,y=430)

##clock
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#timezone
timezone=Label(root,font=('Helvetica',20,'bold'),fg="white",bg="#1ab5ef")
timezone.place(x=600,y=20)

long_lat=Label(root,font=('Helvetica',15,'bold'),fg="white",bg="#1ab5ef")
long_lat.place(x=600,y=50)

root.mainloop()

