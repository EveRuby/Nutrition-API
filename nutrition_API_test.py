test_list = ["Geeks", None, "CS", None, None]
  
# printing original list 
print("The original list is : " + str(test_list))
  
# using lambda
# Converting None to empty string
conv = lambda i : i or ''
res = [conv(i) for i in test_list]
  
# printing result 
print("The list after conversion of None values : " + str(res))

