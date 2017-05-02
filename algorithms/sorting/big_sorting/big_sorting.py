class Number:
    def __init__(self, number_string):
        self.number_string = number_string
        self.length = len(number_string)

    def __lt__(self, other):
        if self.length < other.length:
            return True
        elif self.length > other.length:
            return False
        else:
            return int(self.number_string) < int(other.number_string)

n = int(input().strip())

unsorted = []
for i in range(n):
    number = Number(input().strip())
    unsorted.append(number)

# your code goes here
print('\n'.join([x.number_string for x in sorted(unsorted)]))
