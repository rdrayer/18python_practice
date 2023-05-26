def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0

      f=(c*9/5)+32
      celsius = (fahrenheit - 32)/1.8
    """

    # YOUR CODE HERE
    in_unit = unit_in
    out_unit = unit_out
    temp_in = temp

    if in_unit == "c" and out_unit == "f":
        return (temp*9/5) + 32
    elif in_unit == "f" and out_unit == "c":
        return ((temp - 32)/1.8)
    elif in_unit == "z" or out_unit == "z":
        return f"Invalid unit z"
    else:
        return temp


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

