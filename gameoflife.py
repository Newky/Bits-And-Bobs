import pygame
import random
import sys

from pygame.locals import KEYDOWN


def get_neighbour_count(grid, from_i, to_i, i, j):
	"""
	This takes the full grid.
	It takes a from i and a to i
	It takes the current I and the current J
	It then gets a count of all neighbours for instance
	with the current cell being 1,1 and X denoting alive, 0 dead.
	XOX
	OXO
	OOO
	This will return 2 neighbours
	"""
	if from_i < 0:
		from_i = i
	if to_i == len(grid):
		to_i = i
	neighbour_count = 0
	for curr_i in range(from_i, to_i + 1):
		ignore_index = None
		if curr_i == i:
			ignore_index = j
		neighbour_count += get_row_count(grid[curr_i], j,
			ignore_index=ignore_index)
	return neighbour_count


def get_row_count(grid, i, ignore_index):
	"""
	Given a single row it takes the count of the 
	i - 1, i and i + 1 indexs.
	Aliveness is denoted by alive > 0
	"""
	count = 0
	if i - 1 >= 0:
		count += int(grid[i - 1] > 0)
	if i + 1 < len(grid):
		count += int(grid[i + 1] > 0)
	if ignore_index is None:
		count += int(grid[i] > 0)
	return count


def test_cell(alive, neighbour_count):
	"""
	Takes an alive status of a cell, and number of neighbour cells.
	Applies conway game of life rules.
	"""
	if alive:
		if neighbour_count < 2:
			# under population
			return False
		elif neighbour_count in [2, 3]:
			return True
		elif neighbour_count > 3:
			# overcrowding
			return False
	else:
		if neighbour_count == 3:
			return True
	return alive


def update_grid(grid):
	"""
	The algorithm for this is the usual conways game of life.
	Input param is the grid.
	It first uses the get_neighbour_count to get the number of
	neighbours.
	Secondly it uses the conways rules to determine whether it is alive.
	"""
	for i in xrange(len(grid)):
		for j in xrange(len(grid[i])):
			neighbour_count = get_neighbour_count(grid,
				i - 1, i + 1, i, j)
			aliveness = test_cell(grid[i][j], neighbour_count)
			if not aliveness:
				grid[i][j] = 0
			else:
				grid[i][j] += aliveness


def color_from_number(alive):
	"""
	Some silly little color rules I came up with to represent the
	livelihood of a cell.
	White is dead.
	Black is child.
	Red is teenager
	Blue is rest of life(adult I guess)
	"""
	if not alive:
		color = pygame.Color(255, 255, 255),
	elif alive in range(1, 13):
		#black signifys child
		color = pygame.Color(0, 0, 0),
	elif alive in range(13, 21):
		#teenager
		color = pygame.Color(255, 0, 0),
	elif alive in range(21, 31):
		#Young adult.
		color = pygame.Color(0, 0, 255),
	elif alive >= 31:
		#Rest of lifes..
		color = pygame.Color(0, 255, 0),
	return color


def draw_screen(screen, grid, objs):
	"""
	Get color from number.
	Draw rectangle on screen.
	"""
	for i in range(0, len(grid)):
		for j, alive in enumerate(grid[i]):
			color = color_from_number(alive)
			pygame.draw.rect(screen, color, objs[i][j])


def inputs(events):
	"""
	Function which takes inputs.
	"""
	for event in events:
		if event.type == KEYDOWN:
			if event.key == 27:
				sys.exit(1)


def organic_tester(starting_grid, starting_index=1):
	starting_grid[starting_index][1] = True
	starting_grid[starting_index][2] = True
	starting_grid[starting_index][3] = True
	starting_grid[starting_index][4] = False
	starting_grid[starting_index][5] = False
	starting_grid[starting_index + 1][1] = True
	starting_grid[starting_index + 2][1] = False
	starting_grid[starting_index + 2][2] = False
	starting_grid[starting_index + 2][3] = False
	starting_grid[starting_index + 2][4] = True
	starting_grid[starting_index + 2][5] = True
	starting_grid[starting_index + 3][1] = False
	starting_grid[starting_index + 3][2] = True
	starting_grid[starting_index + 3][3] = True
	starting_grid[starting_index + 3][4] = False
	starting_grid[starting_index + 3][5] = True
	starting_grid[starting_index + 4][1] = True
	starting_grid[starting_index + 4][2] = False
	starting_grid[starting_index + 4][3] = True
	starting_grid[starting_index + 4][4] = False
	starting_grid[starting_index + 4][5] = True


def window_setup(WINDOW_WIDTH=800, WINDOW_HEIGHT=800):
	"""
	This simply sets up the various pygame initialisations.
	Sets the size to be WINDOW_WIDTH, WINDOW_HEIGHT
	Sets a caption, and returns a surface object.
	"""
	pygame.init()
	pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption('Conways Game of Life')
	return pygame.display.get_surface()


def init_grid(starting_func=None):
	"""
	Init grid is responsible for setting up the initial grid for the
	game. It can take a seeding function, by default this is
	randint(0, 1). 
	It returns 2 list of lists.
	One representing the aliveness of cells.
	The other contains the pygame.rect objects to be drawn
	"""
	starting_grid = []
	starting_grid_objects = []
	ROWS = 160
	COLUMNS = 160
	STARTING_X = 0
	x = STARTING_X
	y = 0
	cell_width = 5

	if not starting_func:
		starting_func = lambda: random.randint(0, 1)

	for i in xrange(ROWS):
		row = []
		row_objs = []
		for j in xrange(COLUMNS):
			row.append(starting_func())
			row_objs.append(pygame.Rect(x, y, 20, 20))
			x += cell_width
		starting_grid.append(row)
		starting_grid_objects.append(row_objs)
		y += cell_width
		x = STARTING_X

	return starting_grid, starting_grid_objects


def main():
	screen = window_setup()

	def every_second_one():
		closed_variable = [0]
		def func():
			closed_variable[0] += 1
			if closed_variable[0] % 2 == 0:
				return 1
			else:
				return 0

		return func

	starting_grid, starting_grid_objects = init_grid(starting_func=every_second_one())

	while True:
		update_grid(starting_grid)
		draw_screen(screen, starting_grid, starting_grid_objects)
		inputs(pygame.event.get())
		pygame.display.update()


if __name__ == "__main__":
	main()
