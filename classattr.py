class Example(object):
  def __init__(self):
    self.name = "Girish"
  def printex(self):
    print("This is an example")

e=Example()

print(hasattr(e,"name"))
print(getattr(e,"name"))
print(dict(Example))