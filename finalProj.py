import random
import sympy 

# Set numprimes to a lower number for it to run in a reasonable amount of time.
numPrimes = 100000
# Vary seed bits to see how range of seed values affects collisions.
seedBits = 26
primeBits = 512

def generatePrime():
    random.seed()
    random.seed(random.randint(2**(seedBits - 1), (2**seedBits)-1))
    attempt = random.randint(2**(primeBits-1), (2**primeBits)-1)
    if attempt % 2 == 0:
        attempt += 1
    while not sympy.isprime(attempt):
        attempt += 2
    return attempt


primes = set()
collisionCount = 0
for i in range(numPrimes):
    prime = generatePrime()
    if prime in primes:
        collisionCount += 1
    else:
        primes.add(prime)
    print(i)

print("Generated " + str(numPrimes) + " " + str(primeBits) + "-bit primes")
print(str(seedBits) + "-bit seeds used.")
print("Number of collisions: " + str(collisionCount))



