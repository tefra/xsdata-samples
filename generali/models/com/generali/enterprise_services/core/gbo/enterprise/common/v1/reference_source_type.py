from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


class ReferenceSourceType(Enum):
    LOCAL_COUNTRY_REFERENCE = "LocalCountryReference"
    BUSINESS_LINE_REFERENCE = "BusinessLineReference"
