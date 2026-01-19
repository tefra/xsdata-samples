from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.description import Description
from sdmx_ml.models.name import Name

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class ValueItemType(AnnotableType):
    """
    ValueItemType defines the structure of a value item.

    A value must be provided, and a longer name and description can be
    provided to provide additional meaning to the value (similar to a code
    in a code list).
    """

    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
