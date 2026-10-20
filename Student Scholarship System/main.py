name = input('Enter your name please(First and last):')
first_name = name.split()[0]
age = int(input('Enter your age please:'))
grade = float(input('Enter your grade please(0-100):'))
certificate = input('Have you certificate?(yes-no):').lower()
penalty = input('Have you penalty?(yes-no):').lower()
family_income = float(input('Enter your family income please: $'))
if age < 0:
    print('Invalid age')
elif grade < 0 or grade > 100:
    print('Invalid grade')
elif family_income < 0:
    print('Invalid family income')
elif certificate not in ('yes', 'no'):
    print('Invalid certificate answer')
elif penalty not in ('yes', 'no'):
    print('Invalid penalty answer')
else:
    if 25 >= age >= 18 and grade >= 90 and family_income <= 10000 and penalty == 'no':
        print(f'Congratulations {first_name}!\nYou have a full Scholarship')
    elif 25 >= age >= 18 and penalty == 'no' and (grade >= 80 or family_income <= 6000 or certificate == 'yes' ):
        print(f'Congratulations {first_name}!\nYou have a part Scholarship')
    else:
        print('Unfortunately, you are not eligible for a scholarship')
        if age < 18 or age > 25:
            print('Reason: Age is outside the required range')
        if grade < 80:
            print('Reason: Grade is less than 80')
        if penalty == 'yes':
            print('Reason: You have a university penalty')
