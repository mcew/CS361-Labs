#Tom Green


#---------------------------------------
class Set:

    #---------------------------------------
    def __init__(self):
        """
        :param: None

        """

        self.items = []
        self.length = 0

    #---------------------------------------

    def insert(self, item):
        """ Adds an item to the Set

        :param: item: any object, string or numerical value

        """

        self.items.append(item)
        self.length += 1

    #---------------------------------------

    def contains(self, seek):
        """Returns True if parameter "seek" within the set, otherwise False.

        :param: An item that might or might not exist within the set.

        :return: True of False
        """

        #compares each item within the set with "seek" parameter, returns True for first match, otherwise False
        for item in self.items:
            if item == seek:
                return True
        return False

    #---------------------------------------

    def isSubsetOf(self, other):
        """Returns True if set parameter is within the greater set, otherwise False.

        :param: set: Set

        :return: True or False
        """

        falses = 0
        while falses == 0:
            for item in other.items:
                if item in self.items:
                    pass
                else:
                    falses += 1
            return True
        return False

    #---------------------------------------

    def __len__(self):
        """Returns the number of items in the set

        pre: object has items
        post: returns # of items."""

        #outputs length of object accumulated by insert method
        return self.length

    #---------------------------------------

    def __add__(self, other):
        """operator

        pre: self and other are set objects
        post: a new set containing all the values of self and other"""

        #since both self and other should be lists, the combine with +
        nuSet = self.items + other.items
        set3 = Set()
        for item in nuSet:
            set3.insert(item)
        return set3

    #---------------------------------------

    def __sub__(self, other):
        """operator

        pre: self and other are set objects
        post: a new set with items from other subtracted from items of self"""

        nuSet = self.items
        for item in other.items:
            if item in nuSet:
                self.items.remove(item)
            else:
                pass
        set3 = Set()
        for i in nuSet:
            set3.insert(i)
        return set3


    #---------------------------------------

    def __eq__(self, other):
        """operator

        pre: self and other are set objects
        post: True if self and other are the same, False otherwise"""

        if len(self) == len(other):
            index = 0
            falses = 0
            while falses == 0:
                for item in self.items:
                    if item == other.items.index(index):
                        index += 1
                    else:
                        falses += 1
                return True
        return False


    #---------------------------------------

    def __ne__(self, other):
        """operator

        pre: self and other are set objects
        post: True if self and other are different, False otherwise"""

        if len(self) == len(other):
            index = 0
            falses = 0
            while falses == 0:
                for item in self.items:
                    if item == other.items.index(index):
                        index += 1
                    else:
                        falses += 1
                return False
        return True

    #---------------------------------------