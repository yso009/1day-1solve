a,b = map(int, input().split())

list_a = set(map(int, input().split()))
list_b = set(map(int, input().split()))


print(len(list_a - list_b) + len(list_b-list_a))

