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
class SourceType(BaseSystemTraceabilityType):
    """
    <description xmlns="">The specification of the source country, locale, system
    of the message.</description>

    :ivar sent_date_time: <description xmlns="">The date and time on
        which the message was sent.</description>
    """

    sent_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SentDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
        },
    )
