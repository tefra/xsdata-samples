from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class QueryOperatorCodeType(Enum):
    EQUALS = "Equals"
    NOT_EQUALS = "Not Equals"
    GREATER_THAN = "Greater Than"
    GREATER_THAN_EQUALS = "Greater Than Equals"
    LESS_THAN = "Less Than"
    LESS_THAN_EQUALS = "Less Than Equals"
    CONTAINS = "Contains"
    DOES_NOT_CONTAIN = "Does Not Contain"
    LIKE = "Like"
    NOT_LIKE = "Not Like"
