# DICTIONARY
my_tuple = tuple()
print(my_tuple, type(my_tuple))
my_list = list()
print(my_list, type(my_list))
my_set = set()
print(my_set, type(my_set))
my_dictionary = dict()
print(my_dictionary, type(my_dictionary))

my_data = {101: "anmol", 102: "abhi", 103: "john"}
print(my_data)

print("Min :", min(my_data))
print("Max :", max(my_data))
print("Sum :", sum(my_data))

print(my_data[201])
print(my_data.get(201))
# my_data del [201]
my_data.pop(201)
print(my_data)

my_data[775] = "leo"
print(my_data)

my_data[775] = "leo"
print(my_data)

del my_data[775]
coloums = ["ludhiana","delhi","bathinda"]
population = {}.fromkeys(coloums,"12000")
print("population", population)

population["delhi"] = 2100

# COVERT DICTIONARY INTO LIST OF TUPLES
items = list(population.items())
print("items")
print(items)

