from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.simple_component_value_type import SimpleComponentValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CubeKeyValueType(SimpleComponentValueType):
    """
    CubeKeyValueType derives from the SimpleValueType, but does not allow for a
    locale (xml:lang).
    """

    lang: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
