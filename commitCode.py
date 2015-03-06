from subprocess import Popen as p
from subprocess import call as c
from time import sleep
com1p = 'git status'
com2c = 'git add --all'
com3c = 'git commit -m "Done"'
com4c = 'git push ssh3'

p1 = p(com1p.split())
p1.wait()
print "-------------------------------"
sleep(2)
p2 = c(com2c.split())
#p2.wait()
print "-------------------------------"
sleep(2)
p3 = c(com3c.split())
#p3.wait()
print "-------------------------------"
sleep(2)
p4 = c(com4c.split())
