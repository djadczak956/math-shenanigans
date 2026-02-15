class interval:
    def __init__(self, left_bound_type: int, right_bound_type: int, 
                 left_bound: float, right_bound: float):
        """Initialize interval with bound types and their numerical bounds. 

        left_bound_type -- 0 for open bound, 1 for closed bound
        right_bound_type -- 0 for open bound, 1 for closed bound
        left_bound -- numerical value of left bound
        right_bound -- numerical value of right bound
        """

        if left_bound_type not in {0, 1}:
            raise ValueError("Improper left bound type selected.")
        if right_bound_type not in {0, 1}:
            raise ValueError("Improper right bound type selected.")
        self.left_bound_type = left_bound_type
        self.right_bound_type = right_bound_type
        
        if left_bound.__class__.__name__ not in {"float", "int"}: 
            raise ValueError(f"Improper left bound value selected: {left_bound}.")
        if right_bound.__class__.__name__ not in {"float", "int"}: 
            raise ValueError(f"Improper right bound value selected: {right_bound}.")
        self.left_bound = left_bound
        self.right_bound = right_bound
        

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


    def disp_bounds(self) -> str:
        """Return a string displaying the interval in mathematical notation."""
        
        # Choose proper bracket for each bound
        lb = ["(", "["][self.left_bound_type]  
        rb = [")", "]"][self.right_bound_type]

        return f"{lb}{self.left_bound}, {self.right_bound}{rb}"
    

x1 = interval(0, 0, 0, 1)
print(x1.disp_bounds())

x2 = interval(1, 1, 0, 1)
print(x2.disp_bounds())

print(x2.get_bounds()[1])