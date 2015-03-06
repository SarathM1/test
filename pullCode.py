from subprocess import Popen as p
from subprocess import call as c
from time import sleep
com1c = 'git pull ssh3 master'

p1 = c(com1c.split())
#p1.wait()
print "-------------------------------"
#sleep(2)
#p2 = c(com2c.split())
#p2.wait()
