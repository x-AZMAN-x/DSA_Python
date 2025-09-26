eligibility = int(input("What Is The Percentage Of The Student's Eligibility? "))
if eligibility >= 100:
    print(f"Invalid Input! Please Enter A Number From 0 To 100")
else:
    if eligibility >= 50:
        print(f"This Student Is Not Eligible To Give The Exams.")
    else:
        print("This Student Is Eligible To Give The Exams.")