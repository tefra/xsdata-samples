from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cedant_involvement_type import CedantInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coinsurer_involvement_type import CoinsurerInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.reinsurer_involvement_type import ReinsurerInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_involvement_type import OrganisationInvolvementType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class InsuranceFlowType(OrganisationInvolvementType):
    sequence_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    risk_share: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RiskShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    cedants: Optional["InsuranceFlowType.Cedants"] = field(
        default=None,
        metadata={
            "name": "Cedants",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    coinsurer_involvements: Optional["InsuranceFlowType.CoinsurerInvolvements"] = field(
        default=None,
        metadata={
            "name": "CoinsurerInvolvements",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    reinsurers: Optional["InsuranceFlowType.Reinsurers"] = field(
        default=None,
        metadata={
            "name": "Reinsurers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )

    @dataclass
    class Cedants:
        cedant: List[CedantInvolvementType] = field(
            default_factory=list,
            metadata={
                "name": "Cedant",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class CoinsurerInvolvements:
        coinsurer: List[CoinsurerInvolvementType] = field(
            default_factory=list,
            metadata={
                "name": "Coinsurer",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Reinsurers:
        reinsurer: List[ReinsurerInvolvementType] = field(
            default_factory=list,
            metadata={
                "name": "Reinsurer",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
                "min_occurs": 1,
            }
        )
