from random import randrange

class interval:
    def __init__(self, left_bound_type=1, right_bound_type=1, 
                 left_bound=0, right_bound=1):
        """Initialize interval with bound types and their numerical bounds. 

        left_bound_type -- 0 for open bound, 1 for closed bound
        right_bound_type -- 0 for open bound, 1 for closed bound
        left_bound -- numerical value of left bound
        right_bound -- numerical value of right bound
        """
        
        self.left_bound_type = left_bound_type
        self.right_bound_type = right_bound_type
        self.check_bounds_type()
        
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.check_bounds()


    def check_bounds_type(self) -> None:
        """Raises an error if bound types are improper."""

        if self.left_bound_type not in {0, 1}:
            raise ValueError("Improper left bound type selected.")
        if self.right_bound_type not in {0, 1}:
            raise ValueError("Improper right bound type selected.")


    def check_bounds(self) -> None:
        """Raises an error if bounds are improper."""
        not_closed = self.left_bound_type == 0 or self.right_bound_type == 0

        # Swap if necessary
        if self.left_bound > self.right_bound:
            self.left_bound, self.right_bound = self.right_bound, self.left_bound

        if self.left_bound.__class__.__name__ not in {"float", "int"}: 
            raise ValueError(f"Improper left bound value selected: {self.left_bound}.")
        if self.right_bound.__class__.__name__ not in {"float", "int"}: 
            raise ValueError(f"Improper right bound value selected: {self.right_bound}.")
        if self.left_bound == self.right_bound and not_closed:
            raise Exception("Bounds are of the same value on an interval that is not closed.")


    def get_bounds(self) -> list:
        """Return a two element list of the bounds."""
        return [self.left_bound, self.right_bound]
    

    def set_bounds(self, left_bound: float, right_bound: float) -> None:
        """Set the numerical bounds of an interval.

        Keyword arguments: 
        left_bound -- numerical value of new left bound
        right_bound -- numerical value of new right bound
        """
        
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.check_bounds()


    def get_bound_types(self) -> list:
        """Return bound types in a list."""
        
        return [self.left_bound_type, self.right_bound_type]
        

    # TODO: Add method to set bound types.
    def set_bound_types(self, left_bound_type, right_bound_type):
        pass

    def disp_bounds(self) -> str:
        """Return a string displaying the interval in mathematical notation."""
        # Choose correct bracket to use in mathematical notation.
        lb = ["(", "["][self.left_bound_type]  
        rb = [")", "]"][self.right_bound_type]

        return f"{lb}{self.left_bound}, {self.right_bound}{rb}"
    
    def contains(self, value) -> bool:
        """Check and return a boolean indicating if a value is contained within an interval.
        
        Keyword arguments:
        value -- numerical value to determine if within the set.
        """

        # We need to check if the value is contained within the two bounds, begin careful of bound type.
        # The checks are inclusive of bounds if they are closed, and exclusive otherwise. 
        left_bound_check = value >= self.left_bound if self.left_bound_type == 1 else value > self.left_bound
        right_bound_check = value <= self.right_bound if self.right_bound_type == 1 else value < self.right_bound
        return left_bound_check and right_bound_check
    
    # TODO: Add method to randomly choose element in interval.



