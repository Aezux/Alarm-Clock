# Description
The goal of this project is create a functioning alarm clock. It is designed so the user can enter the time that they want the buzzer to go off, and when it reaches the desired time, the only way that they can stop the buzzing would be to press a button. In addition, a feature that the user can make use of is being read the current weather report, time of day, and date all by pressing another button.

# Hardware needed

- (1)  Raspberry Pi 
- (1)  Speaker with 3.5 mm jack 
- (1)  Breadboard
- (2)  Button Switch 
- (1)  i2c 
- (1)  Lcd Screen 
- (1)  Led Light  
- (1)  470 Ohms resistor for LED light 
- (1)  Piezo Buzzer 
- (1)  4.7K Ohms resistor for Buzzer 
- (1)  1K Ohms resistor for Right Switch (connects to speaker) 
- (1)  10K Ohms resistor also for Right Switch
- (15) M - F Wires 
- (11) M - M Wires 

# Software needed
1. The **Alarm_Clock.py** file
2. **LCD software:**
`type below in terminal`
> wget http://reed.cs.depaul.edu/lperkovic/csc299/lab5/i2c_lib.py

> wget http://reed.cs.depaul.edu/lperkovic/csc299/lab5/lcddriver.py
3. **Flite text to speak software:**
`type below in terminal`
> sudo apt-get install flite
4. **Weather checking software:**
`type below in terminal`
> git clone http://www.yuggoth.org/git/weather.git
