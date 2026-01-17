from dataclasses import dataclass, field
from typing import Any, Optional

from sdmx_ml.models.structured_text import StructuredText
from sdmx_ml.models.text import Text
from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class BooleanValueType(ValueType):
    """
    BooleanValueType is a refinement of SimpleValueType limiting the
    content to be a boolean.
    """

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[bool] = field(default=None)
