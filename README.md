# finalprojectv2
EE 250 final project by Alyssa Margalit and Frida Hill

DEMO: https://drive.google.com/drive/folders/1hl32uvdiJSrgYbnVNL2KqFM5obeEvoxr?usp=sharing

libraries used:
vm: requests, socket, json, random, paho.mqtt.client, time, sys, math, matplotlib.pyplot
rpi: sys, grovepi, math, mqtt, RPi.GPIO, time
  
How it works:
  Run vm.py on your vm and run pi3.py on your rpi
  
  Spin the potentiometer in any direction to "wake" the dragon
  
  The dragon will ask you who you are
  
    the options are wizard, hero, villain or peasant in order
    
  Respond by turning the potentiometer to the desired value
  
  click button to lock in potentiometer response
  
  The lcd will then ask if you've come for the treasure
  
  Turn the potentiometer and click the button to respond (higher potentiometer value is yes, lower is no)
  
  The dragon will then ask you a trivia question depending on your previous response. 
  
  Respond by turning the potentiometer to a higher value for true and a lower value for no and then click the button to lock in the response.
  
  
  There are three different story paths:
  
    1. you have come for the treasure and you answer the trivia question correctly in which case you get the "treasure"
    
    2. you have come for the treasure and you answer the trivia question incorrectly in which case you are "cursed"
    
    3. you have not come for the treasure in which case you are "banished"
    
    
 3D printed portions:

  stl files designed by me:
  
    sensor cases: https://www.thingiverse.com/thing:4650334
    gothic ruins facade: https://www.thingiverse.com/thing:4650352
  
  other stl files:
  
    tree: https://www.thingiverse.com/thing:3958719
    
    dragon: https://www.thingiverse.com/thing:87458
    
    sword: https://www.thingiverse.com/thing:2047413
    
    
 
