from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.item_scheme_type import ItemSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CodelistBaseType(ItemSchemeType):
    """CodelistType defines the structure of a codelist.

    A codelist is defined as a list from which some statistical concepts
    (coded concepts) take their values.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
