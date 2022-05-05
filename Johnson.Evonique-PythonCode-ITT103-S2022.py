sales = input('')
sales_class = input('')

if sales_class == 1:
    if sales <= 1000:
        print(0.06 * sales)
    elif 1000 < sales <= 2000:
        print(0.07 * sales)
    else:
        print(0.1 * sales)
elif sales_class == 2:
    if sales <= 1000:
        print(0.04 * sales)
    else:
        print(0.06 * sales)
elif sales_class == 3:
    print(0.045 * sales)
else:
    print("No rate is added")



