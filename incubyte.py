class GalacticSpacecraft:
    def _init_(self, start_position, start_direction):
        """
        Initialize the GalacticSpacecraft with starting position and direction.

        Args:
            start_position (list): Starting coordinates [x, y, z].
            start_direction (str): Starting direction (N, S, E, W, Up, Down).
        """
        self.position = start_position
        self.direction = start_direction

    def move_forward(self):
        """
        Move the spacecraft one step forward based on its direction.
        """
        if self.direction == "N":
            self.position[1] += 1
        elif self.direction == "S":
            self.position[1] -= 1
        elif self.direction == "E":
            self.position[0] += 1
        elif self.direction == "W":
            self.position[0] -= 1
        elif self.direction == "Up":
            self.position[2] += 1
        elif self.direction == "Down":
            self.position[2] -= 1

    def move_backward(self):
        """
        Move the spacecraft one step backward based on its direction.
        """
        if self.direction == "N":
            self.position[1] -= 1
        elif self.direction == "S":
            self.position[1] += 1
        elif self.direction == "E":
            self.position[0] -= 1
        elif self.direction == "W":
            self.position[0] += 1
        elif self.direction == "Up":
            self.position[2] -= 1
        elif self.direction == "Down":
            self.position[2] += 1

    def turn_left(self):
        """
        Rotate the spacecraft 90 degrees to the left.
        """
        directions = ["N", "W", "S", "E", "Up", "Down"]
        current_idx = directions.index(self.direction)
        new_idx = (current_idx - 1) % len(directions)
        self.direction = directions[new_idx]

    def turn_right(self):
        """
        Rotate the spacecraft 90 degrees to the right.
        """
        directions = ["N", "E", "S", "W", "Up", "Down"]
        current_idx = directions.index(self.direction)
        new_idx = (current_idx + 1) % len(directions)
        self.direction = directions[new_idx]

    def turn_up(self):
        """
        Rotate the spacecraft angle upwards.
        """
        if self.direction == "N" or self.direction == "S":
            self.direction = "Up"

    def turn_down(self):
        """
        Rotate the spacecraft angle downwards.
        """
        if self.direction == "N" or self.direction == "S":
            self.direction = "Down"

def execute_commands(spacecraft, commands):
    """
    Execute a sequence of commands on the spacecraft.

    Args:
        spacecraft (GalacticSpacecraft): The spacecraft object.
        commands (list): List of commands to execute.
    """
    for command in commands:
        if command == "f":
            spacecraft.move_forward()
        elif command == "b":
            spacecraft.move_backward()
        elif command == "r":
            spacecraft.turn_right()
        elif command == "l":
            spacecraft.turn_left()
        elif command == "u":
            spacecraft.turn_up()
        elif command == "d":
            spacecraft.turn_down()

def main():
    start_position = [0, 0, 0]
    start_direction = "N"
    spacecraft = GalacticSpacecraft(start_position, start_direction)

    commands = ["f", "r", "u", "b", "l", "u", "d"]
    execute_commands(spacecraft, commands)

    print("Final Position:", spacecraft.position)
    print("Final Direction:", spacecraft.direction)

if _name_ == "_main_":
    main()
