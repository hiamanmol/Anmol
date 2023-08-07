names = "john,anmol,jim,abhi"
print(len(names))
print(names[2])
print(names[len(names)-1])

split_names = names.split(",")
print(split_names, type(split_names))

s1 = names.replace("jim", "mike")
print("names:", names)
print("s1:", s1)