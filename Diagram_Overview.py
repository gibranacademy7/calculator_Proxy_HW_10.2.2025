# Diagram Overview:

# +------------------------+
# |  CalculatorAbstract    |
# |------------------------|
# | + add(a, b)           |
# | + sub(a, b)           |
# | + mul(a, b)           |
# | + div(a, b)           |
# | + power(a, b)         |
# +------------------------+
#             ^
#             |
#             |
# +------------------------+
# |       Calculator       |
# |------------------------|
# | + add(a, b)           |
# | + sub(a, b)           |
# | + mul(a, b)           |
# | + div(a, b)           |
# | + power(a, b)         |
# +------------------------+
#             ^
#             |
#             |
# +------------------------+
# |     CalculatorProxy    |
# |------------------------|
# | + add(a, b)           |
# | + sub(a, b)           |
# | + mul(a, b)           |  -> NotImplementedError
# | + div(a, b)           |  -> NotImplementedError
# | + power(a, b)         |  -> NotImplementedError
# +------------------------+

# +------------------------+
# |        main()          |
# |------------------------|
# | * Creates Proxy       |
# | * Calls allowed ops   |
# | * Catches exceptions   |
# +------------------------+
