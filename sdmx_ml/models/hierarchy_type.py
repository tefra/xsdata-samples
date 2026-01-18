from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.hierarchical_code_type import HierarchicalCodeType
from sdmx_ml.models.hierarchy_base_type import HierarchyBaseType
from sdmx_ml.models.level_type import LevelType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class HierarchyType(HierarchyBaseType):
    """
    HierarchyType describes the structure of a hierarchical codelist.

    A hierarchical code list is defined as an organised collection of codes
    that may participate in many parent/child relationships with other
    codes in the list.

    :ivar level: In a formally leveled hierarchy, Level describes a
        group of codes which are characterised by homogeneous coding,
        and where the parent of each code in the group is at the same
        higher level of the hierarchy. In a value based hierarchy Level
        describes information about the codes at the specified nesting
        level. This structure is recursive to indicate the hierarchy of
        the levels.
    :ivar hierarchical_code: HierarchicalCode is used to assemble the
        codes from the codelist(s) referenced into a hierarchy.
    :ivar has_formal_levels: If “true”, this indicates a hierarchy where
        the structure is arranged in levels of detail from the broadest
        to the most detailed level. If “false”, this indicates a
        hierarchy structure where the items in the hierarchy have no
        formal level structure.
    """

    level: None | LevelType = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    hierarchical_code: tuple[HierarchicalCodeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HierarchicalCode",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
    has_formal_levels: bool = field(
        metadata={
            "name": "hasFormalLevels",
            "type": "Attribute",
            "required": True,
        }
    )
