from dataclasses import dataclass, field
from typing import Optional

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


@dataclass
class CoinsurerInvolvementType(OrganisationInvolvementType):
    apply_to: PremiumTypeEnum | None = field(
        default=None,
        metadata={
            "name": "ApplyTo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    organisation_role: InsurerRoleType | None = field(
        default=None,
        metadata={
            "name": "OrganisationRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    sequence_number: NumericType | None = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    coinsurance_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "CoinsurancePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    involvement_type: CoinsurerInvolvementTypeEnum | None = field(
        default=None,
        metadata={
            "name": "InvolvementType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    commision_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "CommisionPercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    coinsurer_reference: CodeType | None = field(
        default=None,
        metadata={
            "name": "CoinsurerReference",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    retained_risk_share: PercentType | None = field(
        default=None,
        metadata={
            "name": "RetainedRiskShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    overrider_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "OverriderPercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    local_ceded_share: PercentType | None = field(
        default=None,
        metadata={
            "name": "LocalCededShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
