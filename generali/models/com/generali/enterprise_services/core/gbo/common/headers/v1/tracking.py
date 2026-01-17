from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.tracking_type import (
    TrackingType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class Tracking(TrackingType):
    """
    <description xmlns="">Holds in-flight tracking
    information.</description>.
    """

    class Meta:
        namespace = "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
