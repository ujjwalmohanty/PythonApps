# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:06:14 2020

@author: s28120
"""

import tkinter as tk
import requests
from PIL import Image, ImageTk

def weather(place):
    weather_key = '4725405d9628a58b79e7c90d39f4ab56' 
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q' : place, 'units':'Metric'}
    response = requests.get(url,params=params)
    weather_data = response.json()
    info_label['text'] = format_response(weather_data)
  
def format_response(weather_data):
    try:
        name = weather_data['name']
        desc = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        final_str = 'City : %s \nConditions : %s \nTemperature (C): %s' % (name,desc,temp)
    except:
        final_str = 'Could not be fetched at the moment.'
    return final_str        



def resize_image(event):
    new_width=event.width
    new_height=event.height
    image=copy_of_image.resize((new_width, new_height))
    background = ImageTk.PhotoImage(image)
    label.config(image=background)
    label.image=background

root = tk.Tk()
root.title('Weather')
height = int(root.winfo_screenheight()*0.5)
width = int(root.winfo_screenwidth()*0.4)
size = str(width) + 'x' + str(height)
root.geometry(size)

canvas = tk.Canvas(root)
canvas.place(relx=0,rely=0,relheight=1, relwidth=1)

background_image = Image.open('rainbow-weather.jpg')
copy_of_image = background_image.copy()
#Image = background_image.resize((width,height),Image.ANTIALIAS)
#background = ImageTk.PhotoImage(Image)
background = ImageTk.PhotoImage(background_image)

label = tk.Label(canvas,image=background)
#label.place(relx=0, rely=0, relheight = 1, relwidth=1)
label.bind('<Configure>',resize_image)
label.pack(fill='both', expand='yes')

frame1 = tk.Frame(canvas,bg='sky blue', bd=5)
frame1.place(relheight=0.09, relwidth=0.7, relx=0.15, rely=0.15)

frame2 = tk.Frame(canvas, bg='sky blue',bd=10)
frame2.place(relheight=0.5, relwidth=0.7, relx=0.15, rely=0.3)

area_txt = tk.Entry(frame1, font=('italica', 16))
area_txt.place(relx=0, rely=0, relheight = 1, relwidth=0.7)

submit_button = tk.Button(frame1, text='Get Weather', width=12, font=30,bg='yellow', command=lambda: weather(area_txt.get()))
submit_button.place(relx=0.75, rely=0,relheight = 1, relwidth=0.25)

info_label = tk.Label(frame2, font=('italica', 18), bd=5, bg='white', anchor='nw',justify='left')
info_label.place(relx=0, rely=0, relheight = 1, relwidth=1)

root.mainloop()





#4725405d9628a58b79e7c90d39f4ab56

#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}