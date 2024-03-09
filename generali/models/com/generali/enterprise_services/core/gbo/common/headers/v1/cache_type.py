from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.base_header_type import (
    BaseHeaderType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.cache_options import (
    CacheOptions,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class CacheType(BaseHeaderType):
    """
    <description xmlns="">Mandatory cache parameter supported by all services (a
    service must understand the directive even if no caching support in the service
    – this allows for future extensibility of the service
    implementation)</description>

    :ivar use_cache: <description xmlns="">Indicates whether caching
        should be used or not.</description>
    :ivar max_age_quantity:
    :ivar last_modified_date_time:
    """

    use_cache: Optional[CacheOptions] = field(
        default=None,
        metadata={
            "name": "UseCache",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
            "required": True,
        },
    )
    max_age_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxAgeQuantity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
    last_modified_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastModifiedDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
