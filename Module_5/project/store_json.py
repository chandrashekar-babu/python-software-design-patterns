def store_coro(filename):
    import json
    with open(filename, "w") as outs:
        while True:
            record = yield
            if record is None:
                break
            json.dump(record, outs)
            outs.write("\n")

def store(stream, filename):
    import json
    with open(filename, "w") as outs:
        for record in stream:
            json.dump(record, outs)
            outs.write("\n")
