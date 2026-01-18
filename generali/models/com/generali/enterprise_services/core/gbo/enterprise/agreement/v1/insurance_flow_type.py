from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.insurance_flow_type_cedants import (
    InsuranceFlowTypeCedants,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.insurance_flow_type_coinsurer_involvements import (
    InsuranceFlowTypeCoinsurerInvolvements,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.insurance_flow_type_reinsurers import (
    InsuranceFlowTypeReinsurers,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_involvement_type import (
    OrganisationInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class InsuranceFlowType(OrganisationInvolvementType):
    sequence_number: NumericType | None = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    risk_share: PercentType | None = field(
        default=None,
        metadata={
            "name": "RiskShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    cedants: InsuranceFlowTypeCedants | None = field(
        default=None,
        metadata={
            "name": "Cedants",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    coinsurer_involvements: InsuranceFlowTypeCoinsurerInvolvements | None = (
        field(
            default=None,
            metadata={
                "name": "CoinsurerInvolvements",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            },
        )
    )
    reinsurers: InsuranceFlowTypeReinsurers | None = field(
        default=None,
        metadata={
            "name": "Reinsurers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
