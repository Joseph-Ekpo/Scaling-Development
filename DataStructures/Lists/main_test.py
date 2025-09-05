from main import *

run_cases = [
    (["Software Engineer", "Data Analyst", "Project Manager"], "Project Manager"),
    (["Intern", "Junior Developer"], "Junior Developer"),
]

submit_cases = run_cases + [
    ([], None),
    (["CEO"], "CEO"),
    (["Cashier", "Supervisor", "Manager", "Director"], "Director"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input work experiences: {input1}")
    print(f"Expected output: {expected_output}")
    result = last_work_experience(input1)
    print(f"Actual output: {result}")
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
