@dispatch((list, tuple), (str, int))
def concatenate(a, b):
    return list(a) + [b]

print(concatenate(["a", "b"], "c"))
# ['a', 'b', 'c']
print(concatenate(("a", "b"), 1))
# ['a', 'b', 1]