from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.contact_involvement_enum import (
    ContactInvolvementEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.contact_involvement import (
    ContactInvolvement as ContactInvolvementContactInvolvement,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class ContactInvolvement(ContactInvolvementContactInvolvement):
    contact_involvement_type: ContactInvolvementEnum | None = field(
        default=None,
        metadata={
            "name": "ContactInvolvementType",
            "type": "Attribute",
        },
    )
