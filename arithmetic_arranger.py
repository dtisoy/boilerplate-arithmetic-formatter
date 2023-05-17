import re


def check_problems_format(problem):
    """this function is made to track errors if
    not error finded just raise an error with no error message"""

    # I dont want to repeat re.search all the time
    # i tried with def re_match but does not work
    re_match = lambda x: re.search(x, problem)
    # regular expressions
    # stands for regular expression errors
    re_error = {
        "operatorError": "[+-]",
        "nonDigitsError": "[a-zA-Z]",
        "longerDigitsError": [r"^\S{5,}", r"\S{5,}$"],
    }

    """I resolved to use just ifs because after a return
    the code will exit"""
    if not re_match(re_error["operatorError"]):
        return "Error: Operator must be '+' or '-'."
    if re_match(re_error["nonDigitsError"]):
        return "Error: Numbers must only contain digits."
    if re_match(re_error["longerDigitsError"][0]) or re_match(
        re_error["longerDigitsError"][1]
    ):
        return "Error: Numbers cannot be more than four digits."


def test_all_error_cases(problems):
    # checking input errors
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        return check_problems_format(problem)


def main_logic(problems, result):
    ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y}
    splited = list()
    # split all the strings word by word
    for word_string in problems:
        splited.append(word_string.split())
    # compare the length of the numbers
    # the number indexes are 0 and 2
    thirdline = list()  # this is for the dashes

    fourthline = list()  # this is arithmetic operation

    for item in splited:
        if result:
            fourthline.append(str(ops[item[1]](int(item[0]), int(item[2]))))
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
    if result:
        for index in range(len(thirdline)):
            fourthline[index] = fourthline[index].rjust(len(thirdline[index]))

    separator = "    "
    firsline = separator.join(firsline)
    secondline = separator.join(secondline)
    thirdline = separator.join(thirdline)
    fourthline = separator.join(fourthline)
    if result:
        return f"{firsline}\n{secondline}\n{thirdline}\n{fourthline}"
    return f"{firsline}\n{secondline}\n{thirdline}"


def arithmetic_arranger(problems, result=False):
    # check errors
    if test_all_error_cases(problems):
        return test_all_error_cases(problems)

    # main soluction
    return main_logic(problems, result)


if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
