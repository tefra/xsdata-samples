from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.structures import Structures

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry"


@dataclass(frozen=True, kw_only=True)
class StructuralEventType:
    """
    StructuralEventType provides the details of a structure event,
    specifically the object that changed.

    :ivar structures: Structures contains the details of the structural
        object that has triggered the event. Although this container
        allows for multiple structural objects, it should only contain
        the one changed object.
    """

    structures: None | Structures = field(
        default=None,
        metadata={
            "name": "Structures",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
        },
    )
