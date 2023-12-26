from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.cache_type import (
    CacheType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class Cache(CacheType):
    """
    <description xmlns="">Mandatory cache parameter support by all services (a
    service must understand the directive even if no caching support in the service
    – this allows for future extensibility of the service
    implementation)</description>
    """

    class Meta:
        namespace = "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
