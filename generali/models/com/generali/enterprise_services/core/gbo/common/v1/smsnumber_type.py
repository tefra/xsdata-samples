from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class SmsnumberType:
    """
    <description xmlns=""> <description>The definition for an SMS
    number.</description> </description>

    :ivar full_number_text: <description xmlns=""> <description>The full
        SMS number.</description> </description>
    """
    class Meta:
        name = "SMSNumberType"

    full_number_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FullNumberText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
