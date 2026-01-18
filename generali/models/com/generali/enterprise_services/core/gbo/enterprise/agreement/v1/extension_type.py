from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class ExtensionType:
    effective_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    end_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    retroactive_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "RetroactiveDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    term_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "TermDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    premium: None | PremiumType = field(
        default=None,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    exposures: None | ExposuresType = field(
        default=None,
        metadata={
            "name": "Exposures",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductibles: None | DeductiblesType = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    clauses: None | ClausesType = field(
        default=None,
        metadata={
            "name": "Clauses",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    limits: None | LimitsType = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    extension_code: CodeDescriptionType = field(
        metadata={
            "name": "ExtensionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    geographical_scope: None | GeographicalScope = field(
        default=None,
        metadata={
            "name": "GeographicalScope",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
