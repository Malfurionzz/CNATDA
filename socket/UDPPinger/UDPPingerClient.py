from socket import *
import time

ServerName='192.168.133.134'
serverPort = 12000
clientSocket= socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
RTTcount=[]
timeoutCount=0
for i in range(0,10):
    sendTime =time.time()
    message =('Ping %d %s' % (i+1,sendTime)).encode()
    try:
        clientSocket.sendto(message,(ServerName,serverPort))
        modifiedMessage,address=clientSocket.recvfrom(1024)
        rtt=time.time()-sendTime
        RTTcount.append(rtt)
        print 'Sequence %d from %s RTT=%.3f' % (i+1,ServerName,rtt)
    except Exception as e:
        print('Sequence %d: Request timed out' % (i+1))
        timeoutCount = timeoutCount + 1
RTTAve=0
for i in RTTcount:
    RTTAve+=i
RTTAve/(10-timeoutCount)
print 'RTTMax: %.3f\nRTTMin: %.3f\n RTTAve: %.3f TimeoutRate: %.3f' % (max(RTTcount),min(RTTcount),RTTAve,timeoutCount/10)
clientSocket.close()

