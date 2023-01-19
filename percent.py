def price():
    print(' price - first amount \n percent - fixed interest per year(from 0 to 1) \n month - contribution amount per year \n year - years amount \n')
    price = int(input('Enter price: '))
    percent = float(input('Enter percent: '))
    month = int(input('Enter month: '))
    year = int(input('Enter year: '))
    
    Sum = price * ( ( 1 + percent / month ) ** (month * year) )
    print('Your sum after', year , 'years will be:',"%.3f" % Sum)   
