from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.measure_type import (
    MeasureType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.simple_uom_amount_of_information_code_type import (
    SimpleUomAmountOfInformationCodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class AttachmentTypeSizeMeasure(MeasureType):
    class Meta:
        global_type = False

    unit_code: SimpleUomAmountOfInformationCodeType = field(
        metadata={
            "name": "unitCode",
            "type": "Attribute",
            "required": True,
        }
    )
