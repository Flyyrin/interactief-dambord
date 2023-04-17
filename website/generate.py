num = 64
row = 0
for x in range(8):
    for y in range(8):
        num += 1
        print(f'<rect id="{num}" width="250" height="250" rx="65" ry="65" transform="matrix(0.75 0 0 0.75  {y*250 +35} {x*250 +35})"  fill="#00000000" filter="url(#glow)"/>')