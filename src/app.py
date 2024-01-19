def main(range_to: int) -> list:
    output = []
    for i in range(1, range_to + 1):
        if i == 3:
            output.append("Cazoo!")
        else:
            output.append(i)

    return output