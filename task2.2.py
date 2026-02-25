start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
sum = 0
for i in range(start,end + 1):
    sum += i

print(f"\nThe sum of numbers from {start} to {end} is {sum}")