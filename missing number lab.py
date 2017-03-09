def find_missing(list1, list2):
    try:        
        if len(list1) > len(list2):
            return [x for x in list1 if x not in list2]
        else:
            return [x for x in list2 if x not in list1][0]
    except IndexError:
        return 0
