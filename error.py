class InvalidRowError(Exception):
    def __init__(self, row):
        super(InbalidRowError, self).__init__(f"Row: {row} is invalid index")


class InvalidColumnError(Exception):
    def __init__(self, col):
        super(InvalidColumnError, self).__init__(f"Columns: {col} is invalid index")


class ExistError(Exception):
    def __init__(self):
        super(ExistError, self).__init__("Specified position is already exist")
