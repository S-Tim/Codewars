"""
Direction Reduction

Once upon a time, on a way through the old wild west,…

… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST".
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite
direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important
to save yourself some energy, otherwise you might die of thirst!

Task

Write a function dirReduc which will take an array of strings and returns an array of strings with the needless
directions removed (W<->E or S<->N side by side).
"""

def dirReduc(arr):
    """Simplifies the directions in the Array

        Directions can be NORTH, SOUTH, WEST and EAST.
        Opposite directions that are side by side cancel
        each other out.
    """
    simplified = True

    while simplified:
        simplified = False

        if len(arr) < 2:
            break

        for i in range(len(arr) - 1):
            if areOpposite(arr[i], arr[i+1]):
                del arr[i]
                del arr[i]
                simplified = True
                break
    
    return arr

def areOpposite(dir1, dir2):
    """Tests whether the two given directions are opposite"""
    direction_set = {dir1, dir2}

    if len(direction_set) < 2:
        return False

    if direction_set.issubset({"WEST", "EAST"}):
        return True

    if direction_set.issubset({"NORTH", "SOUTH"}):
        return True

    return False

a = ["NORTH", "NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
a = dirReduc(a)
