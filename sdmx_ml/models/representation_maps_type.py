from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.representation_map_type import RepresentationMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class RepresentationMapsType:
    """RepresentationMapsType describes the structure of the representation maps
    container.

    It contains one or more representation map, which can be explicitly
    detailed or referenced from an external structure document or
    registry service.

    :ivar representation_map: RepresentationMap provides the details of
        a represenation map, which describes mappings between various
        component represenations.
    """

    representation_map: Tuple[RepresentationMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RepresentationMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
