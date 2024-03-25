from dataclasses import dataclass, field
from typing import Optional, Tuple

from sdmx_ml.models.description import Description
from sdmx_ml.models.name import Name

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class SentinelValueType:
    """SentinelValueType defines the structure of a sentinel value.

    A sentinel is a value that has a special meaning within the text
    format representation of a component. The value is associated with a
    multi-lingual name and description.

    :ivar name:
    :ivar description:
    :ivar value: The sentinel value being described.
    """

    name: Tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
            "min_occurs": 1,
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
    value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
