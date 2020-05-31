import RPi.GPIO as IO #Library RPi.GPIO
import time           #Library Time
led0=27               #NET
led1=22               #SIG

IO.setmode(IO.BCM)     #Choose BCM
IO.setup(led0, IO.OUT)  
IO.setup(led1, IO.OUT)  
IO.setwarnings(False)

try:
    while (True):       
        IO.output(led0, 1)
        IO.output(led1, 1)
        time.sleep(1)
        IO.output(led0, 0)
        IO.output(led1, 0)
        time.sleep(1)
except KeyboardInterrupt:
    IO.cleanup()
    print('OK')
