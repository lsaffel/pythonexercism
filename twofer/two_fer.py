def two_fer(name="no name given"):
    if name == "no name given":
        return "One for you, one for me."
    else:
        return "One for " + name + ", one for me."


print(two_fer("Irving"))
print(two_fer())
print(two_fer("Frederick"))
print(two_fer("Sam"))
