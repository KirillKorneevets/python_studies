def geometric_progression(n):
    import pdb; pdb.set_trace()
    c = 0
    for i in range(1, n+1):
         c = 1 * 3 ** (i - 1)
         yield c



d = geometric_progression(10)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
