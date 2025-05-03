num=int(input("enter your number"))
if num > 127:
    print("sorry please enter a value between 0 and 127")
else:
    print("the ascll value for your number is",{chr(num)})