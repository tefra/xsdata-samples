from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_type import BaseReferenceComponentType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.thing_actor_type import ThingActorType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_point_type import ContactPointType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.individual_actor_type import IndividualActorType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_actor_type import OrganisationActorType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class ActorRoleReferenceType(BaseReferenceComponentType):
    """
    <description xmlns="">A component defining a reference to a Party
    indicating the Role being undertaken by the Individual or
    Organisation.</description>

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
        }
    )
    individual: Optional[IndividualActorType] = field(
        default=None,
        metadata={
            "name": "Individual",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    thing: Optional[ThingActorType] = field(
        default=None,
        metadata={
            "name": "Thing",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    contact_points: Optional["ActorRoleReferenceType.ContactPoints"] = field(
        default=None,
        metadata={
            "name": "ContactPoints",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )

    @dataclass
    class ContactPoints:
        """
        :ivar contact_point: A specific contact point for the actor.
        """
        contact_point: List[ContactPointType] = field(
            default_factory=list,
            metadata={
                "name": "ContactPoint",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
                "min_occurs": 1,
            }
        )
