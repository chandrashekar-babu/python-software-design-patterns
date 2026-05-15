import log_parser
import store_json

import re

regex = r'''
    (?P<timestamp>   # Extract timestamp (Dec 30 06:00:23)
        \w+      
        \s       
        \d+
        \s
        \S+       
    )
    .+
    Failed
    \s
    password
    \s
    for
    \s
    (invalid \s user \s)?
    (?P<username>\S+?)     # Extract username
    \s from \s
    (?P<ipaddr>\S+)        # Extract ip address
'''


def log_processor(transform_operations={}):
    pattern = re.compile(regex, re.VERBOSE)

    parser = log_parser.parse("sshd_minimal.log", pattern)
    storer = store_json.store_coro("failed_logins_test.json")
    next(storer)  # Prime the coroutine

    try:
        for record in parser:
            for field, operation in transform_operations.items():
                record = operation(record, field)
            storer.send(record)

        storer.send(None)  # Close the coroutine
    except StopIteration:
        pass

def standardize_timestamp(record, field):
    record = record.copy()
    from datetime import datetime
    time_str = record[field]
    new_dt = datetime.strptime(time_str, "%b %d %H:%M:%S")
    record[field] = new_dt.replace(year=2024).isoformat()
    return record

if __name__ == "__main__":
    log_processor({"timestamp": standardize_timestamp})
