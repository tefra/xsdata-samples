from dataclasses import dataclass, field
from typing import Tuple

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class SpaceKeyType:
    """SpaceKey defines the structure of a super- or sub- space for a SDMX
    Dataflow.

    It is a collection of references to the dimensions that make up the
    space.

    :ivar key: A reference to a dimension by its identifier.
    """

    key: Tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
