# Package Sorter

Sorts packages into stacks for Smarter Technology's robotic arm system.

## How it works

`sort(width, height, length, mass)` takes dimensions in cm and mass in kg, returns which stack the package goes to:

- **STANDARD** - normal packages, not bulky or heavy
- **SPECIAL** - package is bulky or heavy (but not both)
- **REJECTED** - package is both bulky and heavy

A package is considered **bulky** if its volume is >= 1,000,000 cm³ or any dimension is >= 150 cm.
A package is **heavy** if its mass is >= 20 kg.

## Example

```python
from sort import sort

sort(10, 10, 10, 5)      # => "STANDARD"
sort(150, 10, 10, 1)     # => "SPECIAL" (bulky)
sort(10, 10, 10, 25)     # => "SPECIAL" (heavy)
sort(100, 100, 100, 20)  # => "REJECTED"
```

## Tests

```
pip install pytest
pytest test_sort.py -v
```
