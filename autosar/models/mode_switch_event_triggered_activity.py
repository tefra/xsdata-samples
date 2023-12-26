from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .identifier import Identifier
from .ref import Ref
from .swc_mode_switch_event_subtypes_enum import SwcModeSwitchEventSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeSwitchEventTriggeredActivity:
    """
    This meta-class defines an activity of the NvBlockSwComponentType for a
    specific NvBlock which is triggered by a ModeSwitchEvent.

    :ivar role: This attribute indicates which service of the NvM for
        the NvBlock shall be requested.
    :ivar swc_mode_switch_event_ref: This reference identifies the
        SwcModeSwitchEvent that triggers the activity.
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
        name = "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY"

    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    swc_mode_switch_event_ref: Optional[
        "ModeSwitchEventTriggeredActivity.SwcModeSwitchEventRef"
    ] = field(
        default=None,
        metadata={
            "name": "SWC-MODE-SWITCH-EVENT-REF",
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
    class SwcModeSwitchEventRef(Ref):
        dest: Optional[SwcModeSwitchEventSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
