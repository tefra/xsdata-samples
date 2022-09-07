from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/fundref.xsd"


class AssertionProvider(Enum):
    PUBLISHER = "publisher"
    CROSSREF = "crossref"
