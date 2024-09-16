country = {'Afghanistan': 'Kabul','Australia': 'Canberra','Bangladesh': 'Dhaka','Belgium': 'Brussels','Brazil': 'Brasilia','Canada': 'Ottawa','China': 'Beijing','France':'Paris','India':'New Delhi','Japan':'Tokyo','Nepal':'Kathmandu','Pakistan':'Islamabad'}
countries = set(country.keys())
score = 0
attempts = 0
for i in countries:
    choice = input(f"What is the capital of {i} ? ")
    attempts +=1
    if country[i].lower() == choice.lower():
        score+=1
        print(f"{choice} is Correct Answer")
    else :
        print(f"Your answer {choice} is wrong \n correct answer is {country[i]}")
    ans= input("Do you want to play more \n yes or no")
    if ans != 'yes':
        break
print(f"Your Score is {score}, and your attempt count is {attempts}")


