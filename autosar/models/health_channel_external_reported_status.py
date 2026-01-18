from __future__ import annotations

from dataclasses import dataclass, field

from .phm_health_channel_status_subtypes_enum import (
    PhmHealthChannelStatusSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class HealthChannelExternalReportedStatus:
    """
    This element defines a health channel representing the status of an
    external health channel.

    :ivar status_id: Defines the numeric value which is used to identify
        the reporting of this HealthChannelExternalReportedStatus to the
        Phm.
    :ivar status_ref: Reference to one status of a PhmHealthChannel.
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
        name = "HEALTH-CHANNEL-EXTERNAL-REPORTED-STATUS"

    status_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "STATUS-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    status_ref: None | HealthChannelExternalReportedStatus.StatusRef = field(
        default=None,
        metadata={
            "name": "STATUS-REF",
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

    @dataclass(kw_only=True)
    class StatusRef(Ref):
        dest: PhmHealthChannelStatusSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
