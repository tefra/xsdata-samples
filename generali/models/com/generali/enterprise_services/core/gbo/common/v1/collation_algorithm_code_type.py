from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class CollationAlgorithmCodeType(StrEnum):
    """
    The collation (sort) algorithm to use in the sorting to the result set.
    """

    UTS_10 = "UTS#10"
