from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .swc_to_swc_operation_arguments import SwcToSwcOperationArguments
from .swc_to_swc_signal import SwcToSwcSignal

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SeparateSignalPath:
    """The SeparateSignalPath describes that two SwcToSwcSignals and/or
    SwcToSwcOperationArguments shall not take the same way (Signal Path) in the
    topology (e.g. Redundancy).

    This means that the signals are not allowed to share even a single
    physical channel in their path.

    :ivar introduction: This represents introductory documentation about
        the signal path constraint.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar operations: The SwcToSwcOperationArguments that shall not take
        the same way (Signal Path) in the topology.
    :ivar signals: The SwcToSwcSignals that shall not take the same way
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
        name = "SEPARATE-SIGNAL-PATH"

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
    operations: Optional["SeparateSignalPath.Operations"] = field(
        default=None,
        metadata={
            "name": "OPERATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signals: Optional["SeparateSignalPath.Signals"] = field(
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
    class Signals:
        swc_to_swc_signal: list[SwcToSwcSignal] = field(
            default_factory=list,
            metadata={
                "name": "SWC-TO-SWC-SIGNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
