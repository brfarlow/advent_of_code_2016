class Taxicab:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.direction = "n"

	def turn_left(self):
		if self.direction == "n":
			self.direction = "w"
		elif self.direction  =="w":
			self.direction = "s"
		elif self.direction == "s":
			self.direction = "e"
		else:
			self.direction = "n"

	def turn_right(self):
		if self.direction == "n":
			self.direction = "e"
		elif self.direction == "w":
			self.direction = "n"
		elif self.direction == "s":
			self.direction = "w"
		elif self.direction == "e":
			self.direction = "s"

	def move(self):
		if self.direction == "n":
			self.y += 1
		elif self.direction == "w":
			self.x -= 1
		elif self.direction == "s":
			self.y -= 1
		else:
			self.x += 1


if __name__ == '__main__':

	with open('input.txt', 'r') as f:
		content = f.read().replace(" ",'').split(",")
	taxi = Taxicab()

	visited = []
	visited.append((0,0))
	for item in content:
		if item[0] == "L":
			taxi.turn_left()
		else:
			taxi.turn_right()

		i = 0
		hasLocation = False
		while i < int(item[1:]):
			i += 1
			taxi.move()
			if (taxi.x, taxi.y) in visited:
				hasLocation = True
				break
			else:
				visited.append((taxi.x,taxi.y))
		if(hasLocation):
			break;	


	print abs(taxi.x) + abs(taxi.y)