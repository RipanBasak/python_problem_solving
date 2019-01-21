#! /usr/bin/python
import handle_person_objects


def test_print_depth():
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": {
                    "firstname":"user",
                    "lastname":"2",
                    "fathername":"user"
                }
            }
        }
    }

    result = handle_person_objects.print_depth(a)
    print(result)
    # assert 0
