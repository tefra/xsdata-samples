from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.code_description_type import (
    CodeDescriptionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geographical_scope import (
    GeographicalScope,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.clauses_type import (
    ClausesType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coverage_type import (
    ExposuresType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductibles_type import (
    DeductiblesType,
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
class ExtensionType:
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
    premium: Optional[PremiumType] = field(
        default=None,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    exposures: Optional[ExposuresType] = field(
        default=None,
        metadata={
            "name": "Exposures",
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
    clauses: Optional[ClausesType] = field(
        default=None,
        metadata={
            "name": "Clauses",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    limits: Optional[LimitsType] = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    extension_code: Optional[CodeDescriptionType] = field(
        default=None,
        metadata={
            "name": "ExtensionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
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
