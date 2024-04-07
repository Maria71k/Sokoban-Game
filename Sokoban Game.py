class Sokoban:
    def __init__(self, level):
        self.level = level
        self.player_row, self.player_col = self.find_player()
        self.directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        self.targets = self.find_targets()

    def find_player(self):
        for row_idx, row in enumerate(self.level):
            for col_idx, cell in enumerate(row):
                if cell == 'P':
                    return row_idx, col_idx

    def find_targets(self):
        targets = []
        for row_idx, row in enumerate(self.level):
            for col_idx, cell in enumerate(row):
                if cell == 'T':
                    targets.append((row_idx, col_idx))
        return targets

    def is_valid_move(self, row, col):
        return 0 <= row < len(self.level) and 0 <= col < len(self.level[0]) and self.level[row][col] in (' ', 'T')

    def move_player(self, direction):
        d_row, d_col = self.directions[direction]
        new_row, new_col = self.player_row + d_row, self.player_col + d_col

        if self.is_valid_move(new_row, new_col):
            if self.level[new_row][new_col] == 'T':
                self.targets.remove((new_row, new_col))

            self.level[self.player_row][self.player_col] = ' '
            self.level[new_row][new_col] = 'P'
            self.player_row, self.player_col = new_row, new_col

    def is_game_over(self):
        return len(self.targets) == 0

    def print_board(self):
        for row in self.level:
            print(''.join(row))

    def play(self):
        print("Welcome to Sokoban!")
        while not self.is_game_over():
            self.print_board()
            direction = input("Enter direction (w/a/s/d): ")
            self.move_player(direction)
        print("Congratulations! You won!")


if __name__ == "__main__":
    level = [
        "#####",
        "# P #",
        "#  T#",
        "# T #",
        "#####"
    ]
    game = Sokoban(level)
    game.play()
