from kafka import KafkaProducer
from kafka.errors import KafkaError
import subprocess as sub

### - START

INTERFACE_NAME = '' # INPUT NETWORK INTERFCAE THAT YOU WISH TO MONITOR
IP_ADDRESS = '' # INPUT SOURCE NETWORK IP ADDRESS

# Connect kafka producer here
producer = KafkaProducer(bootstrap_servers=['']) # INPUT KAFKA BOOTSTRAP_SERVERS HERE

### - END
topicName = 'cstl'

# Network interface to be monoitored
# define a function to output perf output

def transmit_kafka():
    p = sub.Popen(('tcpdump','-i',INTERFACE_NAME,'-l'), stdout=sub.PIPE)

    for line in iter(p.stdout.readline, b''):
        content = str(line)
        if (content.find(IP_ADDRESS)) != -1 and content.find('ICMP') != -1 :
            print(content)
            producer.send(topicName, content)

        # producer.send(topicName, content)

        # INPUT YOUR CODE HERE - END

# transmit_kafka()

transmit_kafka()
