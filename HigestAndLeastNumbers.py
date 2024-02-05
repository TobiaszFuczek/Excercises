#Znajdowanie Największej i Najmniejszej Liczby
#Napisz funkcję, która pobiera listę liczb od użytkownika i zwraca największą i najmniejszą liczbę w tej liście.
#Złap błąd, jeśli użytkownik wpisze coś innego niż liczby.

def look_for_numbers():
    numbers = []

    try:
        input_data = input("Enter numbers, separated by space or comma: ")
        elements = input_data.replace(",", " ").split()
        numbers = [float(element) for element in elements]
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"List of numbers: {numbers}")

    highest_value = max(numbers)
    lowest_value = min(numbers)

    print(f"The Highest Value in the List is: {highest_value}")
    print(f"The Lowest Value in the List is: {lowest_value}")

look_for_numbers()