from interval import interval

# Test basic construction
x1 = interval(0, 0, 0, 1)
print(x1.disp_bounds())

for a in [-1, 0, 0.25, 1/3, 0.5, 2/3, 0.75, 0.999999, 1, 1.01]:
    print(f"a = {a} is in x1: {x1.contains(a)}")
    
print()
x2 = interval(1, 1, 0, 1)
print(x2.disp_bounds())

for a in [-1, 0, 0.25, 1/3, 0.5, 2/3, 0.75, 0.999999, 1, 1.01]:
    print(f"a = {a} is in x2: {x2.contains(a)}")

# Test contains method with regards to Python precision
for i in range(1, 21):
    num = float("0." + i * "9")
    print(f"({i} digit(s)): {num} in {x1.disp_bounds()}: {x1.contains(num)}")

# Test bounds checking
x1.set_bounds(5, 0)
print(x1.disp_bounds())
