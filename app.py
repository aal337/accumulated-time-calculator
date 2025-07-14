import js
from datetime import timedelta


def calculate(duration: tuple[int, str],
              frequency: tuple[int, str],
              timespan: tuple[int, str]
              ) -> tuple[int, str]:
    duration, frequency, timespan = tuple(map(lambda x: (x[1], x[0]), (duration, frequency, timespan)))
    duration, frequency, timespan = dict([duration]), dict([frequency]), dict([timespan])
    return timedelta(**duration) / timedelta(**frequency) * timedelta(**timespan)


def collect_input():
    return [(int(js.document.getElementById(name).value),
             js.document.getElementById(name + "-unit").value)
             for name in ["duration", "frequency", "timespan"]]


def output(result):
    value = (str(result.days) + " days") if result.days > 0 else ""
    value += (str(result.seconds) + " seconds") if result.seconds > 0 else ""
    js.document.getElementById("res-num").textContent = value


def handler():
    output(calculate(*collect_input()))


js.document.getElementById("thebutton").addEventListener("click", handler)
js.document.getElementById("thebutton").textContent = "(please input sth)"
