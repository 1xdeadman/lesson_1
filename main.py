import time
import random

node_name = [
    "a",
    "b",
    "c",
    "garbage_1",
    "d",
    "e",
    "f",
    "g",
    "(garbage_2)",
    "elem_1",
    "elem_2",
    "elem_3",
]

def gen_new_file(dir, hour):
    filename = "log_" + "Thu, 12 Mar 2019 " + str(hour) + ":22:00"

    with open(dir + filename ,"w") as ff:
        for elem in node_name:
            printed_row = str(random.randint(1,20)) + ":" + elem + ":" + str(random.getrandbits(10))
            ff.write(printed_row + "\n")


for hour in range(11, 22):
        gen_new_file("logs/", hour)