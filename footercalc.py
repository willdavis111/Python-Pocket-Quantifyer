def funcThree():
    print(""
"Please enter '0' in all fields when all footers have been entered")
    repeater = True
    bfint_total = 0
    bfext_total = 0
    exvol_total = 0
    while repeater:
        footer_depth = float(input("Footer Depth: "))
        if footer_depth == 0:
            repeater = False
        footer_width = float(input("Footer Width: "))
        footer_hieght = float(input("Footer Height: "))
        footer_wall = float(input("Footer Wall: "))
        footer_length = float(input("Footer Length: "))
        interior_depth = float(input("Interior Depth: "))
        ex_vol = footer_length * footer_depth * footer_width
        interior_delta = footer_depth - interior_depth
        bf_exterior = ((footer_depth - footer_hieght) * (footer_width - footer_wall) / 2) * footer_length
        if interior_delta != 0:
            bf_interior = bf_exterior + (bf_exterior - ((interior_delta * ((footer_width - footer_wall) / 2)) * footer_length))
        elif interior_delta == 0:
            bf_interior = bf_exterior
        bfint_total += bf_interior
        bfext_total += bf_exterior
        exvol_total += ex_vol

    
    print(f"""
Total Excavation: {exvol_total / 27} CY
Total Interior Back Fill: {bfint_total / 27} CY
Total Exterion Back Fill: {bfext_total / 27} CY
Total Back Fill: {(bfint_total + bfext_total) / 27} CY""")