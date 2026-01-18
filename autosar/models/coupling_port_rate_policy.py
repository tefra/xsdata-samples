from __future__ import annotations

from dataclasses import dataclass, field

from .coupling_port_rate_policy_action_enum import (
    CouplingPortRatePolicyActionEnum,
)
from .ethernet_physical_channel_subtypes_enum import (
    EthernetPhysicalChannelSubtypesEnum,
)
from .positive_integer import PositiveInteger
from .ref import Ref
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CouplingPortRatePolicy:
    """
    Defines a rate policy on a CouplingPort.

    :ivar data_length: Amount of data in bytes (excluding header
        information) that can be received to define the rate policy.
    :ivar policy_action: Defines the action to be performed when this
        rate policy is violated.
    :ivar priority: Defines the priority which this rate policy shall be
        limited on. If no priority is given this rate policy is not
        considering priority.
    :ivar time_interval: Time interval used to define the base of the
        rate policy.
    :ivar v_lan_refs: Defines the VLANs this rate policy shall be
        limited on. If no VLAN is given this rate policy is not
        considering VLAN tags.
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
        name = "COUPLING-PORT-RATE-POLICY"

    data_length: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    policy_action: None | CouplingPortRatePolicyActionEnum = field(
        default=None,
        metadata={
            "name": "POLICY-ACTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    priority: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_interval: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIME-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    v_lan_refs: None | CouplingPortRatePolicy.VLanRefs = field(
        default=None,
        metadata={
            "name": "V-LAN-REFS",
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

    @dataclass
    class VLanRefs:
        v_lan_ref: list[CouplingPortRatePolicy.VLanRefs.VLanRef] = field(
            default_factory=list,
            metadata={
                "name": "V-LAN-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class VLanRef(Ref):
            dest: None | EthernetPhysicalChannelSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
