# Python special method (dunder) list.

## reference URL
[Python Data model](https://docs.python.org/3/reference/datamodel.html#special-method-names)

### Special method names

#### Basic

- __new__(cls[, ...])

- __init__(self[, ...])

- __del__(self)

- __repr__(self)

- __str__(self)

- __byte__(self)

- __format__(self, format_spec)

- __lt__(self, other)

- __le__(self, other)

- __eq__(self, other)

- __ne__(self, other)

- __gt__(self, other)

- __ge__(self, other)

- __hash__(self)

- __bool__(self)


#### Customizing attribute access

- __getattr__(self, name)

- __getattribute__(self, name)

- __setattr__(self, name, value)

- __delattr__(self, name)

- __dir__(self)

##### Implementing Descriptors

- __get__(self, instance, owner=None)

- __set__(self, instance, value)

- __delete__(self, instance)

##### Slots

- __slots__

#### Customizing class creation

- __init_subclass__(cls)

- __set_name__(self, owner, name)

#### Emulating generic types

- __class_getitem__(cls, key)

#### Emulating callable objects

- __call__(self[, args...])

#### Emulating container types

- __len__(self)

- __length_hint__(self)

- __getitem__(self, key)

- __setitem__(self, key, value)

- __deltitem__(self, key)

- __missing__(self, key)

- __iter__(self)

- __reversed__(self)

- __contains__(self, item)

#### Emulating numeric types

- __add__(self, other)

- __sub__(self, other)

- __mul__(self, other)

- __matmul__(self, other)

- __truediv__(self, other)

- __floordiv__(self, other)

- __mod__(self, other)

- __divmod__(self, other)

- __pow__(self, other[, modulo])

- __lshift__(self, other)

- __rshift__(self, other)

- __and__(self, other)

- __xor__(self, other)

- __or__(self, other)

- __radd__(self, other)

- __rsub__(self, other)

- __rmul__(self, other)

- __rmatmul__(self, other)

- __rtruediv__(self, other)

- __rmod__(self, other)

- __rdivmod__(self, other)

- __rpow__(self, other[, modulo])

- __rlshift__(self, other)

- __rrshift__(self, other)

- __rand__(self, other)

- __rxor__(self, other)

- __ror__(self, other)

- __iadd__(self, other)

- __isub__(self, other)

- __imul__(self, other)

- __imatmul__(self, other)

- __itruediv__(self, other)

- __imod__(self, other)

- __ipow__(self, other[, modulo])

- __ilshift__(self, other)

- __irshift__(self, other)

- __iand__(self, other)

- __ixor__(self, other)

- __ior__(self, other)

- __neg__(self)

- __pos__(self)

- __abs__(self)

- __invert__(self)

- __complex__(self)

- __int__(self)

- __float__(self)

- __index__(self)

- __round__(self[, ndigits])

- __trunc__(self)

- __floor__(self)

- __ceil__(self)

#### With Statement Context Managers

- __enter__(self)

- __exit__(self, exc_type, exc_value, traceback)

#### Customizing positional arguments in class pattern matching

- __match_args__

### Coroutines

#### Awaitable Objects

- __await__(self)

#### Asynchronous Iterators

- __aiter__(self)

- __anext__(self)

#### Asynchronous Context Managers

- __aenter__(self)

- __aexit__(self)
