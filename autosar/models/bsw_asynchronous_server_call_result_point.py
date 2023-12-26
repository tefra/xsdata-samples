from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .bsw_asynchronous_server_call_point_subtypes_enum import (
    BswAsynchronousServerCallPointSubtypesEnum,
)
from .bsw_distinguished_partition_subtypes_enum import (
    BswDistinguishedPartitionSubtypesEnum,
)
from .identifier import Identifier
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswAsynchronousServerCallResultPoint:
    """
    The callback point for an BswAsynchronousServerCallPoint i.e. the point at
    which the result can be retrieved from the BSW Scheduler.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar context_limitation_refs: The existence of this reference
        indicates that the call point is used only in the context of the
        referred BswDistinguishedPartitions.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar asynchronous_server_call_point_ref: The call point invoking
        the call to which the result belongs.
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
        name = "BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "BswAsynchronousServerCallResultPoint.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_limitation_refs: Optional[
        "BswAsynchronousServerCallResultPoint.ContextLimitationRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTEXT-LIMITATION-REFS",
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
    asynchronous_server_call_point_ref: Optional[
        "BswAsynchronousServerCallResultPoint.AsynchronousServerCallPointRef"
    ] = field(
        default=None,
        metadata={
            "name": "ASYNCHRONOUS-SERVER-CALL-POINT-REF",
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
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ContextLimitationRefs:
        context_limitation_ref: List[
            "BswAsynchronousServerCallResultPoint.ContextLimitationRefs.ContextLimitationRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-LIMITATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ContextLimitationRef(Ref):
            dest: Optional[BswDistinguishedPartitionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class AsynchronousServerCallPointRef(Ref):
        dest: Optional[BswAsynchronousServerCallPointSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
