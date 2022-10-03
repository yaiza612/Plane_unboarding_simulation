import numpy as np
import matplotlib.pyplot as plt
import random
from passenger import Passenger


class Plane:
    def __init__(self, x_dim, y_dim, exit_rows, luggages, places, minors):
        """

        :param x_dim: The number of seats in each row of the plane
        :param y_dim: The number of rows in the plane
        :param exit_rows: List of row numbers of exit points
        """
        assert x_dim % 2 == 0, f"We only consider planes that have an even amount of seats per row"
        assert np.min(exit_rows) >= 0 and np.max(exit_rows) < y_dim, \
            f"Each exit row must exist in the dimensions of the plane"
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.row_size = self.x_dim//2
        self.exit_rows = exit_rows
        self.coordinate_system = np.zeros((y_dim, x_dim + 1, 3))
        for exit_row in self.exit_rows:
            self.coordinate_system[exit_row, :, 0] = 1
        self.coordinate_system[:, self.row_size, 1] = 1
        self.passengers = []
        self.available_passenger_indices = list(range(len(luggages)))
        self.populate_with_passengers(luggages, places, minors)
        self.done = False

    def populate_with_passengers(self, luggages, places, minors):
        for luggage, place, minor in zip(luggages, places, minors):
            self.passengers.append(Passenger(luggage, place, minor))
            self.coordinate_system[place[1], place[0], 2] = 1

    def is_free(self, place_request, passenger):
        return self.coordinate_system[place_request[1], place_request[0], 2] == 0 or place_request == passenger.place

    def update_position(self, new_pos, old_pos):
        self.coordinate_system[old_pos[1], old_pos[0], 2] = 0
        self.coordinate_system[new_pos[1], new_pos[0], 2] = 1


    def act_on_intentions(self):
        passengers_to_act = self.available_passenger_indices[::]
        action_taken = True
        while action_taken:  # as long as a passenger can do an action he planned, we continue the time-step
            action_taken = False
            # shuffle the indices to simulate random ordering of priorities
            random.shuffle(passengers_to_act)
            for passenger_idx in passengers_to_act:
                passenger = self.passengers[passenger_idx]
                intention = passenger.collect_intention(self.row_size, self.exit_rows)
                if self.is_free(intention, passenger):
                    self.update_position(intention, passenger.place)
                    passenger_left_plane = passenger.act(self.exit_rows)
                    if passenger_left_plane:
                        self.available_passenger_indices.remove(passenger_idx)
                        self.coordinate_system[passenger.place[1], passenger.place[0], 2] = 0
                    action_taken = True
                    passengers_to_act.remove(passenger_idx)
        if len(self.available_passenger_indices) == 0:
            self.done = True
        return self.done

    def display(self):
        plt.imshow(self.coordinate_system)
        plt.show()


if __name__ == '__main__':
    plane = Plane(x_dim=6, y_dim=10, exit_rows=[3, 7],
                  luggages=[True, False],
                  places=[(2, 5), (5, 4)],
                  minors=[False, False])
    plane.display()
