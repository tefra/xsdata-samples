from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswModeReceiverPolicy:
    """
    Specifies the details for the reception of a mode switch for the referred mode
    group.

    :ivar enhanced_mode_api: This controls the creation of the enhanced
        mode API that returns information about the previous mode and
        the next mode. If set to TRUE the enhanced mode API is supposed
        to be generated. For more details please refer to the SWS_RTE.
    :ivar required_mode_group_ref: The required mode group for which the
        policy is specified.
    :ivar supports_asynchronous_mode_switch: Specifies whether the
        module can handle the reception of an asynchronous mode switch
        (true) or not (false).
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
        name = "BSW-MODE-RECEIVER-POLICY"

    enhanced_mode_api: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ENHANCED-MODE-API",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_mode_group_ref: Optional[
        "BswModeReceiverPolicy.RequiredModeGroupRef"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-MODE-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    supports_asynchronous_mode_switch: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH",
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
    class RequiredModeGroupRef(Ref):
        dest: Optional[ModeDeclarationGroupPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
