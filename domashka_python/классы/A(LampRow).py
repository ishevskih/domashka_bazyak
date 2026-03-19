class LampRow:
  def __init__(self, _state = ""):
    self.state = _state
  def show(self):
    if len(self.state) != 8:
      self.state = "00000000"
    result = ""
    for i in self.state:
      if i == "1":
        result += "*"
      else:
        result += "-"
    print(result)
  def state(self, _state):
    self.state = _state
lamps = LampRow()
lamps.show() 
lamps.state = "10101010"
print(lamps.state) 
lamps.show()
