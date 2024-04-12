if __name__ == "__main__":
    s = input()
    print(True if True in [i.isalnum() for i in s] else False)
    print(True if True in [i.isalpha() for i in s] else False)
    print(True if True in [i.isdigit() for i in s] else False)
    print(True if True in [i.islower() for i in s] else False)
    print(True if True in [i.isupper() for i in s] else False)
