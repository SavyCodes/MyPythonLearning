# List

# indexing / slicing
course = ['History','Maths','Physic','CompSci']
course1= ['Art', 'Education']
# To print List
print(course)

# To print Last item of list we use negative index
print(course[-1])

# To slice the list
print(course[2:])

# To append Valve in list
course.append('Art')
print(course)

# To Insert Value in list on specifed index
course.insert(0, course1)
print(course)

# To extend list
course.extend(course1)
print(course)

# To Pop the list value
popped = course.pop()
print(popped)

# To Sort
courses=['Maths','Science','History']
courses.sort()
print(courses)

# Another way to sort 
sorted_course = sorted(courses)
print(sorted_course)

# Index of Valve in list
print(course.index('CompSci'))

# To Iterate a list of Valves
for item in course:
    print(item)

# enumerate item in list 
for index, item in enumerate(course):
    print(index, item)

# enumerate item in list start index with 1
for index, item in enumerate(course, start=1):
    print(index, item)

course_string = ', '.join(courses)
print(course_string)