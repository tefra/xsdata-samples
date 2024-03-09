from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .i_signal_triggering_subtypes_enum import ISignalTriggeringSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ISignalMapping:
    """Arranges those signals (or SignalGroups) that are transferred by the gateway
    from one channel to the other in pairs and defines the mapping between them.

    Each pair consists in a source and a target referencing to a
    ISignalTriggering.

    :ivar introduction: This represents introductory documentation about
        the ISignal mapping.
    :ivar source_signal_ref: Source destination of the referencing
        mapping.
    :ivar target_signal_ref: Target destination of the referencing
        mapping.
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
        name = "I-SIGNAL-MAPPING"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    source_signal_ref: Optional["ISignalMapping.SourceSignalRef"] = field(
        default=None,
        metadata={
            "name": "SOURCE-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_signal_ref: Optional["ISignalMapping.TargetSignalRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class SourceSignalRef(Ref):
        dest: Optional[ISignalTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetSignalRef(Ref):
        dest: Optional[ISignalTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
