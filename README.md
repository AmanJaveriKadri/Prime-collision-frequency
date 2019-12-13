# Prime-collision-frequency
Testing frequency of collisions in RSA public key generation with constraints. (Specifically with varying bit-length of seed used for random prime generation.)
A simple program that generates n number of prime numbers with specified number of bits using random seeds of specified number of bits and checks how often collisions occur. This gives a rough estimate of what percentage of public keys generate with a particular bit-length of seeds would be insecure due to shared factors with other public keys.
