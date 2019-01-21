#! /usr/bin/python
import dictionary_print_depth


def test_print_depth():
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    #def print_test_dict(data, level = 1, key = None, depth_of_key =1)

    result = dictionary_print_depth.print_test_dict(a, level = 1, key = "key1", depth_of_key =1)
    # print(result)
    assert result == 1
