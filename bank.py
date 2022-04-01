def deposit(name, sum):
    bank[name] += sum


def withdraw(name, sum):
    bank[name] -= sum


def balance(name):
    print(bank.get(name))


def transfer(name1, name2, sum):
    bank[name1] -= sum
    bank[name2] += sum


def income(p):
    for name in bank:
        if bank[name] > 0:
            newBalance = bank[name] * (100 + p) / 100
            bank[name] = int(newBalance)


bank = {}
numcommands = int(input())
for i in range (0, numcommands):
    command, *args = input().split()

    if command == 'BALANCE':
        if args[0] not in bank:
            print('ERROR')
        else:
            balance(args[0])

    elif command == 'DEPOSIT':
        if args[0] not in bank:
            bank[args[0]] = int(0)
        deposit(args[0], int(args[1]))

    elif command == 'WITHDRAW':
        if args[0] not in bank:
            bank[args[0]] = int(0)
        withdraw(args[0], int(args[1]))

    elif command == 'TRANSFER':
        if args[0] not in bank:
            bank[args[0]] = int(0)
        if args[1] not in bank:
            bank[args[1]] = int(0)
        transfer(args[0], args[1], int(args[2]))

    elif command == 'INCOME':
        income(int(args[0]))

    else:
        print('ERROR')