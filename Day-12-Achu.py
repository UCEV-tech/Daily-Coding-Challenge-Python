def is_leap(year):
    leap = False
    
    if year % 4 == 0:  # Divisible by 4
        if year % 100 == 0:  # Divisible by 100
            if year % 400 == 0:  # Divisible by 400
                leap = True
        else:
            leap = True  # Not divisible by 100 but divisible by 4, so leap year
    
    return leap

year = int(input())
print(is_leap(year))
