x, y, z = 0, 1, 0

# these test for specifically if the value is 1
if x == 1 or y == 1 or z == 1:
    print("passed")

if 1 in (x, y, z):
    print("passed")

# these test for True(1) or False(0)
if x or y or z:
    print("passed")

if any((x, y, z)):
    print("passed")

if any([x, y, z]):
    print("passed")
