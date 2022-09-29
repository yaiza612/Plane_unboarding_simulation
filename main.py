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
from passenger import Passenger

if __name__ == "__main__":
    plane = Plane(x_dim=6, y_dim=10, exit_rows=[3, 7],
                  luggages=[True, False],
                  places=[(2, 5), (5, 4)],
                  minors=[False, False])
    plane.display()
    plane.act_on_intentions()
    plane.display()
    plane.act_on_intentions()
    plane.display()
