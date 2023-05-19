import re


class errorInputArith(Exception):
    pass


def check_problems_format(problem):
    """Check errors in a single string, no errors will return None"""

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
        raise errorInputArith("Error: Operator must be '+' or '-'.")
    if re_match(re_error["nonDigitsError"]):
        raise errorInputArith("Error: Numbers must only contain digits.")
    if re_match(re_error["longerDigitsError"][0]) or re_match(
        re_error["longerDigitsError"][1]
    ):
        raise errorInputArith("Error: Numbers cannot be more than four digits.")


def format_problem_lines(line_list, get_result=False):
    """gets a list of splitted problems and return a
    ready to print string, it will return the operation result as well"""
    # this will be used to join the final strings
    separator = "    "
    # define functions for the defined operations
    ops = {"+": lambda x, y: int(x) + int(y), "-": lambda x, y: int(x) - int(y)}

    lines = {"line1": [], "line2": [], "line3": [], "result": list()}
    # the string list format will be:
    # [number 1, operator, number 2]
    for num1, op, num2 in line_list:
        if get_result:
            solved = str(ops[op](num1, num2))

        # this will take the actual defined lenght
        # in the current iteration
        num_length = 0
        if len(num1) >= len(num2):
            # now both numbers have the same length
            num2 = num2.rjust(len(num1))
            # add the operator the second number
            num2 = f"{op} {num2}"
            # define the num_length cause it could be
            # needed to justify the result
            num_length = len(num2)
            # justify the number 1 with the modified number 2
            # and it's currently stored in num_length
            num1 = num1.rjust(num_length)
            # add the digits to their corresponding line
            lines["line1"].append(num1)
            lines["line2"].append(num2)
            # create the dashed separator
            lines["line3"].append("-" * num_length)

        else:
            # add the operator to number 2
            num2 = f"{op} {num2}"
            # define the num_length cause it could be
            # needed to justify the result
            num_length = len(num2)
            # justify number 1 to the modified number 2
            num1 = num1.rjust(num_length)
            # add the digits to their corresponding line
            lines["line1"].append(num1)
            lines["line2"].append(num2)
            # create the dashed separator
            lines["line3"].append("-" * num_length)

        if get_result:
            # add the result to the dictionary and justify it with
            # the current number length
            lines["result"].append(solved.rjust(num_length))

    for k in lines:
        lines[k] = separator.join(lines[k])

    # define if the result will be printed or not
    if get_result:
        return "{}\n{}\n{}\n{}".format(
            lines["line1"], lines["line2"], lines["line3"], lines["result"]
        )
    else:
        return "{}\n{}\n{}".format(lines["line1"], lines["line2"], lines["line3"])


def arithmetic_arranger(problems, get_result=False):
    # check errors
    if len(problems) > 5:
        return "Error: Too many problems."
    # loop trying to find an error and return it
    for problem in problems:
        try:
            check_problems_format(problem)
        except errorInputArith as error:
            return str(error)

    # main solution

    # split the problem parameters
    splitted_probl = [x.split() for x in problems]
    # get formatted lines
    lines = format_problem_lines(splitted_probl, get_result)

    return lines


if __name__ == "__main__":
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
