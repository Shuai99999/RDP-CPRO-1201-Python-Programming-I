list1 = input("Enter the first list of numbers separated by spaces: ").split()
list2 = input("Enter the second list of numbers separated by spaces: ").split()

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

common_elements = []
for element in list1:
    if element in list2 and element not in common_elements:
        common_elements.append(element)

print("Common elements:", common_elements)
