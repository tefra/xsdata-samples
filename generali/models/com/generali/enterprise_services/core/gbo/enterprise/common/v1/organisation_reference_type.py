from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.reference_source_type import ReferenceSourceType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class OrganisationReferenceType(BaseIdentifiedComponentType):
    sender: Optional["OrganisationReferenceType.Sender"] = field(
        default=None,
        metadata={
            "name": "Sender",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Sender(CodeType):
        reference_type: Optional[ReferenceSourceType] = field(
            default=None,
            metadata={
                "name": "referenceType",
                "type": "Attribute",
            }
        )
