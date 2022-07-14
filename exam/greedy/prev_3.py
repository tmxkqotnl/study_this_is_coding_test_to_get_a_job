import re


def solution(s: str):
    one = re.findall("(0+)", s)
    zero = re.findall("(1+)", s)

    return min(one.__len__(), zero.__len__())


input_samples = ["0001100", "11111", "00000001", "11001100110011000001", "11101101"]
for i in input_samples:
    print("input : {0} / answer : {1}".format(i, solution(i)))

