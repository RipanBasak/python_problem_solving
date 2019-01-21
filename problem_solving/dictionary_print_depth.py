#! /usr/bin/python

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}
# testing methods

def print_test_dict(data, level = 1, key = None, depth_of_key =1):

    for k, v in sorted(data.items()):

        if isinstance(v, dict):
            if k == key and level == depth_of_key:
                return depth_of_key

            print_test_dict(v, level+1, key, depth_of_key)
        else:
            if k == key and level == depth_of_key:
                return depth_of_key




def print_dict(data, level = 1):
    for k, v in sorted(data.items()):

        # return ("{0} : {1}".format(k, level) if not isinstance(v, dict) else "{0} : {1}".format(k, level) )
        if isinstance(v, dict):
            print("{0} : {1}".format(k, level))
            print_dict(v, level+1)
        else:
            print("{0} : {1}".format(k, level))


def print_depth(data):
    print_dict(data, level=1)




print_depth(a)
# print_test_dict(a, level = 1, key = 'key3', depth_of_key =2)
