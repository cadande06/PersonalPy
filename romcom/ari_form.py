def formatter(eqns):
    answer=''
    result=''
    first_line=''
    second_line=''
    third_line=''
    last_line=''
    for eqn in eqns:
        if len(eqn.split())>3:
            print("Only two numbers can be used!")
            return "Only two numbers can be used!"
        first,sign,last=eqn.split()
        
        max_width=max(len(first),len(last))+2
        if sign not in ['+', '-', '*', '/', '%']:
            print("Only addition and Subtraction allowed")
            return "Only addition and Subtraction allowed"
        if not first.isdigit() and last.isdigit():
            print("Only digits allowed")
            return "Only digits allowed"
        if sign=='+':
            answer=str(int(first)+int(last))
            
            first_line+=first.rjust(max_width)+'    '
            second_line+='+ '+last.rjust(max_width-2)+'    '
            third_line+='-'*max_width+'    '
            last_line+=answer.rjust(max_width)+'    '
        elif sign=='-':
            answer=str(int(first)-int(last))
            #print(answer)
            first_line+=first.rjust(max_width)+'    '
            second_line+='- '+last.rjust(max_width-2)+'    '
            third_line+='-'*max_width+'    '
            last_line+=answer.rjust(max_width)+'    '
        elif sign=='*':
            answer=str(int(first)*int(last))
            #print(answer)
            first_line+=first.rjust(max_width)+'    '
            second_line+='* '+last.rjust(max_width-2)+'    '
            third_line+='-'*max_width+'    '
            last_line+=answer.rjust(max_width)+'    '
        elif sign=='/':
            answer=str(int(first)/int(last))
            #print(answer)
            first_line+=first.rjust(max_width)+'    '
            second_line+='/ '+last.rjust(max_width-2)+'    '
            third_line+='-'*max_width+'    '
            last_line+=answer.rjust(max_width)+'    '
        elif sign=='%':
            answer=str(int(first)%int(last))
            #print(answer)
            first_line+=first.rjust(max_width)+'    '
            second_line+='% '+last.rjust(max_width-2)+'    '
            third_line+='-'*max_width+'    '
            last_line+=answer.rjust(max_width)+'    '
        result=first_line.rstrip()+'\n'+second_line.rstrip()+'\n'+third_line.rstrip()+'\n'+last_line.rstrip()
    print(result)
    return result        
        
        
formatter(["45 % 9", "30 * 2050", "39 - 10", "45 / 10", "72 + 144"])
