from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insurer_role_type import (
    InsurerRoleType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_involvement_type import (
    OrganisationInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class ProducerInvolvementType(OrganisationInvolvementType):
    organisation_role: Optional[InsurerRoleType] = field(
        default=None,
        metadata={
            "name": "OrganisationRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    producer_agreement_identifier: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "ProducerAgreementIdentifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    producing_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducingCountry",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
            "pattern": r"[A-Z][A-Z]",
        },
    )
