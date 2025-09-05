from main import Queue

run_cases = [
    (
        [("push", "Rand"), ("push", "Mat"), ("peek", None), ("pop", None)],
        ["Rand", "Rand"],
    ),
    (
        [
            ("push", "Egwene"),
            ("push", "Nynaeve"),
            ("size", None),
            ("pop", None),
            ("size", None),
        ],
        [2, "Egwene", 1],
    ),
]

submit_cases = run_cases + [
    ([("pop", None), ("peek", None), ("size", None)], [None, None, 0]),
    (
        [
            ("push", "Perrin"),
            ("push", "Moiraine"),
            ("push", "Lan"),
            ("pop", None),
            ("pop", None),
            ("peek", None),
        ],
        ["Perrin", "Moiraine", "Lan"],
    ),
    (
        [("push", "Thom"), ("pop", None), ("push", "Loial"), ("peek", None)],
        ["Thom", "Loial"],
    ),
]


def visualize_queue(queue):
    if not queue.items:
        return "Queue is empty"
    return "\n".join([f"- {item}" for item in reversed(queue.items)])


def test(operations, expected_outputs):
    print("---------------------------------")
    queue = Queue()
    outputs = []
    for op, value in operations:
        if op == "push":
            queue.push(value)
            print(f"Push: {value}")
        elif op == "pop":
            result = queue.pop()
            outputs.append(result)
            print(f"Pop: {result}")
        elif op == "peek":
            result = queue.peek()
            outputs.append(result)
            print(f"Peek: {result}")
        elif op == "size":
            result = queue.size()
            outputs.append(result)
            print(f"Size: {result}")

        print("\nQueue state:")
        print(visualize_queue(queue))
        print()

    print(f"Expected: {expected_outputs}")
    print(f"Actual: {outputs}")
    if outputs == expected_outputs:
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
