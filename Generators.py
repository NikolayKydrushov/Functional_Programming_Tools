
def all_variants(text):
    length = len(text)

    for i in range(1, length + 1):

        for start in range(length - i + 1):
            yield text[start:start + i]


a = all_variants("abc")
for i in a:
    print(i)


"""
a
b
c
ab
bc
abc
"""