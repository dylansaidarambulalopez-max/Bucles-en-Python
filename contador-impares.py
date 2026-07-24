#contador de numerps impares
n = int(input("numero positivo: "))
i = 1
while True:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
    if i > n:
        break
print("\nFin. se mostraron los impares hasta", n)