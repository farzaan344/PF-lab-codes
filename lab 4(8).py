print("Farzaan Bin Khawar\n2023F-BIT-030")
years_of_service = int(input("Enter years of service: "))
qualification = input("Enter qualification (Masters/Bachelors): ")

salary_masters_10_years = 150000
salary_bachelors_10_years = 100000
salary_masters_lessthan_10_years = 100000
salary_bachelors_lessthan_10_years = 70000

if years_of_service >= 10 and qualification == "Masters":
    salary = salary_masters_10_years
elif years_of_service >= 10 and qualification == "Bachelors":
    salary = salary_bachelors_10_years
elif years_of_service < 10 and qualification == "Masters":
    salary = salary_masters_lessthan_10_years
elif years_of_service < 10 and qualification == "Bachelors":
    salary = salary_bachelors_lessthan_10_years
else:
    print("wrong input")
    salary=None
if salary is not None:
    print("the calculated salary is:",salary)

    
