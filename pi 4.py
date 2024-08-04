import RPi.GPIO as GPIO
from time import sleep

tones = {
    "B0": 31, "C1": 33, "CS1": 35, "D1": 37, "DS1": 39, "E1": 41, "F1": 44,
    "FS1": 46, "G1": 49, "GS1": 52, "A1": 55, "AS1": 58, "B1": 62, "C2": 65,
    "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93, "G2": 98,
    "GS2": 104, "A2": 110, "AS2": 117, "B2": 123, "C3": 131, "CS3": 139,
    "D3": 147, "DS3": 156, "E3": 165, "F3": 175, "FS3": 185, "G3": 196,
    "GS3": 208, "A3": 220, "AS3": 233, "B3": 247, "C4": 262, "CS4": 277,
    "D4": 294, "DS4": 311, "E4": 330, "F4": 349, "FS4": 370, "G4": 392,
    "GS4": 415, "A4": 440, "AS4": 466, "B4": 494, "C5": 523, "CS5": 554,
    "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740, "G5": 784,
    "GS5": 831, "A5": 880, "AS5": 932, "B5": 988, "C6": 1047, "CS6": 1109,
    "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397, "FS6": 1480, "G6": 1568,
    "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976, "C7": 2093, "CS7": 2217,
    "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960, "G7": 3136,
    "GS7": 3322, "A7": 3520, "AS7": 3729, "B7": 3951, "C8": 4186, "CS8": 4435,
    "D8": 4699, "DS8": 4978
}

song = ["B3", "G4", "FS4", "D4", "B3", "G4", "FS4", "B3", "FS5", "E5", "B4", "E5", 
        "G5", "A5", "E5", "G5", "FS5", "G5", "A5", "D5", "B5", "C6", "B5", "A5", 
        "FS5", "E5", "B4", "E5", "G5", "A5", "E5", "G5", "FS5", "G5", "A5", "D5", "E5"]
time = [0.5447, 0.5452, 1.0918, 2.1820, 0.5447, 0.5452, 1.0918, 1.6368, 0.2707, 0.2735, 
        2.7264, 0.5460, 0.5450, 1.0901, 3.2735, 2.1818, 0.5459, 0.5455, 0.5454, 0.5448, 
        1.9101, 0.1341, 0.1375, 2.1844, 0.2697, 0.2735, 2.7251, 0.5475, 0.5450, 1.0906, 
        3.2732, 2.1826, 0.5452, 0.5456, 0.5460, 0.5433, 7.0899]

buzzer_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
buzzer = GPIO.PWM(buzzer_pin, 1000)

def playtone(frequency):
    buzzer.ChangeFrequency(frequency)
    buzzer.start(50)  

def bequiet():
    buzzer.stop()

def playsong(mysong, time):
    for i in range(len(mysong)):
        if mysong[i] == "P":
            bequiet()
        else:
            print(mysong[i])
            playtone(tones[mysong[i]])
        sleep(time[i])
    bequiet()

print(len(song) - len(time))
playsong(song, time)

GPIO.cleanup()
