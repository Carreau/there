# There

Print the current filename and line. 

Example, `where.py`

```
import there
import there as here

print(here)
print('and')
print(there)
```

Then `python where.py` will print:

```
where.py:4
and
where.py:6
```

That's it (for now), non more, no less. I have plan – the usually never get
realised – to also have a `there.indent` that return the indentation of the
current line.

# Gotchas

Returns the line where the `__str__`, or `__repr__` of `there` is computed.
Usually by `print`. So it might be wrong. If you want to be sure (like when
using `log`) wrap it in `str()`

Runs only on CPython likely. But anyway don't run it in production.




