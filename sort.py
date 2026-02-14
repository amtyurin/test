def sort(width, height, length, mass):
    """Determine which stack a package goes to based on size and weight."""
    for val in (width, height, length, mass):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Expected a number, got {type(val).__name__}")
        if val < 0:
            raise ValueError(f"Dimensions and mass can't be negative (got {val})")

    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
