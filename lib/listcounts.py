
def min(Lista):

    """
    :param List: A list of only integers
    :return: The lowest integer in the list
    """
    LowN = Lista[1]
    for number in Lista:
        if LowN > number:
            Lown = number
    return Lown

def max(Lista):

    """
    :param List: A list of only integers
    :return: The highest integer in the list
    """
    HighN = Lista[1]
    for number in Lista:
        if HighN < number:
            HighN = number
    return HighN

def average(Lista):
    """
    :param Lista: A list of only integers
    :return: The average value of the lists content rounded to integer.
    """
    listlengt = 0
    listtot = 0
    for number in Lista:
        listlengt += 1
        listtot += number
    return listtot/listlengt


Random_numbers = [4,7,88,37,98,555,-5, 4, 37.6, -1337]

print min(Random_numbers)

print max(Random_numbers)

print average(Random_numbers)
