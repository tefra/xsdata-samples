from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.vessel_interest_type import VesselInterestType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class VesselType(BaseIdentifiedComponentType):
    imo_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImoNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    top: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Top",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flag",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    segment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Segment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    gross_tonnage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GrossTonnage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    dwt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DWT",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    score: Optional[int] = field(
        default=None,
        metadata={
            "name": "Score",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    classification_society: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassificationSociety",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    built_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "BuiltYear",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    vessel_interests: Optional["VesselType.VesselInterests"] = field(
        default=None,
        metadata={
            "name": "VesselInterests",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )

    @dataclass
    class VesselInterests:
        vessel_interest: List[VesselInterestType] = field(
            default_factory=list,
            metadata={
                "name": "VesselInterest",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )
