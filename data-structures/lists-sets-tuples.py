#list methods

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'German']

#courses.append(courses_2)  #output: ['History', 'Math', 'Physics', 'CompSci', ['Art', 'German']]
courses.extend(courses_2)  #output: ['History', 'Math', 'Physics', 'CompSci', 'Art', 'German']

#courses.remove('History')
#courses.pop()               #output: removes last item
courses.index('Physics')    #output: returns index

print('Art' in courses)     #returns boolean


#get index and item in list
for index, course in enumerate(courses):
    print(index, course)

#list to string, comma-separated
courses_str = ', '.join(courses)
#print(courses_str)                  #output: History, Math, Physics, CompSci, Art, German

#sorting methods
nums = [1, 5, 3, 11, 9, 7]
nums.sort()                 #output: sorts in ascending order
nums.sort(reverse=True)     #output: sorts in descending order

#tuples
#tuples
#tuples
courses_tup = ('History', 'Math', 'Physics', 'CompSci')    #immutable


#sets
#sets
#sets
courses_set = {'History', 'Math', 'Physics', 'CompSci'}     #unordered, removes duplicates
electives_set = {'Spanish', 'Econ', 'CompSci'}

print(courses_set.intersection(electives_set))              #find what two sets have in common
print(courses_set.difference(electives_set))                #find what two sets do NOT share in common
print(courses_set.union(electives_set))                     #combine two sets


#create empty litss, tuples, sets
empty_lst = []
empty_lst= list()

empty_tup = ()
empty_tup = tuple()

empty_set = set()







