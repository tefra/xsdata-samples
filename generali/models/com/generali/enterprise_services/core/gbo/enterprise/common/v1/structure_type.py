from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
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
    additional_information: TextType | None = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    automatic_fire_detection_coverage_percentage: PercentType | None = (
        field(
            default=None,
            metadata={
                "name": "AutomaticFireDetectionCoveragePercentage",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            },
        )
    )
    automatic_sprinkler_coverage_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "AutomaticSprinklerCoveragePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    combustible_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "CombustiblePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    construction_year: NumberType | None = field(
        default=None,
        metadata={
            "name": "ConstructionYear",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    highly_protected_risk_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "HighlyProtectedRiskPercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    survey_report_available: bool | None = field(
        default=None,
        metadata={
            "name": "SurveyReportAvailable",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    non_combustible_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "NonCombustiblePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    part_combustible_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "PartCombustiblePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    quality_rating: CodeType | None = field(
        default=None,
        metadata={
            "name": "QualityRating",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    structure_area_m2: NumericType | None = field(
        default=None,
        metadata={
            "name": "StructureAreaM2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    survey_report_date: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "SurveyReportDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    top_location: bool | None = field(
        default=None,
        metadata={
            "name": "TopLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    construction_type: CodeType | None = field(
        default=None,
        metadata={
            "name": "ConstructionType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
