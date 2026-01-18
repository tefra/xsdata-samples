from __future__ import annotations

from dataclasses import dataclass, field

from .hw_element_subtypes_enum import HwElementSubtypesEnum
from .memory_section_subtypes_enum import MemorySectionSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MemorySectionLocation:
    """
    Specifies in which hardware ProvidedMemorySegment the
    softwareMemorySection is located.

    :ivar provided_memory_ref: Reference to the hardware
        ProvidedMemorySegment.
    :ivar software_memory_section_ref: Reference to the MemorySection
        which is mapped on a certain hardware memory segment.
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
        name = "MEMORY-SECTION-LOCATION"

    provided_memory_ref: None | MemorySectionLocation.ProvidedMemoryRef = (
        field(
            default=None,
            metadata={
                "name": "PROVIDED-MEMORY-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    software_memory_section_ref: (
        None | MemorySectionLocation.SoftwareMemorySectionRef
    ) = field(
        default=None,
        metadata={
            "name": "SOFTWARE-MEMORY-SECTION-REF",
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
    class ProvidedMemoryRef(Ref):
        dest: None | HwElementSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SoftwareMemorySectionRef(Ref):
        dest: None | MemorySectionSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
