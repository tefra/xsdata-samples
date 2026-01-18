from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.date_pattern_map_base_type import DatePatternMapBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DatePatternMapType(DatePatternMapBaseType):
    """
    :ivar source_pattern: Describes the source date using conventions
        for describing years, months, days, etc.
    :ivar locale: The locale on which the input will be parsed according
        to the pattern.
    """

    source_pattern: str | None = field(
        default=None,
        metadata={
            "name": "sourcePattern",
            "type": "Attribute",
            "required": True,
        },
    )
    locale: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
