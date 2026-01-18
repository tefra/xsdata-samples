from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_person_type import (
    ContactPersonType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class IndividualRoleType:
    """
    :ivar individual: A contact person for the organisation.
    """

    individual: ContactPersonType | None = field(
        default=None,
        metadata={
            "name": "Individual",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
