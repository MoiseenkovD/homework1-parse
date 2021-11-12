def parse_cookie(query):
    result = {}
    c = query.split(";")
    for word in c:
        if word == '':
            continue
        d = word.split("=", 1)

        result[d[0]] = d[1]
    return result


