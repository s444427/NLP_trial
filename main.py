
def parser(sentence):
    local_information = []
    word = ""

    for i in sentence:
        if i != ' ':
            word = word + i
        else:
            local_information.append(word)
            word = ''

    local_information.append(word)
    return local_information


def extractor(information):
    local_extract = {}

    for i in range(len(information)):
        # date extraction
        if information[i] in ['today', 'tomorrow']:
            local_extract['date'] = information[i]

        # time extraction
        if information[i] in ['at']:
            local_extract['time'] = information[i+1]

        # place extraction
        if information[i] in ['in']:

            place = ''
            j = i + 1

            while information[j] not in ['with']:
                place = place + information[j] + ' '
                j += 1

            # Delete last space
            place = place[:-1]
            local_extract['place'] = place

    return local_extract


if __name__ == '__main__':
    information = parser("Hello World and the other creatures, let's meet today at 8PM in our favourite restaurant with friends")
    extract = extractor(information)

    print(information)
    print(extract)
