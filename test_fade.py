from udp_client import UdpClient 
import time

IP = '192.168.1.1'
PORT = 11600

udpClient = UdpClient(IP,PORT)

ONLINE = 1
OFFLINE = 0
DEFAULT_BRIGHT = 22

lights=udpClient.get_lights()
sns = []
for light in lights['led']:
    sns.append(light['sn'])
    print "found light: "+light['sn']

def send(r,g,b,bright=DEFAULT_BRIGHT):
    udpClient.set_light(bright,r,g,b,ONLINE,sns)

def main():
    #fadeloop()
    send(255,145,15)

def fadeloop():
    r=0
    g=0
    b=0
    colormax = 1
    step = 2.0/256
    delay = 0.01

    while r < colormax :
        send(int(r*255),int(g*255),int(b*255))
        r=r+step
        time.sleep(delay)
        
    while True:
        while g < colormax :
            send(int(r*255),int(g*255),int(b*255))
            r=r-step
            g=g+step
            time.sleep(delay)
        while b < colormax :
            send(int(r*255),int(g*255),int(b*255))
            g=g-step
            b=b+step
            time.sleep(delay)
        while r < colormax :
            send(int(r*255),int(g*255),int(b*255))
            b=b-step
            r=r+step
            time.sleep(delay)

if __name__ == "__main__":
    main()