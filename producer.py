# There is only 1 section that has to be edited in this code
# The codes that needs to be edited are designated with :
# ### - START
# 
# ### - END
#
# You will also need to uncomment the last line (producer.send(topicName, content)) of def transmit_kafka()


from kafka import KafkaProducer
from kafka.errors import KafkaError
import subprocess as sub

### - START

INTERFACE_NAME = '' # input network interface name that you wish to monitor
BOOTSTRAP_SERVERS = [''] # input kafka broker servers

### - END

# Connect kafka producer here

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
topicName = 'cstl'

# Network interface to be monoitored

def transmit_kafka():
    p = sub.Popen(('tcpdump','-i',INTERFACE_NAME,'-l'), stdout=sub.PIPE)

    for line in iter(p.stdout.readline, b''):
        content = str(line) # output of tcpdump of a network interface is saved in content
        print(content) # this will print contents

        ### - START

        # Insert code here that will filter all the other messages.
        # You need to transmit only ICMP packets via Kafka
        # You also need to print only ICMP packets via Kafka
        # ICMP packet will look like below :
        # 11:02:15.612968 IP 111.111.111.111 > 222.222.222.222 : ICMP echo request, id 7725, seq 1, length 64
        # 11:02:16.612990 IP 222.222.222.222 > 111.111.111.111 : ICMP echo reply, id 7725, seq 1, length64

        ### - END

        # IF YOU UNCOMMENT THE LINE BELOW, IT WILL SEND the variable contents TO KAFKA
        # producer.send(topicName, content) 

transmit_kafka()
