from main import *

run_cases = [
    (
        [
            ("push", {"name": "Alice", "role": "Developer"}),
            ("push", {"name": "Bob", "title": "CTO"}),
            ("size", None),
        ],
        2,
    ),
    (
        [
            ("push", {"name": "Charlie", "company": "TechCorp"}),
            ("push", {"name": "Diana", "skills": "Python"}),
            ("push", {"name": "Ethan", "role": "Manager"}),
            ("size", None),
        ],
        3,
    ),
]

submit_cases = run_cases + [
    (
        [
            ("size", None),
        ],
        0,
    ),
    (
        [
            ("push", {"name": "Frank", "experience": "5 years"}),
            ("push", {"name": "Grace", "education": "MBA"}),
            ("push", {"name": "Henry", "location": "New York"}),
            ("push", {"name": "Ivy", "industry": "Finance"}),
            ("size", None),
        ],
        4,
    ),
    (
        [
            ("push", {"name": "Jack", "connections": 500}),
            ("size", None),
            ("push", {"name": "Kelly", "endorsements": 50}),
            ("size", None),
        ],
        2,
    ),
]


def test(operations, expected_output):
    print("---------------------------------")
    stack = Stack()
    result = None
    for op, value in operations:
        if op == "push":
            print(f"Push: {value}")
            stack.push(value)
        elif op == "size":
            result = stack.size()

    print(f"Expecting size: {expected_output}")
    print(f"Actual size: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
