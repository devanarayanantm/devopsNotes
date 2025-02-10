

# def fun(nums):
    # # num=int(input("enter a number: "))
    # for i in nums:
    #     print(i)

def check_prime(nums):
    for i in nums:
        if i<2:
            continue
        flag=1
        for j in range(2,i//2+1):
            if i%j==0:
                flag=0
                break
        if flag==1:
            print(i)




# fun([1,2,3,4,5])
arr=[1,2,3,4,8,9,1,11,25]
check_prime(arr)
    