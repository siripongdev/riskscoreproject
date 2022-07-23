from kafka import KafkaProducer
from kafka.errors import KafkaError

import time

f = open("../dataset/rejected_only_2008_up.csv", "r")
toggle = True
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

counter = 0

for x in f:
    x = x.rstrip()
    if toggle == True:
        toggle =False
        continue

    #producer.send('numtest', value=data)
    future = producer.send('riskscore2', bytes(x,'utf-8'))
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass

    # Successful result returns assigned partition and offset
    print(x)
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)
    time.sleep(0.5)
    counter = counter+1
    #if counter > 10 :
    #    break
    #break;
