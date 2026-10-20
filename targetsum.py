print("HELLO!!"+"\n Welcome to this game "+"\n Type stop to get back to the last page:")
while True :
    ask=input("Write 'start' to play and 'stop' to end the game ; ")
    if ask.lower().strip()=='start':
        while True:
            nums=input("Write the list of numbers with space in between : ")
            if nums.lower().strip()=='stop':
                    break
            else:
                target=int(input("Enter the sum you want : "))
                string_lst=nums.split()
                nums_lst=list()
                nums_lst.sort()
                answer_dic=dict()
                try:
                    for num in string_lst:
                        num=int(num)
                        nums_lst.append(num)
                except:
                    print("please type numbers only")    
                    break  
                for i in range(len(nums_lst)):
                    need=target - nums_lst[i]
                    if need in nums_lst:
                        answer_dic[(i,nums_lst.index(need))]=(nums_lst[i],need )   
                    else:
                        continue
                print(answer_dic)    
    elif ask.lower().strip()=='stop':
        print("Thankyou for playing")   
        break  