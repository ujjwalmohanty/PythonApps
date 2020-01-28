# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:32:42 2020

@author: s28120
"""
import tkinter as tk
from PIL import Image, ImageTk
import requests


class Display:
    
    api_key = 'jIiLXX4cdVX7VVH56LSFk66IiYm1'
    statListBat = ['No. Of Matches : ', 'Total Runs : ', 'Batting Average : ', 'Strike Rate : ', 'Highest Score : ']
    statListBowl = ['No. Of Matches : ', 'Total Wickets : ', 'Bowling Average : ', 'Strike Rate : ', 'Best Bowling : ']
    
    def __init__(self,root):
        self.canvas = tk.Canvas(root)
        self.canvas.pack()
        
        self.image = Image.open('cricket_background.jpg')
        self.image_copy = self.image.copy()
        self.background = ImageTk.PhotoImage(self.image)
        
        self.label = tk.Label(self.canvas,image=self.background)
        self.label.bind('<Configure>',self.resize_image)
        self.label.pack(fill='both', expand = 'yes')
        
        self.frame1 = tk.Frame(self.canvas, bg='light green',bd=5)
        self.frame1.place(relx=0.15,rely=0.15, relwidth=0.7,relheight=0.08)
        
        
        self.frame2 = tk.Frame(self.canvas, bg='light green',bd=5)
        self.frame2.place(relx=0.05,rely=0.3, relwidth=0.9,relheight=0.6)
        
        self.entry = tk.Entry(self.frame1, font=40)
        self.entry.place(relx=0,rely=0,relheight=1, relwidth=0.8)
        self.getData = tk.Button(self.frame1, text='Get Stats', bg='white', command=lambda: self.getPlayingRole(self.entry.get()))
        self.getData.place(relx=0.85,rely=0,relheight=1,relwidth=0.15)
        
        self.label1 = tk.Label(self.frame2, anchor='nw',justify='left',bg='white')
        self.label1.place(relx=0, rely=0, relheight=1, relwidth=0.49)
        self.label2 = tk.Label(self.frame2, anchor='nw',justify='left',bg='white')
        self.label2.place(relx=0.51, rely=0, relheight=1, relwidth=0.49)
        
        
    def resize_image(self,event):
        new_height = event.height
        new_width = event.width
        self.image1 = self.image_copy.resize((new_width,new_height))
        self.background1 = ImageTk.PhotoImage(self.image1)
        self.label.config(image=self.background1)

    def getPlayer(self,name):
        #return('Player stats' + ': ' + name)
        pid_url = 'https://cricapi.com/api/playerFinder'
        params = {'apikey':Display.api_key, 'name':name}
        response = requests.get(pid_url,params=params)
        player_id= response.json()
        return player_id['data'][0]['pid']
        
    def getPlayingRole(self,name):
        #try:
            pId = self.getPlayer(name)
            stats_url = 'https://cricapi.com/api/playerStats'
            params = {'apikey' :Display.api_key,'pid':pId}
            response = requests.get(stats_url,params=params)
            playerData = response.json()['data']
            playingRole = (response.json()['playingRole']).lower()
            if ('batsman' in playingRole):
                self.getBattingstats(playerData)
            elif ('bowler' in playingRole):
                self.getBowlingstats(playerData)
            elif ('allrounder' in playingRole):
                self.getBattingstats(playerData)
                self.getBowlingstats(playerData)
#            if playingRole in Display.playingRoleList:
#                  print(response.json()['data'])
                
       
        #except:
         #   self.label1['text'] = 'Please recheck the name'
     
        
    def getBattingstats(self, playerInfo):
        print (playerInfo['batting']['ODIs']) 
                
        

    def getBowlingstats(self, playerInfo):        
        print (playerInfo['bowling'])  
       
       
root = tk.Tk()
x=int(root.winfo_screenwidth()*0.6)
y=int(root.winfo_screenheight()*0.7)
z = str(x) +'x'+str(y)
root.geometry(z)
root.title('Test and ODI stats')
a = Display(root)
root.mainloop()        




#Key: jIiLXX4cdVX7VVH56LSFk66IiYm1
#pid url https://cricapi.com/api/playerFinder
#stats url https://cricapi.com/api/playerStats