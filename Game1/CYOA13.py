# RidleyP13
# Made by: David Ridley
# Email: dridley1@cnm.edu
# Purpose: This program gives you geographical information about a
# given location using a GUI and information from a database
# Last Updated: 4/11/22

import tkinter as tk
from GeoPoint import GeoPoint
import sqlite3

window = tk.Tk()

# Global variable to display results
result = "Results go here"

# Create button function that takes user input to calculate and display the result

def coords():

    # Draw Data from Database
    conn = sqlite3.connect('test.db')
    test = conn.execute("SELECT LocationNum, Lat, Lon, Desc from LocInfo")
    x = test.fetchall()
    
    loc1 = x[0]
    loc2 = x[1]
    loc3 = x[2]
    loc4 = x[3]
    loc5 = x[4]

    lat1 = loc1[1]
    lon1 = loc1[2]
    desc1 = loc1[3]
    
    lat2 = loc2[1]
    lon2 = loc2[2]
    desc2 = loc2[3]
    
    lat3 = loc3[1]
    lon3 = loc3[2]
    desc3 = loc3[3]
    
    lat4 = loc4[1]
    lon4 = loc4[2]
    desc4 = loc4[3]
    
    lat5 = loc5[1]
    lon5 = loc5[2]
    desc5 = loc5[3]

    # Get info from User
    
    lat = float(ent1.get())
    lon = float(ent2.get())
    desc = ent3.get()

    # Use GeoPoint class to process data
    
    location = GeoPoint(lat, lon, desc)
    location.set_point(lat, lon)
    location.get_point()
    location.set_distance()

    # Re-format data
        
    loc_dist = location.get_distance()
    loc_dist[0] = "{:.2f}".format(loc_dist[0])
    loc_dist[1] = "{:.2f}".format(loc_dist[1])
    loc_dist[2] = "{:.2f}".format(loc_dist[2])
    loc_dist[3] = "{:.2f}".format(loc_dist[3])
    loc_dist[4] = "{:.2f}".format(loc_dist[4])
        
    # Determine which point is closer and update Results label
    
    global result


    loclist = loc_dist[0:4]
    loclist.sort()
    closest = loclist[0]
    tloc = loc_dist.index(closest)
    tdesc = loc_dist[tloc+5]

    # Give result to User
    
    result.config(text = f"{desc} is closest to{tdesc}, which is {closest} kilometers away!")
    
        
# Magic Button

loc = tk.Button(window,text="Check Location", command = coords)

# Create modules

greeting = tk.Label(text= "Welcome to the GeoPoint Calc 3000!")
latcoord = tk.Label(text = "Please enter the latitude: ")
loncoord = tk.Label(text = "Please enter the longitude: ")
londesc = tk.Label(text = "Please enter the location's name: ")
lonfile = tk.Label(text = "Please enter the name of a file with location data: ")
result = tk.Label(text = result)
ent1 = tk.Entry(width = 20)
ent2 = tk.Entry(width = 20)
ent3 = tk.Entry(width = 20)
ent4 = tk.Entry(width = 20)

# Place modules

greeting.pack()
latcoord.pack()
ent1.pack()
loncoord.pack()
ent2.pack()
londesc.pack()
ent3.pack()
result.pack()
loc.pack(side = "top")

window.mainloop()

