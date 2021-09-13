import matplotlib.pyplot as plt

size = int(input("enter the size of an array :"))
year = []
pop = []
print('Enter years :')
for i in range(size):
    year.append(int(input()))
print('Enter populations in billion :')
for i in range(size):
    pop.append(float(input()))
print(year)
print(pop)
plt.plot(year,pop)
# plt.scatter(year,population)
length = len(year)
print(year[length-1])
plt.show()

