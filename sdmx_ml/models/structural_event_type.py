from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.structures import Structures

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class StructuralEventType:
    """
    StructuralEventType provides the details of a structure event, specifically the
    object that changed.

    :ivar structures: Structures contains the details of the structural
        object that has triggered the event. Although this container
        allows for multiple structural object, it should only contain
        the one changed object.
    """

    structures: Optional[Structures] = field(
        default=None,
        metadata={
            "name": "Structures",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
