paranthesis_map = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}


def peek(stack):
    if len(stack) == 0:
        return None
    else:
        return stack[-1]

def is_balanced_parentheses(test_string):
    stack = []
    closing_parenthesis = list(paranthesis_map.values())
    opening_parenthesis = list(paranthesis_map.keys())
    print(opening_parenthesis)
    print(closing_parenthesis)
    if test_string and test_string[0] in closing_parenthesis:
        return False
    else:
        for st in test_string:
            if st in opening_parenthesis:
                stack.append(st)
            elif st in closing_parenthesis:
                previous_opening_parenthesis = peek(stack)
                if previous_opening_parenthesis and paranthesis_map[peek(stack)] == st:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()