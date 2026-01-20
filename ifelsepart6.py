salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    loan=int(input("Loan:"))
    if(loan>5000):
        print("maximum loan amount is 50000")
    else:       
        print("you are elgible for loan")
else:
    print("you are not eligible")
