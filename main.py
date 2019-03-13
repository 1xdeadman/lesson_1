import random

def gen_new_file(dir, hour, is_empty=False):

    node_name = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "elem_1",
        "elem_2",
        "elem_3",
        "elem_4",
        "elem_5",
        "elem_6"
    ]
    # add garbage
    garbage_count = random.randint(0, 6)
    for _ in range(garbage_count):
        trash_values = []
        for _ in range(2):
            trash_values.append(str(random.getrandbits(random.randint(1,15))))
        garbage = trash_values[0] + "garbage" + trash_values[1]
        node_name.append(garbage)

    # add empty rows
    if is_empty:
        empty_count = random.randint(1, 5)
        for _ in range(empty_count):
            node_name.append(None)

    filename = "log_(" + "Thu, 12 Mar 2019 " + str(hour) + ":22:00).txt"

    with open(dir + filename ,"w", encoding="utf-8") as ff:
        while len(node_name) != 0:
            elem_index = random.randint(0, len(node_name) - 1)
            elem = node_name[elem_index]
            del(node_name[elem_index])
            printed_row = ""
            if elem is not None:
                printed_row = str(random.randint(1,20)) + ":" + elem + ":" + str(random.getrandbits(10))
            ff.write(printed_row + "\n")


start = 11
end = 22


def is_empty_hour(hour, start, end):
    for _ in range(5):
        if hour == random.randint(start,end):
            return True
    return False


for hour in range(start, end):
    is_empty = is_empty_hour(hour, start, end)
    gen_new_file("logs/", hour, is_empty)