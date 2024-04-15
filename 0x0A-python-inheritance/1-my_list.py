#!/usr/bin/python3
class MyList(list):
    """A custom list class inheriting from the built-in list class."""

    def print_sorted(self):
        """Print the elements of the list sorted in ascending order."""
        sortedlist = sorted(self)
        print(sortedlist)
