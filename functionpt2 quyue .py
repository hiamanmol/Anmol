def compute_taxes(amount, tax): # IN FUCTIONS WE CAN GIVE VALUES FROM (RIGHT TO LEFT) ONLY!!
    amount_to_pay = amount+amount*tax
    return amount_to_pay

# WHEN WE PRINT FUNCTION NAME IT WILL GIVE US HASHCODE OF IT

print("Amount :",compute_taxes)
print("Hashcode is:", id(compute_taxes), hex(id(compute_taxes)))

# REFRENCE COPY
fun = compute_taxes
print("fun is:", fun)

result = fun(amount=100, tax=2)
print("Result is :", result)

del compute_taxes

result = fun(amount=200, tax=5)
print("Result is :", result)


