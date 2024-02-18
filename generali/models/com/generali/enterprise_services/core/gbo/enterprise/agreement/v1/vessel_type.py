from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.vessel_type_vessel_interests import (
    VesselTypeVesselInterests,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class VesselType(BaseIdentifiedComponentType):
    imo_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImoNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    top: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Top",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flag",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    segment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Segment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    gross_tonnage: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "GrossTonnage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    dwt: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "DWT",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    score: Optional[NumberType] = field(
        default=None,
        metadata={
            "name": "Score",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    classification_society: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassificationSociety",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    built_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "BuiltYear",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    vessel_interests: Optional[VesselTypeVesselInterests] = field(
        default=None,
        metadata={
            "name": "VesselInterests",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
