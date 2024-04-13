def postfix_interpreter():
    val_dict={}
    rerun=True
    while rerun==True:
        postfix=input("--> ")
        if postfix=="done()":
            rerun=False
        else:
            postfix_lst=postfix.split(" ")
            lst=[]
            operators="+-/*"
            assignment=False
            var=None
            for i in range(len(postfix_lst)):
                if postfix_lst[i]=="=":
                    var=postfix_lst[i-1]
                    assignment=True
            if assignment==True:
                for i in range(2):
                    postfix_lst.pop(0)
                variable=None
                index=None
                for key in val_dict:
                    for i in range(len(postfix_lst)):
                        if postfix_lst[i]==key:
                            index=key
                            variable=val_dict[key]
                if isinstance(variable,float):
                    for i in range(len(postfix_lst)):
                        if postfix_lst[i]==key:
                            postfix_lst[i]=str(variable)
                for elem in postfix_lst:
                    if elem not in operators:
                        lst.append(float(elem))
                    else:
                        arg2=lst.pop()
                        arg1=lst.pop()
                        if elem=="+":
                            res=arg1+arg2
                        elif elem=="-":
                            res=arg1-arg2
                        elif elem=="/":
                            if arg2==0:
                                raise ZeroDivisionError
                            else:
                                res=arg1/arg2
                        else:
                            res=arg1*arg2
                        lst.append(res)
                result=lst.pop()
                val_dict[var]=result
                print(var)
            else:
                variable=None
                index=None
                for key in val_dict:
                    for i in range(len(postfix_lst)):
                        if postfix_lst[i]==key:
                            index=key
                            variable=val_dict[key]
                if isinstance(variable,float):
                    for i in range(len(postfix_lst)):
                        if postfix_lst[i]==key:
                            postfix_lst[i]=str(variable)
                for elem in postfix_lst:
                    if elem not in operators:
                        lst.append(float(elem))
                    else:
                        arg2=lst.pop()
                        arg1=lst.pop()
                        if elem=="+":
                            res=arg1+arg2
                        elif elem=="-":
                            res=arg1-arg2
                        elif elem=="/":
                            if arg2==0:
                                raise ZeroDivisionError
                            else:
                                res=arg1/arg2
                        else:
                            res=arg1*arg2
                        lst.append(res)
                result=lst.pop()
                result_str=str(result)
                index=None
                condition=False
                for i in range(len(result_str)):
                    if result_str[i]==".":
                        index=i
                if result_str[index+1]=="0":
                    condition=True
                if condition==True:
                    print(int(result))
                else:
                    print(result)
postfix_interpreter()
                
                
                    
