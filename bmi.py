def bmi(mass: int, height: int) -> str:
    res = mass / pow(height, 2)
    if res <= 18.5:
        return "Underweight"
    elif res <= 25.0:
        return "Normal"
    elif res <= 30.0:
        return "Overweight"
    else:
        return "Obese"

assert bmi(50, 1.80) == "Underweight"
assert bmi(80, 1.80) == "Normal"
assert bmi(90, 1.80) == "Overweight"
assert bmi(110, 1.80) == "Obese"
assert bmi(50, 1.50) == "Normal"