""" A Python program that finds the largest value in a list using recursion by comparing the head with the maximum value found in the
tail."""

list = [2,5,8,10,12,56]

def listMax(list):
    head = list[0]

    if len(list) == 1:
        print(f"Head: {head}")
        return head

    tail = listMax(list[1:])

    print(f"Head: {head}")
    print(f"Tail: {tail}")

    if head > tail:
        return head
    else:
        return tail


print(f"Largest value: {listMax(list)}")