size=input("Enter the size of the pizza:")
bill=0
if size=='S' or size=='s':
    bill+=100
    print('small size pizza price is 100 Rs .')
elif size=='M' or size=='m':
    bill+=200
    print('Medium size pizza price is 200 Rs .')
elif size=='L' or size=='l':
    bill+=300
    print('Large size pizza price is 300 Rs .')
else:
    print('Enter valid pizza size')
    
add_pepporoni=input('Do you want to add pepporoni?(y/n) :')
if add_pepporoni=='y' or add_pepporoni=='Y':
    if size=='s' or size=='S':
        bill+=30
    else:
        bill+=50

extra_cheese=input('Do you want to add extra cheese?(y/n) :')
if extra_cheese=='y' or extra_cheese=='Y':
    bill+=20
print(f'Total final bill is {bill} .')
    