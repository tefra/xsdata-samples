from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.value_type import ValueType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class PricingLayerType(BaseIdentifiedComponentType):
    primary: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Primary",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    attachment_point: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AttachmentPoint",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    limit: Optional["PricingLayerType.Limit"] = field(
        default=None,
        metadata={
            "name": "Limit",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    poshare: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "POShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )

    @dataclass
    class Limit:
        value: Optional[ValueType] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )
