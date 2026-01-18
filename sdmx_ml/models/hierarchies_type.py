from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.hierarchy_type import HierarchyType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class HierarchiesType:
    """
    HierarchiesType describes the structure of the hierarchies container.

    It contains one or more hierarchy, which can be explicitly detailed or
    referenced from an external structure document or registry service.

    :ivar hierarchy: Hierarchy provides the details of a hierarchy,
        which is defined as an organised collection of codes that may
        participate in many parent/child relationships with other codes
        in the list.
    """

    hierarchy: tuple[HierarchyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Hierarchy",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
