from main1 import Stack

run_cases = [
    (
        [
            ("push", {"name": "Alice", "role": "Developer"}),
            ("push", {"name": "Bob", "role": "Designer"}),
            ("size", None),
            ("peek", None),
            ("pop", None),
            ("size", None),
        ],
        [
            None,
            None,
            2,
            {"name": "Bob", "role": "Designer"},
            {"name": "Bob", "role": "Designer"},
            1,
        ],
    ),
    (
        [
            ("push", {"name": "Charlie", "company": "TechCorp"}),
            ("push", {"name": "David", "skills": ["Python", "JavaScript"]}),
            ("pop", None),
            ("pop", None),
            ("pop", None),
        ],
        [
            None,
            None,
            {"name": "David", "skills": ["Python", "JavaScript"]},
            {"name": "Charlie", "company": "TechCorp"},
            None,
        ],
    ),
]

submit_cases = run_cases + [
    (
        [
            ("push", {"name": "Eve", "role": "Manager", "years": 5}),
            ("peek", None),
            ("push", {"name": "Frank", "role": "DevOps"}),
            ("size", None),
            ("pop", None),
            ("pop", None),
            ("pop", None),
        ],
        [
            None,
            {"name": "Eve", "role": "Manager", "years": 5},
            None,
            2,
            {"name": "Frank", "role": "DevOps"},
            {"name": "Eve", "role": "Manager", "years": 5},
            None,
        ],
    ),
]


def visualize_stack(stack):
    if not stack:
        return "- (empty)"
    return "\n".join(
        [f"    - {item['name']}: {list(item.values())[1]}" for item in reversed(stack)]
    )


def test(operations, expected_outputs):
    print("---------------------------------")
    stack = Stack()
    actual_outputs = []

    for i, (op, value) in enumerate(operations):
        print(f"Operation {i + 1}:")
        if op == "push":
            print(f"  Push: {value}")
            actual_outputs.append(stack.push(value))
        elif op == "pop":
            result = stack.pop()
            print(f"  Pop: {result}")
            actual_outputs.append(result)
        elif op == "peek":
            result = stack.peek()
            print(f"  Peek: {result}")
            actual_outputs.append(result)
        elif op == "size":
            result = stack.size()
            print(f"  Size: {result}")
            actual_outputs.append(result)

        print(f"  Stack:\n{visualize_stack(stack.items)}")
        print()

    print(f"Expected outputs: {expected_outputs}")
    print(f"Actual outputs: {actual_outputs}")
    if actual_outputs == expected_outputs:
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
