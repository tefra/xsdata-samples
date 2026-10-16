from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class SortOrderCodeType(StrEnum):
    """
    The direction by which to sort a set of values.
    """

    ASC = "ASC"
    DSC = "DSC"
