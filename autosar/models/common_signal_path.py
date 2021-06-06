from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    DocumentationBlock,
    VariationPoint,
)
from .swc_to_swc_operation_arguments import SwcToSwcOperationArguments
from .swc_to_swc_signal import SwcToSwcSignal

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CommonSignalPath:
    """
    The CommonSignalPath describes that two or more SwcToSwcSignals and/or
    SwcToSwcOperationArguments shall take the same way (Signal Path) in the
    topology.

    :ivar introduction: This represents introductory documentation about
        the signal path constraint.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar operations: The arguments sent in one direction (either from
        client to server or server to client) of the operations that
        shall take the same signal path.
    :ivar signals: The SwcToSwcSignals that shall take the same way
        (Signal Path) in the topology.
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
        name = "COMMON-SIGNAL-PATH"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    operations: Optional["CommonSignalPath.Operations"] = field(
        default=None,
        metadata={
            "name": "OPERATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    signals: Optional["CommonSignalPath.Signals"] = field(
        default=None,
        metadata={
            "name": "SIGNALS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class Operations:
        swc_to_swc_operation_arguments: List[SwcToSwcOperationArguments] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-SWC-OPERATION-ARGUMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Signals:
        swc_to_swc_signal: List[SwcToSwcSignal] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-SWC-SIGNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
