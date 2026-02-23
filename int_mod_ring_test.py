from int_mod_ring import int_mod_ring
import time

z_test = int_mod_ring(12)
print(z_test.to_list())
print(z_test.addition_table())
print()
print(z_test.multiplication_table())

# for i in range(2, 1000):
#     print(f"Z mod {i}: ", end="") 
#     start = time.time()
#     ring = int_mod_ring(i).to_list()
#     end = time.time()
#     print(ring)
#     print(f"Took {end} - {start} = {end - start}s")

# This takes over a minute on my machine
# BIG_NUM = 1000000000
# print(f"Z mod {BIG_NUM}: ", end="") 
# start = time.time()
# ring = int_mod_ring(BIG_NUM).to_list()
# end = time.time()
# print(f"Took {end} - {start} = {end - start}s")