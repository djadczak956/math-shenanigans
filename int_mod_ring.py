class int_mod_ring:
    def __init__(self, mod_val: int) -> None:
        self.mod_val = mod_val
        self.check_mod_val()
        self.ring = list(range(0, self.mod_val))

    def check_mod_val(self) -> None:
        """Check to make sure that the modulus value is an integer greater than 1."""
        try:
            if self.mod_val.__class__.__name__ != "int" or self.mod_val <= 1:
                raise ValueError()

        except ValueError:
            print("ERROR: Modulus value must be an integer strictly greater than 1.")
    
    def to_list(self) -> list:
        """Return a list of the values in the ring. """
        return self.ring