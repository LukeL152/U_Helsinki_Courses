#!/usr/bin/env python3


def triple(x):
    tripled = x * 3
    return tripled


def square(x):
    squared = x * x
    return squared


def main():
    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        if t >= s:
            print(f"triple({i})=={t} square({i})=={s}")
        else:
            break


if __name__ == "__main__":
    main()
