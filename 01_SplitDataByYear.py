f = open("../dataset/rejected_2007_to_2018Q4.csv", "r")
fw2007 = open("../dataset/rejected_only_2007.csv","w")
fw2008up = open("../dataset/rejected_only_2008_up.csv","w")
counter = 0
for x in f:
    line = x.split(",")
    appDate = line[1].split("-")
    print(x)
    if counter == 0 :
        fw2007.write(x)
        fw2008up.write(x)
        counter=counter+1
        continue
    if appDate[0] == "2007" :
        fw2007.write(x)
    else :
        fw2008up.write(x)

    counter=counter+1
f.close()
fw2007.close()
fw2008up.close()
