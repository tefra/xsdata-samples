from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class QueryAlgorithmCodeType(Enum):
    STRICT = "Strict"
    REG_EX = "RegEx"
    FUZZY = "Fuzzy"
