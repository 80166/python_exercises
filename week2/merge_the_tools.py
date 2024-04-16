import textwrap


def merge_the_tools(string, k):
    new_str = textwrap.wrap(string, k)
    for i in new_str:
        cases = "".join(set(i))
        print(cases)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
