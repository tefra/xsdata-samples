from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.frequency_format_mapping_base_type import (
    FrequencyFormatMappingBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class FrequencyFormatMappingType(FrequencyFormatMappingBaseType):
    frequency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrequencyId",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    date_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatePattern",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
