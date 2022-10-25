def fakt(sz):
    if sz==1:
        return 1
    return sz*fakt(sz-1)

print(fakt(1035))