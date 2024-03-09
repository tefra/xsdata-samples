from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.base_system_traceability_type import (
    BaseSystemTraceabilityType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class TargetType(BaseSystemTraceabilityType):
    """
    <description xmlns="">The specification of the target country, locale, system
    of the message.</description>

    :ivar received_date_time: <description xmlns="">The date and time
        the message was received at the target system. Only applicable
        when the target header is part of a response
        message.</description>
    """

    received_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReceivedDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
