"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = f"{result[0:7]}{result[7].upper()}"
    return result

