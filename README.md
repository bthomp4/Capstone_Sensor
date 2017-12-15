# Capstone_Sensor

## Acronyms
- **SS**: Side sensor
- **US**: Ultrasonic sensor
- **FS**: Front sensor

## Project Goal
The goal of this project is to recieve inputs from the ultrasonic sensors, and eventually the front sensor.

## Project Tasks
~1. Test the output and input voltages from the Arduino Nano connected to the SS~
   ~- This voltage should be 5 volts~
~2. Test the output and input voltages from the Arduino Nano connected to the SS through the voltage divider~
   ~- This is to make sure the voltage divider can safely divide the 5 V down to the 3.3 V that the Raspberry Pi uses~
   ~- This set can be skipped the input / output voltage is found to be 3.3 V~
3. Create a program to get a distance measurement from the SS
   - This program may be in C or Python
   - This program can display the information on the terminal or as a text file
   - This program does **_NOT_** need to work with the Camera program
4. Create a program that lights up LEDs based on the distance recorded from the SS
   - This program does **_NOT_** need to work with the Camera program
5. Join the Camera program and the Sensor program
   - This step does not need to be done until after the Fall demo
   - Hopefully by this step the FS will be in and can be interfaced with the Sensor program befor merging with the Camera program

## Additional Info
- The Arduino code was sourced from <https://www.dfrobot.com/wiki/index.php/Weather-proof_Ultrasonic_Sensor_SKU_:_SEN0207>
- This website has great information on how the ultrasonic sensor works
- To program the Arduino you will need the [Arduino IDE](https://www.arduino.cc/en/Main/Software#download)
- Another good source I have found is <https://www.raspberrypi-spy.co.uk/2016/10/waterproof-ultrasonic-distance-measuring-module/>
    - The Python scripts come from the above website

