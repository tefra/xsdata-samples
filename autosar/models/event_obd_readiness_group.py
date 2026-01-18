from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .nmtoken_string import NmtokenString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EventObdReadinessGroup:
    """
    This meta-class represents the ability to define the value of attribute
    eventObdReadinessGroup.

    It is only introduced to allow for a variant modeling of this
    attribute.

    :ivar event_obd_readiness_group: This attribute specifies the Event
        OBD Readiness group for PID $01 and PID $41 computation. This
        attribute is only applicable for emission-related ECUs.
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
        name = "EVENT-OBD-READINESS-GROUP"

    event_obd_readiness_group: None | NmtokenString = field(
        default=None,
        metadata={
            "name": "EVENT-OBD-READINESS-GROUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
