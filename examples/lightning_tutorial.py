
# Helper to extract the bit of utool that we need

# This is a "lightning" liberator tutorial.

# Problem: I have an old codebase that has a function that I want, but I don't
# want to bring over that entire old codebase.

# Solution: Liberate the functionality you need with "liberator"

# Example: I want to get the "unarchive_file" function from an old codebase so
# I can just import the codebase (once), create a liberator object, then add
# the function I care about to the liberator object. Liberator will do its best
# to extract that relevant bit of code.

# We can also remove dependencies on external modules using the "expand"
# function. In this example, we "expand" out utool itself, because we dont want
# to depend on it. The liberator object will then crawl through the code and
# try to bring in the source for the expanded dependencies. Note, that the
# expansion code works well, but not perfectly. It cant handle `import *` or
# other corner cases that can break the static analysis.


# Requires:
#     pip install liberator

import liberator
import utool as ut

lib = liberator.Liberator()
lib.add_dynamic(ut.unarchive_file)
# lib.expand(['utool'])
print(lib.current_sourcecode())


# doesnt work
# lib.expand(['utool.util_arg'])
