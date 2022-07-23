
from functionsUtil import get_risk_score


data = "8000.0,2007-07-02,\"I intend to use this loan to pay off a credit card and most of my overdraft protection, while reducing my monthly payments (if I get my target rate).\",727.0,47.63%,146xx,NY,4 years,0.0"

print(get_risk_score(data))
