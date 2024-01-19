def main(range_to: int) -> list:
    output = []
    for i in range(1, range_to + 1):
        if i % 3 == 0:
            output.append("Cazoo!")
        elif i % 5 == 0:
            output.append("Yeah!")
        else:
            output.append(i)

    return output
