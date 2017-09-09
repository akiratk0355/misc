'''
Collection of sorting algorithms just for learning's sake

Created on Jun 17, 2016
'''

# Readings

# Problem Solving with Algorithms and Data Structures using Python
# http://interactivepython.org/runestone/static/pythonds/index.html


unsorted = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#unsorted = [154, 126, 93, 27, 15, 12, 43, 2, 2]

# TODO: implement swap func
def _swap(i, j):
    pass


# Insertion sort
def insertion_sort(lst):
    ilist = lst[:]
    ctr = 0
    print("insertion_sort: %s received" % ilist)
    for index in range(1,len(ilist)):
        currentvalue = ilist[index]
        position = index
        print("-----looking at %s------" % currentvalue)
    
        while position > 0 and ilist[position-1] > currentvalue:
            ilist[position-1], ilist[position] = "x", ilist[position-1]
            position = position-1
            print("%s: %s moved backwards" % (ilist, currentvalue))
          
        ilist[position]=currentvalue
        print("%s: %s was fixed" % (ilist, currentvalue))
        
    print("%s: sort completed" % ilist)
    return ilist

sorted_insert = insertion_sort(unsorted)
print("RESULT INSERTION: %s" % sorted_insert)

# Selection sort
def selection_sort(lst):
    slist = lst[:]
    print("selection_sort: %s received" % slist)
    length = len(slist)
    i = 0 
    # let's decide a number put at ith entry in the list
    while i < length - 1:
        j = i + 1
        smallest = slist[i]
        smallest_idx = i
        while j <= length - 1:
            if slist[j] < smallest:
                smallest = slist[j]
                smallest_idx = j
            j += 1
        slist[i], slist[smallest_idx] = slist[smallest_idx], slist[i]
        i += 1
    return slist

sorted_selection = selection_sort(unsorted)
print("RESULT SELECTION: %s" % sorted_selection)
            

# Bubble sort 
def bubble_sort(lst):
    blist = lst[:]
    print("bubble_sort: %s received" % blist)
    length = len(blist)
    for endpoint in range(1, length): # range(a, b) returns all x that satisfies a <= x and x < b e.g. range(1,3) =[1,2]   
        position = len(blist) - 1
        print(blist)
        while position >= endpoint:
            if blist[position-1] > blist[position]:
                blist[position], blist[position-1] = blist[position -1], blist[position]
            position = position - 1
    return blist

sorted_bubble = bubble_sort(unsorted)
print("RESULT BUBBLE: %s" % sorted_bubble)


def merge_sort(lst):
    mlist = lst[:]
    length = len(mlist)
    print("merge_sort: %s received" % mlist)
    if length == 0:
        print("merge_sort: sorting empty list, abort")
        return mlist
    if length <= 2:
        if length == 2 and mlist[0] > mlist[1]:
            mlist[0], mlist[1] = mlist[1], mlist[0]
        return mlist
    else:
        mididx = length // 2
        sorted_lefthalf = merge_sort(mlist[:mididx])
        sorted_righthalf = merge_sort(mlist[mididx:])
        merged = []
        print("merge_sort: merging two lists: %s and %s" % (sorted_lefthalf, sorted_righthalf))
        while len(sorted_lefthalf) and len(sorted_righthalf):
            if sorted_lefthalf[0] < sorted_righthalf[0]:
                merged.append(sorted_lefthalf.pop(0))
            else:
                merged.append(sorted_righthalf.pop(0))
        
        # append remaining list when either of two lists becomes empty
        merged.extend(sorted_lefthalf)
        merged.extend(sorted_righthalf)
        print("merge_sort: merging completed: %s" % merged) 
        return merged

      
sorted_merge = merge_sort(unsorted)
print("RESULT MERGE: %s" % sorted_merge)        
    

if      sorted_insert == sorted_bubble \
    and sorted_merge == sorted_bubble \
    and sorted_selection == sorted_bubble:
    print("SUCCESS")
else:
    print("FAIL")


