from json2html import *
input = {
        "sample": [{
                "a":1, "b":2, "c":3
        }, {
                "a":5, "b":6, "c":7
        }]
}
print(json2html.convert(json = input))