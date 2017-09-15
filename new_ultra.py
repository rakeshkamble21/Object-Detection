import RPi.GPIO as GPIO     
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    
TRIG = 12
ECHO = 26
led = 22
buzz=17
GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)                   
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzz,GPIO.OUT)
time.sleep(5)
count=0
while True:
 i=0
 avgDistance=0
 for i in range(5):
  GPIO.output(TRIG, False)                 
  time.sleep(0.1)                                  
  GPIO.output(TRIG, True)                  
  time.sleep(0.00001)                           
  GPIO.output(TRIG, False)                 
  while GPIO.input(ECHO)==0:             
       GPIO.output(led, True)             
  pulse_start = time.time()
  while GPIO.input(ECHO)==1:              
       GPIO.output(led, True)
      
  pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start 
  distance = pulse_duration * 17150        
  distance = round(distance,2)                 
  avgDistance=avgDistance+distance
 avgDistance=avgDistance/5
 print (avgDistance)
 flag=0
 if avgDistance < 100:      
    count=count+1
    print ("Object is detected")
    print(count);
    
    GPIO.output(22,0)
    GPIO.output(17,0)
    time.sleep(1)
    
 else:
    print ("All clear")
    GPIO.output(22,1)
    GPIO.output(buzz,1)
    flag=0
    
