from dataclasses import dataclass, field

from sdmx_ml.models.structure_map_type import StructureMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class StructureMapsType:
    """StructureMapsType describes the structure of the structure maps container.

    It contains one or more structure maps, which can be explicitly
    detailed or referenced from an external structure document or
    registry service.

    :ivar structure_map: StructureMap provides the details or a
        structure map, which describes mapping between data structures
        or dataflows.
    """

    structure_map: tuple[StructureMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "StructureMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
