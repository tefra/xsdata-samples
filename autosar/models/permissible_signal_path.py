from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .physical_channel_subtypes_enum import PhysicalChannelSubtypesEnum
from .ref import Ref
from .swc_to_swc_operation_arguments import SwcToSwcOperationArguments
from .swc_to_swc_signal import SwcToSwcSignal

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PermissibleSignalPath:
    """
    The PermissibleSignalPath describes the way a data element shall take
    in the topology.

    The path is described by ordered references to PhysicalChannels. If
    more than one PermissibleSignalPath is defined for the same
    signal/operation attributes, any of them can be chosen. Such a signal
    path can be a constraint for the communication matrix . This path
    describes that one data element should take path A (e.g. 1. CAN
    channel, 2. LIN channel) and not path B (1. CAN channel, FlexRay
    channel A). This has an effect on the frame generation and the frame
    path.

    :ivar introduction: This represents introductory documentation about
        the signal path constraint.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar operations: The arguments of an operation that can take the
        predefined way in the topology.
    :ivar physical_channel_refs: The SwcToSwcSignal can be transmitted
        on one of these physical channels.
    :ivar signals: The data element which can take the predefined way in
        the topology.
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
        name = "PERMISSIBLE-SIGNAL-PATH"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
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
    operations: Optional["PermissibleSignalPath.Operations"] = field(
        default=None,
        metadata={
            "name": "OPERATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    physical_channel_refs: Optional[
        "PermissibleSignalPath.PhysicalChannelRefs"
    ] = field(
        default=None,
        metadata={
            "name": "PHYSICAL-CHANNEL-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signals: Optional["PermissibleSignalPath.Signals"] = field(
        default=None,
        metadata={
            "name": "SIGNALS",
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
    class Operations:
        swc_to_swc_operation_arguments: list[SwcToSwcOperationArguments] = (
            field(
                default_factory=list,
                metadata={
                    "name": "SWC-TO-SWC-OPERATION-ARGUMENTS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class PhysicalChannelRefs:
        physical_channel_ref: list[
            "PermissibleSignalPath.PhysicalChannelRefs.PhysicalChannelRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "PHYSICAL-CHANNEL-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PhysicalChannelRef(Ref):
            dest: Optional[PhysicalChannelSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class Signals:
        swc_to_swc_signal: list[SwcToSwcSignal] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-SWC-SIGNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
