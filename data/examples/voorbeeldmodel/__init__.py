"""YeOleDummy - Package met class en factory voor een eenvoudige
dummy-classifier, ontwikkeld als voorbeeld door Ye Ole Teacher."""

from .model import YeOleDummy

def model_factory():
    return YeOleDummy()