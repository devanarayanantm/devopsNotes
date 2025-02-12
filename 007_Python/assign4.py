def list_to_dict(lst):
    anslist=[]
    for item in lst:
        dict_country={}
        # print(item)
        dict_country['Country'] = item[0][0]
        dict_country['City'] = item[0][1]
        anslist.append(dict_country)
    print(anslist)


list_to_dict([ [('India','kochi')], [('fin', 'finland')], [('hel','helenski')]])