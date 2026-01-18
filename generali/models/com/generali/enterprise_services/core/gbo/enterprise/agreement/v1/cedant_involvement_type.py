from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
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


@dataclass(kw_only=True)
class CedantInvolvementType(OrganisationInvolvementType):
    organisation_role: InsurerRoleType = field(
        metadata={
            "name": "OrganisationRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    policy_identifier: None | Idtype = field(
        default=None,
        metadata={
            "name": "PolicyIdentifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    sequence_number: None | NumericType = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    ceded_risk_share: None | PercentType = field(
        default=None,
        metadata={
            "name": "CededRiskShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    retained_risk_share: None | PercentType = field(
        default=None,
        metadata={
            "name": "RetainedRiskShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
