from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coinsurer_involvement_type_enum import (
    CoinsurerInvolvementTypeEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insurer_role_type import (
    InsurerRoleType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_involvement_type import (
    OrganisationInvolvementType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.premium_type_enum import (
    PremiumTypeEnum,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class CoinsurerInvolvementType(OrganisationInvolvementType):
    apply_to: None | PremiumTypeEnum = field(
        default=None,
        metadata={
            "name": "ApplyTo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    organisation_role: None | InsurerRoleType = field(
        default=None,
        metadata={
            "name": "OrganisationRole",
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
    coinsurance_percentage: None | PercentType = field(
        default=None,
        metadata={
            "name": "CoinsurancePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    involvement_type: None | CoinsurerInvolvementTypeEnum = field(
        default=None,
        metadata={
            "name": "InvolvementType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    commision_percentage: None | PercentType = field(
        default=None,
        metadata={
            "name": "CommisionPercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    coinsurer_reference: None | CodeType = field(
        default=None,
        metadata={
            "name": "CoinsurerReference",
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
    overrider_percentage: None | PercentType = field(
        default=None,
        metadata={
            "name": "OverriderPercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    local_ceded_share: None | PercentType = field(
        default=None,
        metadata={
            "name": "LocalCededShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
