# Introduction
This document adheres to the specifications outlined in
[RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

# Version Control
### Commit Messages
- Issue IDs **must** be included.
```
# YES
git commit --message "PROJECT-1: foo"

# No
git commit --message "foo"
```

# Python
### General
- Classes and their modules **should not** be named with an object type suffix. An exception is
    with Models. Model classes and their modules **must not** be named with an object type suffix.
```
# YES
/foos
    - eggs.py
    - ham.py

# No
/foos
    - eggs_foo.py
    - ham_foo.py
```
