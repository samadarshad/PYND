def parse_text_line(line):
    line = line.strip('\n\r').strip()
    parse = line.split(' - ')
    body = parse[0].strip('"')
    author = parse[1]
    return body, author