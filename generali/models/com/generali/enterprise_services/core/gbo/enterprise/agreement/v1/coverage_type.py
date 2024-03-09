from dataclasses import dataclass, field
from typing import List, Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.amount_or_quantity_type import (
    AmountOrQuantityType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.code_description_type import (
    CodeDescriptionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geographical_scope import (
    GeographicalScope,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.perc_value_type import (
    PercValueType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.clauses_type import (
    ClausesType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductibles_type import (
    DeductiblesType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.exposure_type_apply_rate_type import (
    ExposureTypeApplyRateType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.exposure_type_basis import (
    ExposureTypeBasis,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.exposure_type_calculation_rate_type import (
    ExposureTypeCalculationRateType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.indemnity_type import (
    IndemnityType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limits_type import (
    LimitsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_type import (
    PremiumType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class CoverageType:
    """
    :ivar limits:
    :ivar deductibles:
    :ivar exposures:
    :ivar premium:
    :ivar coverage_code: The coverage code will be mapped in the
        reference data, no need to have an enum in the ServiceModel
    :ivar clauses:
    :ivar effective_date:
    :ivar end_date:
    :ivar retroactive_date:
    :ivar term_date:
    :ivar geographical_scope:
    :ivar claims_trigger:
    """

    limits: Optional[LimitsType] = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductibles: Optional[DeductiblesType] = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    exposures: Optional["ExposuresType"] = field(
        default=None,
        metadata={
            "name": "Exposures",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    premium: Optional[PremiumType] = field(
        default=None,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    coverage_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "CoverageCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    clauses: Optional[ClausesType] = field(
        default=None,
        metadata={
            "name": "Clauses",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    effective_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    end_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    retroactive_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "RetroactiveDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    term_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "TermDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    geographical_scope: Optional[GeographicalScope] = field(
        default=None,
        metadata={
            "name": "GeographicalScope",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    claims_trigger: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClaimsTrigger",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )


@dataclass
class ExposureType(BaseIdentifiedComponentType):
    annual_rate: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AnnualRate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    estimated_value: Optional[AmountOrQuantityType] = field(
        default=None,
        metadata={
            "name": "EstimatedValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    premium: Optional[PremiumType] = field(
        default=None,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    calculation_factor: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "CalculationFactor",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    apply_rate_type: Optional[ExposureTypeApplyRateType] = field(
        default=None,
        metadata={
            "name": "ApplyRateType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    unit: Optional[CodeDescriptionType] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    item: Optional[CodeDescriptionType] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    basis: Optional[ExposureTypeBasis] = field(
        default=None,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    calculation_rate_type: Optional[ExposureTypeCalculationRateType] = field(
        default=None,
        metadata={
            "name": "CalculationRateType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    coverage: Optional[CoverageType] = field(
        default=None,
        metadata={
            "name": "Coverage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mfl: Optional[PercValueType] = field(
        default=None,
        metadata={
            "name": "MFL",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    unit_price: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "UnitPrice",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    indemnity: Optional[IndemnityType] = field(
        default=None,
        metadata={
            "name": "Indemnity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )


@dataclass
class ExposuresType:
    exposure: List[ExposureType] = field(
        default_factory=list,
        metadata={
            "name": "Exposure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
