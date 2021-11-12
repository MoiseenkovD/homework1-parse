def parse(query):
    result = {}
    queryParams = query.split("?")

    if len(queryParams) <= 1:
        return result

    queryParams = queryParams[1]

    x = queryParams.split("&")

    for i in x:
        if i == '':
            continue
        d = i.split("=")
        result[d[0]] = d[1]

    return result