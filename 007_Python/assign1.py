#bubble sort

def sort(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums

                



list1=[]
num=int(input("Enter no: of elements: "))
print(num)

for i in range(0,num):
    x=int(input("Enter the number: "))
    list1.append(x)
print(list1[0])

sort_list=sort(list1)
print(sort_list)


 