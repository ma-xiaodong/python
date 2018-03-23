from functools import wraps

class Person(object):
  @staticmethod
  def hello():
    print "static hello!"

def log(text):
  def decorator(func):
    print text
    def wrap(*args, **kw):
      print "2018-03-22"
      return func(*args, **kw)
    return wrap
  return decorator

@log("Parameterized decorator:")
def now():
  print "2018-03-23"

def log_wraps(text):
  def decorator_wraps(func):
    print text
    @wraps(func)
    def log_wraps(*args, **kw):
      print "2018-03-22 in wraps"
      return func(*args, **kw)
    return log_wraps
  return decorator_wraps

@log_wraps("Parameterized & wrapped decorator:")
def now_wraps():
  print "2018-03-23 in wraps"

if __name__ == "__main__":
  Person.hello()
  now()
  print now.__name__
  now_wraps()
  print now_wraps.__name__

