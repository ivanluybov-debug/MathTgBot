class GeneratorError(Exception):
    pass


class DifficultAlreadySetError(GeneratorError):
    pass

class DifficultNotSetError(GeneratorError):
    pass