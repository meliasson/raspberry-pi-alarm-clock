from datetime import datetime
import os
import pygame
import requests
import RPi.GPIO as GPIO
import subprocess
import time

def init_motion_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)

def init_signal():
    pygame.mixer.init()
    pygame.mixer.music.load("seagulls-and-waves.mp3")
    pygame.mixer.music.play()

def speak_greeting():
    subprocess.call(f"echo \"Good morning master of disaster ninja eagle!\" | festival --tts", shell=True)

def speak_quote():
    subprocess.call(f"echo \"Today's inspirational quote.\" | festival --tts", shell=True)
    response = requests.get("http://quotes.rest/qod.json?category=inspire")
    quote = response.json()["contents"]["quotes"][0]["quote"]
    subprocess.call(f"echo \"{quote}\" | festival --tts", shell=True)

def speak_weather():
    subprocess.call(f"echo \"Today's weather.\" | festival --tts", shell=True)
    city = 2670781
    key = os.environ['OPENWEATHERMAP_API_KEY']
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city}&appid={key}&units=metric")
    temperature = round(response.json()["main"]["temp"], 1)
    subprocess.call(f"echo \"Temperature is {temperature}.\" | festival --tts", shell=True)
    wind = response.json()["wind"]["speed"]
    subprocess.call(f"echo \"Wind is {wind}.\" | festival --tts", shell=True)
    sunrise = datetime.fromtimestamp(response.json()["sys"]["sunrise"]).strftime('%H:%M')
    subprocess.call(f"echo \"Sunrise at {sunrise}.\" | festival --tts", shell=True)
    sunset = datetime.fromtimestamp(response.json()["sys"]["sunset"]).strftime('%H:%M')
    subprocess.call(f"echo \"Sunset at {sunset}.\" | festival --tts", shell=True)

def motion_registered():
    return GPIO.input(4) == 1

def signal_finished():
    return pygame.mixer.music.get_busy() == False

def speak():
    pygame.mixer.music.fadeout(4)
    speak_greeting()
    speak_weather()
    speak_quote()
    
def start():
    while not motion_registered() and not signal_finished():
        pass
    speak()
    
init_motion_sensor()
init_signal()
start()
