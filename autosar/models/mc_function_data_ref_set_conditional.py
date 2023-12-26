from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .flat_instance_descriptor_subtypes_enum import (
    FlatInstanceDescriptorSubtypesEnum,
)
from .mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McFunctionDataRefSetConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar flat_map_entry_refs: Refers to an entry in a FlatMap that is
        part of the set, for example a calibration parameter or measured
        variable.
    :ivar mc_data_instance_refs: Refers to a data instance within MC
        support data that is part of the set, i.e. a calibration
        parameter or measured variable.
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
        name = "MC-FUNCTION-DATA-REF-SET-CONDITIONAL"

    flat_map_entry_refs: Optional[
        "McFunctionDataRefSetConditional.FlatMapEntryRefs"
    ] = field(
        default=None,
        metadata={
            "name": "FLAT-MAP-ENTRY-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_data_instance_refs: Optional[
        "McFunctionDataRefSetConditional.McDataInstanceRefs"
    ] = field(
        default=None,
        metadata={
            "name": "MC-DATA-INSTANCE-REFS",
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
    class FlatMapEntryRefs:
        flat_map_entry_ref: List[
            "McFunctionDataRefSetConditional.FlatMapEntryRefs.FlatMapEntryRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "FLAT-MAP-ENTRY-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class FlatMapEntryRef(Ref):
            dest: Optional[FlatInstanceDescriptorSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class McDataInstanceRefs:
        mc_data_instance_ref: List[
            "McFunctionDataRefSetConditional.McDataInstanceRefs.McDataInstanceRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "MC-DATA-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class McDataInstanceRef(Ref):
            dest: Optional[McDataInstanceSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
