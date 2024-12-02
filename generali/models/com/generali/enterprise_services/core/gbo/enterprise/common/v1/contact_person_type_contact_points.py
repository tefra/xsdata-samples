from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_point_type import (
    ContactPointType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class ContactPersonTypeContactPoints:
    class Meta:
        global_type = False

    contact_point: list[ContactPointType] = field(
        default_factory=list,
        metadata={
            "name": "ContactPoint",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "min_occurs": 1,
        },
    )
