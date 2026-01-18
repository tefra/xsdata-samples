from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .per_instance_memory_subtypes_enum import PerInstanceMemorySubtypesEnum
from .positive_integer import PositiveInteger
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PerInstanceMemorySize:
    """
    Resources needed by the allocation of PerInstanceMemory for each SWC
    instance.

    Note that these resources are not covered by an ObjectFileSection,
    because they are supposed to be allocated by the RTE.

    :ivar alignment: Required alignment (1,2,4,...) of the referenced
        PerInstanceMemory.  Unit: byte.
    :ivar per_instance_memory_ref: This represents the referenced
        PerInstanceMemory.
    :ivar size: Size (in bytes) of the reference perInstanceMemory. The
        aggregation of PerInstanceMemorySize is subject to variability
        with the purpose to support variability in the software
        components implementations. Different algorithms in the
        implementation might require a different PerInstanceMemorySize.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "PER-INSTANCE-MEMORY-SIZE"

    alignment: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "ALIGNMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    per_instance_memory_ref: (
        None | PerInstanceMemorySize.PerInstanceMemoryRef
    ) = field(
        default=None,
        metadata={
            "name": "PER-INSTANCE-MEMORY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size: None | PositiveIntegerValueVariationPoint = field(
        default=None,
        metadata={
            "name": "SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class PerInstanceMemoryRef(Ref):
        dest: None | PerInstanceMemorySubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
