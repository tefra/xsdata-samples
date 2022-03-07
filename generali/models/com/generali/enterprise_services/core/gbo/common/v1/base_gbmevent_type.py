from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbmtype import BaseGbmtype
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.event_code_type import EventCodeType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseGbmeventType(BaseGbmtype):
    """
    <description xmlns="">The base definition of all business events and
    notifications.</description>

    :ivar event_code: <description xmlns="">A value representing the
        event that occurred on the publishing system to generate this
        notify event.</description>
    :ivar business_event_code: <description xmlns="">A value
        representing the business event that occurred on the publishing
        system to generate this notify event.</description>
    """
    class Meta:
        name = "BaseGBMEventType"

    event_code: Optional[EventCodeType] = field(
        default=None,
        metadata={
            "name": "eventCode",
            "type": "Attribute",
            "required": True,
        }
    )
    business_event_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "businessEventCode",
            "type": "Attribute",
        }
    )
