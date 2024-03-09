from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_type import (
    BaseReferenceComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.thing_actor_type import (
    ThingActorType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.actor_role_reference_type_contact_points import (
    ActorRoleReferenceTypeContactPoints,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.individual_actor_type import (
    IndividualActorType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_actor_type import (
    OrganisationActorType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class ActorRoleReferenceType(BaseReferenceComponentType):
    """
    <description xmlns="">A component defining a reference to a Party indicating
    the Role being undertaken by the Individual or Organisation.</description>

    :ivar organisation: <description xmlns="">The details of the
        organisation actor.</description>
    :ivar individual: <description xmlns="">The details of the
        individual actor.</description>
    :ivar thing: The details of the thing actor.
    :ivar contact_points:
    """

    organisation: Optional[OrganisationActorType] = field(
        default=None,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    individual: Optional[IndividualActorType] = field(
        default=None,
        metadata={
            "name": "Individual",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    thing: Optional[ThingActorType] = field(
        default=None,
        metadata={
            "name": "Thing",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    contact_points: Optional[ActorRoleReferenceTypeContactPoints] = field(
        default=None,
        metadata={
            "name": "ContactPoints",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
