if __name__ == "__main__":
    N = int(input())
    I = []
    for _ in range(N):
        user = input().split()

        if user[0] == "insert":
            I.insert(int(user[1]), int(user[2]))

        elif user[0] == "print":
            print(I)

        elif user[0] == "remove":
            I.remove(int(user[1]))

        elif user[0] == "append":
            I.append(int(user[1]))

        elif user[0] == "sort":
            I.sort()

        elif user[0] == "pop":
            I.pop()

        elif user[0] == "reverse":
            I.reverse()
