nums = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

smallest = []
small = 0
total = 0
# get smallest in each array
# add smallest together
for num in nums:
    small = num[0]  # start with first numbver
    for i in range(1, len(num)):  # start point and stop point
        if small > num[i]:
            small = num[i]
    total += small

print(total)
