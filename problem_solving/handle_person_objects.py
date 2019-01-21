#! /usr/bin/python

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

        # print(self.first_name, self.last_name, self.father)
    def retDict(self):
        # print( {'first_name': self.first_name, 'last_name': self.last_name, 'father': self.father})
        return ( {'first_name': self.first_name, 'last_name': self.last_name, 'father': self.father})


# def process_date():
#     person_a = Person("User", "1", None)
#     person_b = Person("User", "2", person_a.retDict())
#
#     a = {
#         "key1": 1,
#         "key2": {
#             "key3": 1,
#             "key4": {
#                 "key5": person_b.retDict()
#             }
#         }
#     }
#     return a
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a.retDict())

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": person_b.retDict()
        }
    }
}
def print_dict(data, level = 1):
    #all logic will be here
    for k, v in sorted(data.items()):
        if isinstance(v, dict):
            print("{0} : {1}".format(k, level))
            print_dict(v, level+1)
        else:
            print("{0} : {1}".format(k, level))


def print_depth(data):
    print_dict(data, level=1)


print_depth(a)