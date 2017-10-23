"""
Your job is to write a function which increments a string,
to create a new string. If the string already ends with a number,
the number should be incremented by 1. If the string does not end
with a number the number 1 should be appended to the new string.
"""

import re

def increment_string(strng):
    if re.search(r"(\d+)$", strng) is not None:
        strng = re.sub(r"(\d+)$", lambda x: str(int(x.group(1)) + 1).zfill(len(x.group(1))), strng)
    else:
        strng += "1"

    return strng
