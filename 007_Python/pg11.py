def first_repeating_num(nums):
    flag={}
    for i in nums:
        if flag.get(i)==1:
            print(i)
            return
        else:
            flag[i]=1




arr=[1,2,7,7,3,4,5,6,1,4,7]
first_repeating_num(arr)