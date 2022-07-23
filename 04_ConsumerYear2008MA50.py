from kafka import KafkaConsumer
from datetime import *
from functionsUtil import get_risk_score

counter = 0
moving_size50 = 50
moving_size100 = 100
moving_average = []

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('riskscore2',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

    x = message.value.decode("utf-8")
    data = x.split(",")
    #get risk score
    risk_score = get_risk_score(x)

    fw = open("../dataset/rejected_2008_up_riskscore.csv","a")
    moving_average.append(risk_score)
    #data is less than moving average size (50), do not calculate yet
    if counter < moving_size50 :
        fw.write(x + ",0\r\n")
    else :
        try:
            print(counter)

            #get 50 data point from array
            window = moving_average[counter - moving_size50 : counter]

            ma100 = ""
            d = data[1].split("-")
            data_date = date(int(d[0]),int(d[1]),int(d[2]))
            #if data come from 2009 onward, will change to MA(100)
            #if use the same previous  column (MA50), will make people confuse,
            #add new column called MA100 is better
            if data_date > date(2008, 12, 31) :
                if counter < moving_size100 :
                    ma100 = ",0"
                else :
                    window100 = moving_average[counter - moving_size100 : counter]
                    ma100 = "," + str(round(sum(window100)/moving_size100,2))

            fw.write(x + "," + str(round(sum(window)/moving_size50,2)) + ma100 + "\r\n")
            print(window)
            print(sum(window)/moving_size50)
            print("============")

            fw.close()

        except:
            error_log = open("../dataset/errorlog.csv","a")
            error_log.write("data error => " + x)
            error_log.close()

        counter=counter+1
