from types import MethodDescriptorType


def parosak(meddig):
    for x in range(meddig):
        if x % 2 == 0:
            yield x

for x in parosak(1000):
    print(x)