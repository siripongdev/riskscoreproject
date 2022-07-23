def get_risk_score(data):
    line = data.split(",")
    #print("x = " + data)

    #some data has "," between " " that will make split wrong data
    if line[2].find("\"") > -1 :
        idx = data.index("\"")
        data2 = data[idx+1:len(data)]
        idx = data2.index("\"")
        data3 = data2[idx+1:len(data2)]
        line = data3.split(",")
        risk = line[1]

        #if line[1] == "":
        #    risk_score = 0
        #else :
        #    risk_score = float(line[1])
    else :
        #print("line = " + line[3])
        risk = line[3]
        #if line[3] == "" :
        #    risk_score = 0
        #else :
        #    risk_score = float(line[3])
    if risk == "" :
        risk_score = 0
    else:
        risk_score = float(risk)

    print("riskscore = " + str(risk_score))
    return risk_score

def movingAverageExponential(values, alpha, epsilon = 0):

   if not 0 < alpha < 1:
      raise ValueError("out of range, alpha='%s'" % alpha)

   if not 0 <= epsilon < alpha:
      raise ValueError("out of range, epsilon='%s'" % epsilon)

   result = [None] * len(values)

   for i in range(len(result)):
       currentWeight = 1.0

       numerator     = 0
       denominator   = 0
       for value in values[i::-1]:
           numerator     += value * currentWeight
           denominator   += currentWeight

           currentWeight *= alpha
           if currentWeight < epsilon:
              break

       result[i] = numerator / denominator

   return result
