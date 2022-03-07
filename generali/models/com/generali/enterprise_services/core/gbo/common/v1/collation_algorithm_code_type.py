from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class CollationAlgorithmCodeType(Enum):
    """
    The collation (sort) algorithm to use in the sorting to the result set.
    """
    UTS_10 = "UTS#10"
