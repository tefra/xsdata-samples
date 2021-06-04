from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class NilReasonEnumerationValue(Enum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"
