from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductibles_type import (
    DeductiblesType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limits_type import (
    LimitsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.peril_type import (
    PerilType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PerilStructureType(BaseIdentifiedComponentType):
    limits: LimitsType | None = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductibles: DeductiblesType | None = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    peril: PerilType | None = field(
        default=None,
        metadata={
            "name": "Peril",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    worldwide_flag: str | None = field(
        default=None,
        metadata={
            "name": "WorldwideFlag",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    state_region_code: str | None = field(
        default=None,
        metadata={
            "name": "StateRegionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    state_region_name: str | None = field(
        default=None,
        metadata={
            "name": "StateRegionName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    country_of_peril_code: str | None = field(
        default=None,
        metadata={
            "name": "CountryOfPerilCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "pattern": r"[A-Z][A-Z]",
        },
    )
    country_of_peril_name: str | None = field(
        default=None,
        metadata={
            "name": "CountryOfPerilName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    zip_code_of_peril: str | None = field(
        default=None,
        metadata={
            "name": "ZipCodeOfPeril",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    included: bool | None = field(
        default=None,
        metadata={
            "name": "Included",
            "type": "Attribute",
        },
    )
