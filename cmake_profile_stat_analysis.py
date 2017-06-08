#!/usr/bin/env python

import sys
import re
import pprint
from operator import itemgetter

def process(filename):
    regex = re.compile(r"\s*\[\d+\].*\:\d+\:\s(.*?)\(.*\)\s\((.*?)sec\)")

    function_times = {}

    with open(filename) as f:
        for line in f:
            m = regex.match(line)
            if m:
                function_name = m.group(1).upper() #function
                function_duration = float(m.group(2)) #duration
                
                if not function_name in function_times:
                    function_times[function_name] = function_duration
                else:
                    function_times[function_name] = function_times[function_name] + function_duration

    
    function_times_by_time = sorted(function_times.items(), key=itemgetter(1), reverse=True)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(function_times_by_time)


if __name__ == '__main__':
    filename = sys.argv[1]
    process(filename)
