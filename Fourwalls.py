def funcTwo():
    depth = float(input("Depth: "))
    length = float(input("Length: "))
    width = float(input("Width: "))
    depthes = [depth]
    areas = []
    depth_count = 0
    remainder = depth % 4
    while depth >= 4:
        depth_count += 1
        depth -= 4
        depthes.append(depth)
    depthes[depth_count] = remainder

    for items in depthes:
        arae = length * width
        length += 4
        width += 4
        new_area = length * width - arae
        areas.append(new_area)

    volumes = []
    count = 0
    for items in depthes:
        count += 1
        for area in areas:
            vol = items * area
            volumes.append(vol)

    list = volumes[0::count + 1]
    sum = 0
    for i_vol in list:
        sum += i_vol

    print(f"""
areas of work: {areas}
depths: {depthes}
Total Volume: {(sum / 27)} CY""")