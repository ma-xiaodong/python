class Memoize:
  def __init__(self, f):
    self.f = f
    self.memo = {}
  def __call__(self, *args):
    if not args in self.memo:
      self.memo[args] = self.f(*args)
    return self.memo[args]

@Memoize
def fib(k):
  if k < 3: return 1
  return fib(k - 1) + fib(k - 2)

if __name__ == "__main__":
  print fib(8)
  print fib(10)
  print fib(12)
