def parse(filename, pattern):
    with open(filename) as ins:
        for line in ins:
            if m := pattern.search(line):
                yield m.groupdict()