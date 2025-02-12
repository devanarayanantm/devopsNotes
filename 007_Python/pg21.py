#operation on regular programs

import re

str1 = "Goodmorning all,goof dgood g  good  goog good ggod good"

# match = re.match("good",str1,re.I)
# print(match)
# if match:
#     print("matching",match.group(0))

# match1=re.findall("(?i)Morning",str1)
# print(match1)

# match1=re.findall("(?i)good",str1,re.DOTALL)
# print(match1)

# match1=re.search("(?i)Morning",str1,re.DOTALL)
# print(match1)

# lst=[]
# for i in re.finditer("(?i)good",str1):
#     print(i)
#     lst.append(i)
# print(lst)

# match=re.sub("(?i)good","awesome",str1)
# print(match)


# match=re.split("good",str1)
# print(match)


pattern = r'.*[g][o][o][d].*'
match = re.findall(pattern,str1)
print(match)