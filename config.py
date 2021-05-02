weather_key = "273f91442c966dbca2945393b9e9390d"
g_key = "AIzaSyAsKuDwzTZOEs67DVsnwgC6dRHr-LcX3D8"


# mystring = 'This is a test.'

# for i in range(len(mystring)):
#     print (mystring[i])

# mystring_list = [mystring[x] for x in range(len(mystring))]
# print(mystring_list)

tuple_1 = (1, 'Hyderabad', 13.5, True)
tuple_2 = (11, 22, 33)
tuple_2 = tuple_2 + (44,)

print(sorted(tuple_2))
def area_vol_cube(side_length):
    area = 6 * side_length * side_length
    volume = side_length * side_length * side_length
    return area, volume
