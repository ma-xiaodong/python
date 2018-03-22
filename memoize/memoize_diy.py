fib_memo = {}

class Memoize:
  def __init__(self, f):
    self.f = f
    self.memo = {}
  def __call__(self, *args):
    if not args in self.memo:
      self.memo[args] = self.f(*args)
    return self.memo[args]

def fib(k):
  if k < 3: return 1
  if k not in fib_memo:
    fib_memo[k] = fib(k - 1) + fib(k - 2)
  return fib_memo[k]

if __name__ == "__main__":
  fib_func = Memoize(fib)

  print fib_func(8)
  print fib_func(10)
  print fib_func(12)

