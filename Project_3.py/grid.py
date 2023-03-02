class Grid:
    def __init__(self, rows, colums, values = None):
        self.grid = []

        for row in range(rows):
            self.grid.append([])
            for col in range(colums):
                self.grid[row].append(values)

    def get_height (self):
        return len(self.grid)
    
    def get_width(self):
        return len(self.grid[0])
    
    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.grid[row][col]) + " "

            result += "\n"
        return str(result)

