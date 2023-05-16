def arithmetic_arranger(problems):

    # main soluction
    splited = list()
    # split all the strings
    for word_string in problems:
        splited.append(word_string.split())
    # compare the length of the numbers
    # the number indexes are 0 and 2
    thirdline = list()

    for item in splited:
        if len(item[0]) > len(item[2]):
            item[2] = item[2].rjust(len(item[0]))
            item[0] = f"  {item[0]}"
            thirdline.append("-" * len(item[0]))
        else:
            # here I should add 2 spaces for de + character
            item[0] = item[0].rjust(len(item[2]) + 2)
            thirdline.append("-" * len(item[0]))

        item[1] = f"{item[1]} {item.pop(2)}"

    firsline = [x[0] for x in splited]
    secondline = [x[1] for x in splited]

    separator = "    "
    firsline = separator.join(firsline)
    secondline = separator.join(secondline)
    thirdline = separator.join(thirdline)
    print(f"{firsline}\n{secondline}\n{thirdline}")
    return f"{firsline}\n{secondline}\n{thirdline}"


if __name__ == "__main__":
    arithmetic_arranger(
        ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
    )
