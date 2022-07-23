from functionsUtil import get_risk_score

f = open("../dataset/rejected_only_2007.csv", "r")
fw = open("../dataset/rejected_2007_only_risk_score_ma50.csv","w")
counter = 0
moving_size = 50
moving_average = []
for x in f:
    x = x.rstrip()
    if counter == 0:
        fw.write(x + ",Risk Score MA50\r\n")
        counter=counter+1
        continue

    risk_score = get_risk_score(x)

    moving_average.append(risk_score)
    if counter < moving_size :
        fw.write(x + ",0\r\n")
    else :
        print("counter = " + str(counter))
        window = moving_average[counter - moving_size : counter]
        fw.write(x + "," + str(round(sum(window)/moving_size,2)) + "\r\n")
        print(window)
        print(sum(window)/moving_size)
        print("============")
    counter=counter+1

f.close()
fw.close()
