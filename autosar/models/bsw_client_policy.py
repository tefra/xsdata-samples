from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .bsw_module_client_server_entry_subtypes_enum import (
    BswModuleClientServerEntrySubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswClientPolicy:
    """
    The requiredClientServerEntry for which the BSW Scheduler using this
    policy.

    :ivar enable_take_address: If set to true, the BSW Module is able to
        use the API reference for deriving a pointer to an object
    :ivar required_client_server_entry_ref: The
        requiredClientServerEntry for which the BSW Scheduler using this
        policy.
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
        name = "BSW-CLIENT-POLICY"

    enable_take_address: Boolean | None = field(
        default=None,
        metadata={
            "name": "ENABLE-TAKE-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_client_server_entry_ref: BswClientPolicy.RequiredClientServerEntryRef | None = field(
        default=None,
        metadata={
            "name": "REQUIRED-CLIENT-SERVER-ENTRY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class RequiredClientServerEntryRef(Ref):
        dest: BswModuleClientServerEntrySubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
