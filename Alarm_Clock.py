import time
import RPi.GPIO as GPIO
import os
import lcddriver

lcd = lcddriver.lcd()
GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP)     #right, speaker switch
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #left, LED/Buzz switch
buzzer_pin = 17                                     
GPIO.setup(buzzer_pin, GPIO.OUT)                    #buzzer
GPIO.setup(18, GPIO.OUT)                            #LED


def takeTime():
    lst = []
    m = 'am'
    isPM = False
    x = int(time.strftime("%H"))
    y = int(time.strftime("%M"))
    z = int(time.strftime("%S"))
    if x > 12:
        isPM = True
        x -= 12
    if(isPM):
        m = 'pm'
    lst.append(x)
    lst.append(y)
    lst.append(z)
    lst.append(m)
    return lst

def convertTime(hour, minute, second):
    return (hour*3600) + (minute*60) + second

def waitTime(seconds):
    while(seconds > 0):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        #print("Time until the alarm goes off: {:02d}:{:02d}:{:02d}".format(h,m,s))
        lcd.lcd_display_string("{:02d}:{:02d}:{:02d}".format(h,m,s),1)
        seconds -= 1
        time.sleep(1)

def buzz(pitch, duration):
    print("WAKE UP")
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(buzzer_pin, True)
        GPIO.output(buzzer_pin, False)

a = takeTime()
print('The current time is {:02d}:{:02d}:{:02d} {}'.format(a[0],a[1],a[2],a[3]))
t = raw_input ('Enter the time you want the alarm clock to go off (hh:mm(a/p)) : ')
h = int(t[:2])
if (h > 12):
    raise ValueError('You can\'t have more than 12 hours!')
m = int(t[3:-1])
a = takeTime()
x = convertTime(h,m,0)
y = convertTime(a[0], a[1], a[2])

if (t[-1].lower() == a[-1][0].lower()):
    if x > y:
        z = x-y
    else:
        z = -1*(x-y) + 86400
elif ((t[-1].lower() != a[-1][0].lower()) and (t[-1].lower() == 'a' or t[-1].lower() == 'p')):
    z = x-y + 43200
else:
    raise ValueError('Not a valid time, for x type a(am) or p(pm)')
waitTime(z)
   
while True:
    GPIO.output(17, True)
    GPIO.output(18, True)
    buzz(1000, 1)
    lcd.lcd_display_string("WAKE UP!!!", 1)

    if(GPIO.input(27) == False):
        time.sleep(0.05)
        GPIO.output(17, False)
        GPIO.output(18, False)
        break
os.system('clear')
print("Press button 2 for time/date/weather")
while True:
    if(GPIO.input(4) == False):
        time.sleep(0.5)
        os.system("date '+%I:%M %P' | flite")
        os.system('weather -q fips1703114000 | flite')
        break


