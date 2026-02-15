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
        if left_bound == right_bound:
            raise Exception("Bounds are of the same value.")
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
    

x1 = interval(0, 0, 0, 1)
print(x1.disp_bounds())

for a in [-1, 0, 0.25, 1/3, 0.5, 2/3, 0.75, 0.999999, 1, 1.01]:
    print(f"a = {a} is in x1: {x1.contains(a)}")
    
print()
x2 = interval(1, 1, 0, 1)
print(x2.disp_bounds())

for a in [-1, 0, 0.25, 1/3, 0.5, 2/3, 0.75, 0.999999, 1, 1.01]:
    print(f"a = {a} is in x2: {x2.contains(a)}")