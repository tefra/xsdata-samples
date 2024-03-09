from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
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
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.perils_structure_type import (
    PerilsStructureType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class RiskInvolvement(BaseIdentifiedComponentType):
    exposures_for: Optional[ExposuresType] = field(
        default=None,
        metadata={
            "name": "ExposuresFor",
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
    deductibles: Optional[DeductiblesType] = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    perils_structure: Optional[PerilsStructureType] = field(
        default=None,
        metadata={
            "name": "PerilsStructure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    local_asset_group: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "LocalAssetGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
