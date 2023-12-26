from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.risk_element_type import (
    RiskElementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class StructureType(RiskElementType):
    additional_information: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    automatic_fire_detection_coverage_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AutomaticFireDetectionCoveragePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    automatic_sprinkler_coverage_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AutomaticSprinklerCoveragePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    combustible_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CombustiblePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    construction_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConstructionYear",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    highly_protected_risk_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HighlyProtectedRiskPercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    survey_report_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SurveyReportAvailable",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    non_combustible_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NonCombustiblePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    part_combustible_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PartCombustiblePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    quality_rating: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "QualityRating",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    structure_area_m2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StructureAreaM2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    survey_report_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SurveyReportDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    top_location: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TopLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    construction_type: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ConstructionType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
