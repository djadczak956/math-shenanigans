class interval:
    def __init__(self, left_bracket: bool, right_bracket: bool, 
                 left_bound: float, right_bound: float):
        self.left_bracket = left_bracket
        self.right_bracket = right_bracket
        self.left_bound = left_bound
        self.right_bound = right_bound

    def set_bounds(self, left_bound: float, right_bound: float) -> None:
        try:
            self.left_bound = left_bound
            self.right_bound = right_bound
        except:
            print("Error: Bounds not set.")

    def disp_bounds(self) -> str:
        # Choose whether each bound is open or closed
        lb = ["(", "["][self.left_bracket]  
        rb = [")", "]"][self.right_bracket]

        return f"{lb}{self.left_bound}, {self.right_bound}{rb}"
    
x = interval(0, 0, 0, 1)
print(x.disp_bounds())