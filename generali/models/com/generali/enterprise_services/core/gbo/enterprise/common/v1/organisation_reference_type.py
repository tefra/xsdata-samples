from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_reference_type_sender import (
    OrganisationReferenceTypeSender,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class OrganisationReferenceType(BaseIdentifiedComponentType):
    sender: Optional[OrganisationReferenceTypeSender] = field(
        default=None,
        metadata={
            "name": "Sender",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    external: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
