import numpy as np

a = np.array([2, 3, 4, 5])

b = np.array([8, 5, 4])

c = np.array([5, 4, 6, 8, 3])

ax, bx, cx = np.ix_(a, b, c)

print(ax)

print(bx)

print(cx)

print(ax.shape, bx.shape, cx.shape)

result = ax + bx * cx

print(result)

print(result[3, 2, 4])

print(a[3] + b[2] * c[4])


def ufunc_reduce(ufct, *vectors):

   vs = np.ix_(*vectors)
   r = ufct.identity

   for v in vs:
       r = ufct(r, v)

   return r


print(ufunc_reduce(np.add, a, b, c))
