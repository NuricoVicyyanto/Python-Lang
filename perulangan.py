# for loop
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in angka:
    print(i)

print("=" * 20)  # tanda pemisah

# while loop
count = 0
while count < 10:
    print("angka ke ", count)
    count += 1

print("=" * 20)  # tanda pemisah

# nested loop
i = 2
while(i < 20):
    j = 2
    while(j <= (i/j)):
        if not(i % j):
            break
        j = j + 1
    if (j > i/j):
        print(i, " adalah bilangan prima")
    i = i + 1
