from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_person_type_contact_points import (
    ContactPersonTypeContactPoints,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.individual_actor_type import (
    IndividualActorType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class ContactPersonType(BaseIdentifiedComponentType):
    """
    <description xmlns=""/>.

    :ivar individual: <description xmlns="">The details of the
        individual who is the contact.</description>
    :ivar contact_points: <description xmlns="">The set of contact
        points for the contact person.</description>
    """

    individual: None | IndividualActorType = field(
        default=None,
        metadata={
            "name": "Individual",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
    contact_points: None | ContactPersonTypeContactPoints = field(
        default=None,
        metadata={
            "name": "ContactPoints",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
