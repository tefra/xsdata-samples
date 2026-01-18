from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbotype import (
    BaseGbotype,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.exposure_item_type import (
    ExposureItemType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.line_of_business_detail_type import (
    LineOfBusinessDetailType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.specification_base_type import (
    SpecificationBaseType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class ExposureSpecificationType(BaseGbotype):
    specification_base: None | SpecificationBaseType = field(
        default=None,
        metadata={
            "name": "SpecificationBase",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    line_of_business: None | LineOfBusinessDetailType = field(
        default=None,
        metadata={
            "name": "LineOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    item: None | ExposureItemType = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
