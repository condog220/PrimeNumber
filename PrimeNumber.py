# Range from 1-100
for number in range(0, 99):
    # Prime number is always divisable by itself, therefore check it is greater than or equal to 2.
    if number >= 2:
        # Our divisor; will go through the loop and MOD number by i
        for i in range(2, number):
            if number % i == 0:
                # If any manage to be divisable with no remainder, number is not prime. Break
                break
        else:
            # Print number as it is prime.
            print(number)
