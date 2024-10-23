def formatter(eqns):
    
    for eqn in eqns:
        if len(eqn.split())>3:
            print("Only two numbers can be used!")
            return "Only two numbers can be used!"
        first,sign,last=eqn.split()
        print(first)
formatter(["45 + 9", "30 + 50", "39 - 10"])
