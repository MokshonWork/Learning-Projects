def arithmetic_arranger(problems, display_answers=False):
    """
    Arranges arithmetic problems vertically and side-by-side.

    Args:
        problems (list): A list of strings, where each string is an arithmetic problem.
                         Example: ["32 + 698", "3801 - 2"]
        display_answers (bool, optional): If True, the answers to the problems
                                          will be displayed. Defaults to False.

    Returns:
        str: The problems arranged vertically, or an error message if the
             input problems do not meet the specified rules.
    """

    # Rule 1: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists to store parts of each line for easy joining later
    first_operands = []
    operators_and_second_operands = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        # Check for correct number of parts (operand1, operator, operand2)
        if len(parts) != 3:
            # This case should ideally be caught by other specific error checks,
            # but it's a good general sanity check for malformed strings.
            # However, the problem statement doesn't explicitly mention this error.
            # Sticking to specified errors.
            pass

        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # Rule 2: Operator must be '+' or '-'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Rule 3: Numbers must only contain digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Rule 4: Numbers cannot be more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width for the current problem block
        # This is the length of the longest operand + 2 (for operator and space)
        width = max(len(operand1), len(operand2)) + 2

        # Format the first operand (top number)
        first_operands.append(operand1.rjust(width))

        # Format the second operand (bottom number with operator)
        operators_and_second_operands.append(operator + operand2.rjust(width - 1))

        # Format the dashes line
        dashes.append("-" * width)

        # Calculate answer if display_answers is True
        if display_answers:
            num1 = int(operand1)
            num2 = int(operand2)
            if operator == '+':
                result = str(num1 + num2)
            else:
                result = str(num1 - num2)
            answers.append(result.rjust(width))

    # Join the collected parts for each line with four spaces between problems
    arranged_output = []
    arranged_output.append("    ".join(first_operands))
    arranged_output.append("    ".join(operators_and_second_operands))
    arranged_output.append("    ".join(dashes))

    if display_answers:
        arranged_output.append("    ".join(answers))

    # Return the final multi-line string
    return "\n".join(arranged_output)

