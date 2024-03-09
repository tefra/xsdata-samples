from dataclasses import dataclass, field
from typing import Optional

from .argument_data_prototype_subtypes_enum import (
    ArgumentDataPrototypeSubtypesEnum,
)
from .ref import Ref
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ClientServerPrimitiveTypeMapping:
    """
    Mapping of an argument with a primitive datatype to a signal.

    :ivar argument_ref: Reference to an argument in the context of the
        mappedOperation.
    :ivar system_signal_ref: Reference to the system signal used to
        carry the argument
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
        name = "CLIENT-SERVER-PRIMITIVE-TYPE-MAPPING"

    argument_ref: Optional["ClientServerPrimitiveTypeMapping.ArgumentRef"] = (
        field(
            default=None,
            metadata={
                "name": "ARGUMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    system_signal_ref: Optional[
        "ClientServerPrimitiveTypeMapping.SystemSignalRef"
    ] = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ArgumentRef(Ref):
        dest: Optional[ArgumentDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SystemSignalRef(Ref):
        dest: Optional[SystemSignalSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
