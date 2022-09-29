import numpy as np
import matplotlib.pyplot as plt
from passenger import Passenger


class Plane:
    """

    """
    def __init__(self, x_dim, y_dim, exits, luggages, places, minors):
        """

        :param x_dim: The number of seats in each row of the plane
        :param y_dim: The number of rows in the plane
        :param exits: Tuple of row numbers of exit points
        """
        assert x_dim % 2 == 0, f"We only consider planes that have an even amount of seats per row \n "
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.row_size = self.x_dim//2
        self.exits = exits
        self.coordinate_system = np.zeros((y_dim + len(self.exits), x_dim + 1, 3))
        offset = 0
        for exit in self.exits:
            if exit == -1:
                self.coordinate_system[0, :, 0] = 1
            else:
                self.coordinate_system[exit + offset, :, 0] = 1
            offset += 1
        self.coordinate_system[:, self.row_size, 1] = 1
        self.passengers = []
        self.populate_with_passengers(luggages, places, minors)

    def populate_with_passengers(self, luggages, places, minors):
        for luggage, place, minor in zip(luggages, places, minors):
            self.passengers.append(Passenger(luggage, place, minor))
            self.coordinate_system[place[0], place[1], 2] = 1

    def is_free(self, place_request):
        return self.coordinate_system[place_request[0], place_request[1], 2] == 0

    def update_position(self, new_pos, old_pos):
        self.coordinate_system[new_pos[0], new_pos[1], 2] = 1
        self.coordinate_system[old_pos[0], old_pos[1], 2] = 0

    def act_on_intentions(self):
        for passenger in self.passengers:
            if passenger.on_plane:
                if not passenger.has_acted:
                    intention = passenger.collect_intention()
                    if self.is_free(intention):
                        self.update_position(intention, passenger.position)
                        passenger.act()

    def display(self):
        plt.imshow(self.coordinate_system)
        plt.show()


if __name__ == '__main__':
    plane = Plane(x_dim=6, y_dim=10, exits=(3, 7),
                  luggages=[True, False],
                  places=[(2, 5), (5, 4)],
                  minors=[False, False])
    plane.display()
