# fruit_a, fruit_c, fruit_f = ["kiwi","apple","blueberry"]
# city_h, city_t, city_w = "Paris","Berlin","Chihuahua"

# new_tuple = 1,34,21,34,56
# print(new_tuple)

# def sortting_algorithm(lst):
#     n = len(lst)
#     # Traverse through all list elements
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             # Traverse the list
#             # Swap if the element found is greater than the next element
#             if lst[j] > lst[j+1] :
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
 
# spells = ['Accio', 'Avada Kedavra', 'Expecto Patronum', 'Wingardium Leviosa', 'Expelliarmus', 'Lumos', 'Alohomora']
# print(sortting_algorithm(spells))
# def print_month_name(month):
#     months = {
#         1: 'January',
#         2: 'February',
#         3: 'March',
#         4: 'April',
#         5: 'May',
#         6: 'June',
#         7: 'July',
#         8: 'August',
#         9: 'September',
#         10: 'October',
#         11: 'November',
#         12: 'December'
#     }
#     print(months.get(month, 'Invalid month'))

def print_cities():
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco", "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington"]
    
    for city in cities:
          print(city)