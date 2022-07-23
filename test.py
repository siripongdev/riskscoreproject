
#from functionsUtil import get_risk_score
#data = "8000.0,2007-07-02,\"I intend to use this loan to pay off a credit card and most of my overdraft protection, while reducing my monthly payments (if I get my target rate).\",727.0,47.63%,146xx,NY,4 years,0.0"
#print(get_risk_score(data))

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


values = [9, 5, 10, 16, 5]
period = 5

result = movingAverageExponential(values,0.5,0)
print(result)
print(result[len(result)-1])
