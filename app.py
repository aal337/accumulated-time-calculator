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
    return [(js.document.getElementById(name).value,
             js.document.getElementById(name + "-unit"))
             for name in ["duration", "frequency", "timespan"]]


def output(result):
    value = (str(result.days) + " days") if result.days else ""
    value += (str(result.hours) + " hours") if result.hours else ""
    value += (str(result.minutes) + " minutes") if result.minutes else ""
    value += (str(result.seconds) + " seconds") if result.seconds else ""
    js.document.getElementById("res-num").value = value


def handler():
    output(calculate(*collect_input()))


js.document.getElementByTagName("button").item(0).addEventListener("click", handler)
