"""
This program calculates prime numbers and saves them to disk.
"""

def is_prime(n):

    for d in range(2, floor(sqrt(n)), 2):

        if n % d == 0:
            return False

    return True

save_period = 100000
primes = []
calculate = True

if calculate:

    for n in count():
        # count increments n by 1 starting from 0, indefinitely
        # You can cancel the program at any time by hitting the red square next to the green play button
        if is_prime(n):
            primes.append(n)

        if len(primes) % save_period == 0:
            np.save(f"primes_starting_from_{primes[0]}", primes)

else:
    # The following will retrieve the saved primes.
    saved_primes = []

    for f in Path(".").glob("primes_*.py"):
        saved_primes.extend(np.load(f))



