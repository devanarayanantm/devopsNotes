numbers = [22,-55,11,55]
# numbers.sort()
# print('Min=',numbers[0],'max=',numbers[len(numbers)-1])


# sec_max=-99
# max_num=-99
# for i in range(0,len(numbers)):
#     if numbers[i] > max_num:
#         max_num=numbers[i]
    # max_num=max(max_num,numbers)
    # if (arr[i]!=max_num):
    #     sec_max=max(sec_max,numbers[i])


# for i in range(0,len(numbers)): 
#     if max_num != numbers[i] and sec_max < numbers[i]:
#         sec_max=numbers[i]



import heapq

def nsmallest(arr,n):
    heap = []

    heapq.heapify(heap)
    for i in arr:
        heapq.heappush(heap,i)
    
    for i in range(0,n-1):
        heapq.heappop(heap)

    return heapq.heappop(heap)

def nlargest(arr,n):
    heap = []

    heapq.heapify(heap)
    for i in arr:
        heapq.heappush(heap,-i)
    
    for i in range(0,n-1):
        heapq.heappop(heap)

    return -heapq.heappop(heap)



n=2
print(nsmallest(numbers,n))
print(nlargest(numbers,n))