# tuples are immutable sequences, typically used to store collections of heterogeneous data. Tuples are defined by enclosing the elements in parentheses `()`.  
example_tuple = (1, "hello", 3.14, True)
# example_tuple[1] = "world"  # This will raise an error because tuples are immutable
print(example_tuple[3])  

# datatype
print(type(example_tuple))  

# create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# create a single element tuple

# To create a single element tuple, you need a trailing comma.
single_element_tuple = (42,) 
print("Single element tuple:", single_element_tuple)
print("Type of single element tuple:", type(single_element_tuple))

single_element_tuple = (42) # This is not a tuple, it's just an integer. 
print("Single element without comma:", single_element_tuple)
print("Type of single element without comma:", type(single_element_tuple))

# Accessing the first element of the tuple
print(example_tuple.index("hello")) 

# counting the number of occurrences of an element in a tuple
print("Count of 3.14 in example_tuple:", example_tuple.count(3.14))