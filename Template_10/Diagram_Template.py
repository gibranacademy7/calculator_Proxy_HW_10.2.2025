# Diagram:

# +---------------------+
# |    InputTemplate    |
# |---------------------|
# | + get_input()       |
# | + validate_input()  |
# +---------------------+
#           ^
#           |
#           |
# +---------------------+      +---------------------+
# |     NumberInput     |      |      EmailInput     |
# |---------------------|      |---------------------|
# | + get_input()       |      | + get_input()       |
# | + validate_input()  |      | + validate_input()  |
# +---------------------+      +---------------------+
