# This piece of code is a calculator of "permutation without repetition" formula used in math in the field of probability
# n! / (n - p)!
# Where n is the number of elements in the set, and p is the number of elements desired, as p < n
# That code just returns the number of possible permutations, helping out in math questions without having to calculate fatorials. It doesn't offer all the permutations in lists

n = []
p = []
d = []
n1 = int(input('Número de elementos do arranjo: '))
p1 = int(input('Número de elementos do agrupamento: '))
d1 = n1 - p1
i = 1
m = 1
x = 1
y = 1

# Derivating n1 input into many elements
while i <= n1:
  n.append(i)
  i += 1

# Doing the same thing with the difference between n and p
if n[n1 - 1] == n1:
  i = 1
  while i <= d1:
    d.append(i)
    i += 1

# n!
while m < n1:
  x = x * n[-m]
  m += 1

m = 1

# (n - p)!
while m < d1:
  y = y * d[-m]
  m += 1

# n! / (n - p)!
Anp = int(x / y)
print(Anp)
