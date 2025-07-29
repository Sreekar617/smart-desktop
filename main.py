import os  # Used for path stuff actually
import ctypes  # ctypes is used specifically to change the wallpaper
import requests  # Used to get time and weather
import json


weather_url = "https://api.open-meteo.com/v1/forecast?latitude=45&longitude=-93&current=temperature_2m,precipitation,cloud_cover&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch" # approx coordinates for Minneapolis off the brainstem
time_url = "https://timeapi.io/api/time/current/zone?timeZone=America%2FChicago"

def get_info():
    global weather
    global current_time
    response = requests.get(weather_url)
    weather = response.json()
    weather = weather['current']
    print(weather)

    response = requests.get(time_url)
    current_time = response.json()
    print(current_time)
    # print(f"the hour is {current_time["hour"]}")

get_info()

### Constants ###
imagePath = r"C:\Users\Ramisetty\Pictures\smartwallpapers\main.jpg" 
dayFolder = r"C:\Users\Ramisetty\Pictures\smartwallpapers\Day"
nightFolder = r"C:\Users\Ramisetty\Pictures\smartwallpapers\Night"
morningFolder = r"C:\Users\Ramisetty\Pictures\smartwallpapers\Morning"
eveningFolder = r"C:\Users\Ramisetty\Pictures\smartwallpapers\Evening"
rainFolder = r"C:\Users\Ramisetty\Pictures\smartwallpapers\Rain"
SPI_SETDESKWALLPAPER = 20  # Tells Windows API to perform action 20: set desktop wallpaper

def setWallpaper(imagePath):
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.path.abspath(imagePath).encode(), 0)



hour = current_time['hour']
if weather['precipitation'] > 0.05: # arbitrary based on current precipitation (storm is basically over), increase to 0.1 later?
    print("rain")
    image_files = [f for f in os.listdir(rainFolder) if f.lower().endswith(('.jpg', '.jpeg'))]

    with open (os.path.join(rainFolder, random.choice(image_files)), 'rb') as src_file:
        image_bytes = src_file.read()

    with open(imagePath, 'wb') as dst_file:
        dst_file.write(image_bytes)

elif hour >= 19 or hour <= 6:
    print("night")
    image_files = [f for f in os.listdir(nightFolder) if f.lower().endswith(('.jpg', '.jpeg'))] # kaoruhana reference? 

    with open (os.path.join(nightFolder, random.choice(image_files)), 'rb') as src_file:
        image_bytes = src_file.read()

    with open(imagePath, 'wb') as dst_file:
        dst_file.write(image_bytes)


elif hour >= 7 and hour <= 10:
    print("morning")
    image_files = [f for f in os.listdir(morningFolder) if f.lower().endswith(('.jpg', '.jpeg'))]

    with open (os.path.join(morningFolder, random.choice(image_files)), 'rb') as src_file:
        image_bytes = src_file.read()

    with open(imagePath, 'wb') as dst_file:
        dst_file.write(image_bytes)


elif hour >= 11 and hour <= 16:
    print("afternoon")
    image_files = [f for f in os.listdir(dayFolder) if f.lower().endswith(('.jpg', '.jpeg'))]

    with open (os.path.join(dayFolder, random.choice(image_files)), 'rb') as src_file:
        image_bytes = src_file.read()

    with open(imagePath, 'wb') as dst_file:
        dst_file.write(image_bytes)


elif hour >= 17 and hour <= 18:
    print("evening")
    image_files = [f for f in os.listdir(eveningFolder) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    with open (os.path.join(eveningFolder, random.choice(image_files)), 'rb') as src_file:
        image_bytes = src_file.read()

    with open(imagePath, 'wb') as dst_file:
        dst_file.write(image_bytes)




setWallpaper(imagePath)