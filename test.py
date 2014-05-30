import itertools
import pprint

pp = pprint.PrettyPrinter(indent=4)

a = [["a", "b", "c"],
     ["1","2","3"]
     ]

result = map("".join, itertools.product(*a))
pp.pprint(result)