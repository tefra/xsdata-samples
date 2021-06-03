from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.bsw_distinguished_partition_subtypes_enum import BswDistinguishedPartitionSubtypesEnum
from autosar.models.bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from autosar.models.exclusive_area_nesting_order_subtypes_enum import ExclusiveAreaNestingOrderSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswDirectCallPoint:
    """Represents a concrete point in the code from where a BswModuleEntry is
    called directly, i.e. not via the BSW Scheduler.

    This information can be used to analyze call tree and resource
    locking scenarios. It is not needed to configure the BSW Scheduler.

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
    :ivar called_entry_ref: The BswModuleEntry called at this point.
    :ivar called_from_within_exclusive_area_ref: This indicates that the
        call point is located at the deepest level inside one or more
        ExclusiveAreas that are nested in the given order.
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
        name = "BSW-DIRECT-CALL-POINT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["BswDirectCallPoint.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_limitation_refs: Optional["BswDirectCallPoint.ContextLimitationRefs"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-LIMITATION-REFS",
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
    called_entry_ref: Optional["BswDirectCallPoint.CalledEntryRef"] = field(
        default=None,
        metadata={
            "name": "CALLED-ENTRY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    called_from_within_exclusive_area_ref: Optional["BswDirectCallPoint.CalledFromWithinExclusiveAreaRef"] = field(
        default=None,
        metadata={
            "name": "CALLED-FROM-WITHIN-EXCLUSIVE-AREA-REF",
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
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ContextLimitationRefs:
        context_limitation_ref: List["BswDirectCallPoint.ContextLimitationRefs.ContextLimitationRef"] = field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-LIMITATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ContextLimitationRef(Ref):
            dest: Optional[BswDistinguishedPartitionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class CalledEntryRef(Ref):
        dest: Optional[BswModuleEntrySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class CalledFromWithinExclusiveAreaRef(Ref):
        dest: Optional[ExclusiveAreaNestingOrderSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
