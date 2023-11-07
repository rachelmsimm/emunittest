class DuplicateNameOrKeyException(Exception):
    def __init__(self, message="The name or key of the demo you are trying to add already exists. Names and keys must be unique."):
        self.message = message
        super().__init__(self.message)