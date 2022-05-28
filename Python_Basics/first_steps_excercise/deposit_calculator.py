deposit_amount = int(input())
deposit_period = int(input())
yearly_interest_rate = float(input())/100
total = deposit_amount + deposit_period * ((deposit_amount * yearly_interest_rate)/12)
print(total)