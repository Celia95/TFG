def frange(start, end, step):
    while start < end:
        yield start
        start = start + step