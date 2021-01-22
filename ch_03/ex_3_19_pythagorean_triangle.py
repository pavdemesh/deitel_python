"""Find all Pythagorean triangles for sides and hypotenuse all no larger than 20"""

known_hypotenuse = list()

for side1 in range(1, 21):
    for side2 in range(1, 21):
        for hypotenuse in range(1, 21):
            if side1 < hypotenuse and side2 < hypotenuse:
                if side1 ** 2 + side2 ** 2 == hypotenuse ** 2:
                    if hypotenuse not in known_hypotenuse:
                        print(f"Valid combination: {side1}, {side2}, {hypotenuse}")
                        known_hypotenuse.append(hypotenuse)
