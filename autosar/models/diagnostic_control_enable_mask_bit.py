from __future__ import annotations

from dataclasses import dataclass, field

from .diagnostic_data_element_subtypes_enum import (
    DiagnosticDataElementSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DiagnosticControlEnableMaskBit:
    """
    This meta-class has the ability to represent one bit in the control
    enable mask record.

    :ivar bit_number: This attribute represents the bit number of the
        bit in the control mask record. Bit number 0 is the most
        significant bit (MSB) in the first byte of the CEMR in the
        network presentation.
    :ivar controlled_data_element_refs: This reference represents the
        collection of DiagnosticDataElements that are controlled by this
        bit of the control mask record.
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
        name = "DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT"

    bit_number: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "BIT-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    controlled_data_element_refs: (
        None | DiagnosticControlEnableMaskBit.ControlledDataElementRefs
    ) = field(
        default=None,
        metadata={
            "name": "CONTROLLED-DATA-ELEMENT-REFS",
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

    @dataclass(kw_only=True)
    class ControlledDataElementRefs:
        controlled_data_element_ref: list[
            DiagnosticControlEnableMaskBit.ControlledDataElementRefs.ControlledDataElementRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTROLLED-DATA-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class ControlledDataElementRef(Ref):
            dest: DiagnosticDataElementSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
