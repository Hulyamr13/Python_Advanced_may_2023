def read_next(*args):
    for sequence in args:
        for item in sequence:
            yield item


for i in read_next("Need", (2, 3), ["words", "."]):
 print(i)
