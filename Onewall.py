def funcOne():
    num = float(input("Enter Depth: "))
    sum = 0
    benches = 0
    remainder = num % 4
    while num >= 4:
        benches += 1
        sum += num
        num -= 4
    sum += remainder
    area = float(input("enter length: ")) * 4 * benches
    volume_cy = (area / benches) * sum / 27
    print(f"""
           It will take {benches} benches to reach above depth
           the total depth is: {sum}
           the total area of work will be {area}SF
           the volume is {volume_cy}CY""")