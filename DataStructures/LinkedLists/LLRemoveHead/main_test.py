from main import *

run_cases = [
    (
        ["Rick", "Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        (["Cliff", "Sharon", "Jay", "Roman", "Squeaky"], "Rick", "Squeaky"),
    ),
    (
        ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        (["Sharon", "Jay", "Roman", "Squeaky"], "Cliff", "Squeaky"),
    ),
]

submit_cases = run_cases + [
    ([], ([],)),
    (["Jay"], ([], "Jay")),
    (["Roman", "Squeaky"], (["Squeaky"], "Roman", "Squeaky")),
    (["Squeaky"], ([], "Squeaky")),
]


def test(linked_list, expected_state, expected_head=None, expected_tail=None):
    print("---------------------------------")
    print(f"Linked List Queue: {linked_list}")
    print(f"Removing Head...\n")
    try:
        head = linked_list.remove_from_head()
        tail = linked_list.tail
        result = linked_list_to_list(linked_list)
        print(f"Expected List: {expected_state}")
        print(f"  Actual List: {result}\n")
        if result != expected_state:
            print("Fail")
            return False
        print(f"Expected Removed Head: {expected_head}")
        print(f"  Actual Removed Head: {head}\n")
        if not (head == None and expected_head == None) and (head.val != expected_head):
            print("Fail")
            return False
        print(f"Expected Tail: {expected_tail}")
        print(f"  Actual Tail: {tail}\n")
        if not (tail == None and expected_tail == None) and (tail.val != expected_tail):
            print("Fail")
            return False
        if head != None:
            print("Expected Removed Head's Next Node: None")
            print(f"         Actual Removed Head Next: {head.next}\n")
            if head.next != None:
                print("Fail")
                return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Exception: {str(e)}")
        print("Fail")
        return False


def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)

    return result


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        linked_list = LLQueue()
        for item in test_case[0]:
            linked_list.add_to_tail(Node(item))
        correct = test(linked_list, *test_case[1])
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
