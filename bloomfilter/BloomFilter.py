import pyhash

bit_vector = [0] * 20

# non cryptographic hash functions murmur() and FNV()
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()


# calculate the output of FNV and Murmur hash function for d and Charmander
fnv_pika  = fnv('Pickachu')%20
fnv_char  = fnv('Charmander')%20

murmur_pika  = murmur('Pickachu')%20
murmur_char  = murmur('Charmander')%20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1

bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1

# A wild Bulbusaur

fnv_bulb  = fnv('Bulbusaur')%20
murmur_bulb  = murmur('Bulbusaur')%20

print(bit_vector[fnv_bulb])
print(bit_vector[murmur_bulb])