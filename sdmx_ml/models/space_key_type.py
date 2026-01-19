from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class SpaceKeyType:
    """
    SpaceKey defines the structure of a super- or sub- space for a SDMX
    Dataflow.

    It is a collection of references to the dimensions that make up the
    space.

    :ivar key: A reference to a dimension by its identifier.
    """

    key: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
