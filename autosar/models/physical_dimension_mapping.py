from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .physical_dimension_subtypes_enum import PhysicalDimensionSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PhysicalDimensionMapping:
    """
    This class represents a specific mapping between two
    PhysicalDimensions.

    :ivar first_physical_dimension_ref: This represents the first
        PhysicalDimension of the enclosing PhysicalDimensionMapping.
    :ivar second_physical_dimension_ref: This represents the first
        PhysicalDimension of the enclosing PhysicalDimensionMapping.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "PHYSICAL-DIMENSION-MAPPING"

    first_physical_dimension_ref: PhysicalDimensionMapping.FirstPhysicalDimensionRef | None = field(
        default=None,
        metadata={
            "name": "FIRST-PHYSICAL-DIMENSION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_physical_dimension_ref: PhysicalDimensionMapping.SecondPhysicalDimensionRef | None = field(
        default=None,
        metadata={
            "name": "SECOND-PHYSICAL-DIMENSION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class FirstPhysicalDimensionRef(Ref):
        dest: PhysicalDimensionSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecondPhysicalDimensionRef(Ref):
        dest: PhysicalDimensionSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
