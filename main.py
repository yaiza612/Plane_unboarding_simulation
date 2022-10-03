"""
Copyright (C) 2022  Yaiza Arnaiz Alcacer and Samuel Schüler

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from plane import Plane
import random


def generate_places(x_dim, y_dim, exit_rows, num_passengers, luggage_percentage=0.7, minor_percentage=0.1):
    luggages = []
    places = []
    minors = []
    for _ in range(num_passengers):
        luggages.append(random.random() < luggage_percentage)
        minors.append(random.random() < minor_percentage)
        sampled_place = [random.randint(0, x_dim - 1), random.randint(0, y_dim - 1)]
        while sampled_place not in places and sampled_place[0] not in exit_rows:
            places.append(sampled_place)
            sampled_place = [random.randint(0, x_dim - 1), random.randint(0, y_dim - 1)]
    return luggages, places, minors


if __name__ == "__main__":
    x_dim = 6
    y_dim = 20
    exit_rows = [3, 7]
    luggages, places, minors = generate_places(x_dim, y_dim, exit_rows, 10)
    plane = Plane(x_dim=x_dim, y_dim=y_dim, exit_rows=exit_rows,
                  luggages=luggages,
                  places=places,
                  minors=minors)
    while not plane.done:
        plane.display()
        plane.act_on_intentions()
    plane.display()
