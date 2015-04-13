from qlib import *

MyQStation = QStation()

MyQStation.show()

m= MyQStation

for i in range(3):
  m.bulbs[i].switch(1,360)