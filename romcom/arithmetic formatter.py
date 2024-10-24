def formatter(eqns):
    answer=''
    for eqn in eqns:
        if len(eqn.split())>3:
            print("Only two numbers can be used!")
            return "Only two numbers can be used!"
        first,sign,last=eqn.split()
        if sign not in ['+', '-']:
            print("Only addition and Subtraction allowed")
            return "Only addition and Subtraction allowed"
        if sign=='+':
            answer=str(int(first)+int(last))
            print(answer)
        elif sign=='-':
        
            answer=str(int(first)-int(last))
            print(answer)
formatter(["45 + 9", "30 - 50", "39 - 10"])
