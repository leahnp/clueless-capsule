class Clothing:
  def __init__(self, clothing, color):
    self.type = clothing
    self.color = color


black_pants = Clothing("pants", "black")
print(getattr(black_pants, 'color'))



