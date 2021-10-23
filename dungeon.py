from random import randint, choice

class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

def draw_grid(g, width=2):
    for y in range(g.height):
        for x in range(g.width):
            if (x, y) in g.walls:
                symbol = '#'
            else:
                symbol = '.'
            print("%%-%ds" % width % symbol, end="")
        print()

def get_walls(g: MapGrid, pct=.25):
        out = []
        for i in range(int(g.height*g.width*pct)//2):

            x = randint(1, g.width-2)
            y = randint(1, g.height-2)

            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
        return out

def main():
    g = MapGrid(10, 10)
    g.walls = get_walls(g)
    draw_grid(g)

if __name__ == '__main__':
    main()
