largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        value=int(num)
        valid=1
    except:
        valid=0
        #continue
    if valid==1:
        if smallest==None:
            smallest=value
            if largest==None:
            smallest=value
        elif value>largest:
            largest=value
    else:
        print('Invalid input, please correct it')
print('Maximum is',largest)
print('Minimum is',smallest)
