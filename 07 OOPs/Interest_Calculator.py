#Assignment 3 Interest Calculator

class bank_interest_calculator():
    __interest_rate = 8.6
    __interest_rate_seniorCitizen = 8.4
    def __init__(self,principal1,Duration1,flag1):
        self.principal= principal1
        self.Duration = Duration1
        self.flagSenoirCitizen =flag1

    def simple_interest_calcultor(self):
        if self.flagSenoirCitizen:
            si = ((self.principal) * (self.Duration) * (bank_interest_calculator.__interest_rate_seniorCitizen))/100
            print(f'Simple Interest on principal amount of {self.principal} is {si}')
        else:
            si = ((self.principal) * (self.Duration) * (bank_interest_calculator.__interest_rate))/100
            print(f'Simple Interest on principal amount of {self.principal} is {si}')

customer1 = bank_interest_calculator(10000, 1 , False)
customer2 = bank_interest_calculator(10000, 1, True)
customer1.simple_interest_calcultor()
customer2.simple_interest_calcultor()