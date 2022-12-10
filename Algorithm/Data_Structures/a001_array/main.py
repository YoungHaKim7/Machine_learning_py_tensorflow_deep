arr = [2, 5, 3, 10, 8]
print("\nINITIAL ARRAY")
print(arr)


print("--------")
#Append to array
print("\nAPPEND TO ARRAY")
arr.append(100)
print(arr)


print("--------")
# Get an array element
print("\nGET AN ARRAY ELEMENT")
print(arr[2])



print("--------")
# Set an array element
print("\nSET AN ARRAY ELEMENT")
arr[2] = 50
print(arr)


print("--------")
# Insert value : 38 at array 2
print("\nINSERT AN ARRAY ELEMENT")
arr.insert(2, 38)
print(arr)


print("--------")
# Delete from array
print("\nDELETE FROM ARRAY")
arr.pop(2) # delete by index
print(arr)


print("--------")
# Get array slice
print("\nGET ARRAY")
print(arr[2:5])

