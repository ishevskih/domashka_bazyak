class LampRow:
  def __init__(self, _count = 8):
    self.count = _count
    self._state = "0" * _count
  
  def get_state(self):
    return self._state
  
  def set_state(self, _state):
    if len(_state) == self.count:
      self._state = _state
    else:
      print(f"ошибка")
      self._state = "0" * self.count
  
  state = property(get_state, set_state)
  
  def show(self):
    result = ""
    for i in self._state:
      if i == "1":
        result += "*"
      else:
        result += "-"
    print(result)


lamps = LampRow(6)
lamps.show()              
lamps.state = "101010"
print(lamps.state)      
lamps.show()             
lamps.state = "10101010"  
print(lamps.state)       
lamps.show()              
