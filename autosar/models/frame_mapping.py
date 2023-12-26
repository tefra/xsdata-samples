from dataclasses import dataclass, field
from typing import Optional
from .annotation import (
    DocumentationBlock,
    VariationPoint,
)
from .frame_triggering_subtypes_enum import FrameTriggeringSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FrameMapping:
    """The entire source frame is mapped as it is onto the target frame (what in
    general is only possible inside of a common platform).

    In this case source and target frame should be the identical object.
    Each pair consists in a SOURCE and a TARGET referencing to a
    FrameTriggering. The Frame Mapping is not supported by the Autosar
    BSW. The existence is optional and has been incorporated into the
    System Template mainly for compatibility in order to allow
    interchange between FIBEX and AUTOSAR descriptions.

    :ivar introduction: This represents introductory documentation about
        the frame mapping.
    :ivar source_frame_ref: Source destination of the referencing
        mapping.
    :ivar target_frame_ref: Target destination of the referencing
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
        name = "FRAME-MAPPING"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    source_frame_ref: Optional["FrameMapping.SourceFrameRef"] = field(
        default=None,
        metadata={
            "name": "SOURCE-FRAME-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_frame_ref: Optional["FrameMapping.TargetFrameRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-FRAME-REF",
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
    class SourceFrameRef(Ref):
        dest: Optional[FrameTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetFrameRef(Ref):
        dest: Optional[FrameTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
