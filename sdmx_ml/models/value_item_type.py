from dataclasses import dataclass, field
from typing import Optional, Tuple

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.description import Description
from sdmx_ml.models.name import Name

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ValueItemType(AnnotableType):
    """ValueItemType defines the structure of a value item.

    A value must be provided, and a longer name and description can be
    provided to provide additiona meaning to the value (similar to a
    code in a code list).
    """

    name: Tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    description: Tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
