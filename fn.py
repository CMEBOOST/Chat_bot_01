import time


def stream_data(info):
    for word in info.split(" "):
        yield word + " "
        time.sleep(0.10)