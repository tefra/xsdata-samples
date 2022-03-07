from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class SortOrderCodeType(Enum):
    """
    The direction by which to sort a set of values.
    """
    ASC = "ASC"
    DSC = "DSC"
