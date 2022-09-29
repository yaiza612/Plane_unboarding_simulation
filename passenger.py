import math


class Passenger:
    """ Create a new passenger of the object Plane"""

    def __init__(self, statement, place, minor):
        """
        :param statement: Is a True/False statement indicating if the passenger needs to take his luggage
        :param place: Represent the coordinates in the object Plane (x,y)
        :param minor: Is a True/False statement indicating if the passenger is underage or not
        """
        self.intention = None
        self.needs_luggage = statement
        self.place = place
        self.minor = minor

    def intend(self, row_size, exits):
        """
        Function to obtain the intention of the passenger
        :param row_size: size of places in each side of the object plane
        :param exits: list of exists (columns in the object plane)
        :return: desired place for the passenger
        """
        sign = lambda x: math.copysign(1, x)
        on_aisle = (row_size + 1, self.place[1])
        if on_aisle != self.place:
            desired_place = (int(self.place[0] + sign((row_size - self.place[0]))), self.place[1])
        else:
            if self.needs_luggage:
                desired_place = (row_size+1, self.place[1])
            else:
                take_closest = lambda num, collection: min(collection, key=lambda x: abs(x - num))
                desired_exit = take_closest(self.place[1], exits)
                desired_place = (row_size+1, int(self.place[1]+sign((desired_exit[1])-self.place[1])))
        return desired_place

    def collect_intention(self, row_size, exits):
        """
        Collecting the desired place in the object Passenger
        :param row_size: size of places in each side of the object plane
        :param exits: list of exists (columns in the object plane)
        :return: self.intention
        """
        if self.intention is None:
            self.intention = self.intend(row_size, exits)
        return self.intention

    def act(self, exits):
        """
        Actualizing the object Passenger with their actions.
        :return: After actualizes check need_luggage or not and return True if left the plane, otherwise
        return False and give again the value None to intention of the object Passenger.
        """
        if self.intention != self.place:
            self.place = self.intention
            if self.place[1] in exits:
                return True
        else:
            self.needs_luggage = False
        self.intention = None
        return False


if __name__ == "__main__":
    p1 = Passenger(True, (0, 1), True)
    print(p1.needs_luggage)
    print(p1.place[1])
    print(p1.minor)
    print(p1.intend(3,1))

