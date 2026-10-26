L = [2, 3, 4]
factorial= []
for n in L:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    factorial.append(fact)
print("factorial =", factorial)