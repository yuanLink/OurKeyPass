import json
import dawg


def buildDAWG(filename, savename):
    fp = open(filename, 'r')

    result = json.load(fp)
    my_dict = {}
    for each in result:
        if "W" in each:
            my_dict.update(result[each])

    my_list = []
    index = 0
    for each in my_dict:
        my_list.append((each, my_dict[each]))
        index += 1
    my_list.append(("__total__", index))

    my_dawg = dawg.IntDAWG(my_list)

    with open(savename, 'wb') as f:
        my_dawg.write(f)


if __name__ == "__main__":
    buildDAWG("grammar.cfg", "words.dawg")
