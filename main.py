import tkinter
import phonenumbers
import folium.map
import opencage

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone as tz

from tkinter import*
from tkinter import messagebox
from opencage.geocoder import OpenCageGeocode

root=tkinter.Tk()
root.geometry("350x350")

Label=Label(text="Phone Numbers Tracker")
Label.pack()
def getresult():
    num=number.get("1.0",END)
    num1=phonenumbers.parse(num)

    location=geocoder.description_for_number(num1,"en")
    service_provider=carrier.name_for_number(num1,"en")

    timezone=tz.time_zones_for_number(numobj=num1)

    ocg=OpenCageGeocode(ApiKey)
    query=str(location)
    results=ocg.geocode(query)

    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']

    my_label=LabelFrame(root)
    my_label.pack()

    result.insert(END,"the country of this number is:"+location)
    result.insert(END,"\nthe sim card of this number is:"+service_provider)

    result.insert(END,"\nlatitude is:"+str(lat))
    result.insert(END,"\nlongitude is:"+str(lng))

    result.insert(END,"\nthe continent timezone:"+str(timezone))

    Map_location=folium.Map(location=[lat,lng],zoom_start=10)
    folium.Marker([lat,lng],popup=location).add_to(Map_location)
    Map_location.save("mylocation.html")


number=Text(height=1)
number.pack()

Button=Button(text="BUTTON",command=getresult)
Button.pack(pady=10,padx=100)

result=Text(height=7)
result.pack()
root.mainloop()

