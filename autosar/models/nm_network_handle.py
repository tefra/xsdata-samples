from __future__ import annotations

from dataclasses import dataclass, field

from .ethernet_communication_connector_subtypes_enum import (
    EthernetCommunicationConnectorSubtypesEnum,
)
from .identifier import Identifier
from .pnc_mapping_ident_subtypes_enum import PncMappingIdentSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NmNetworkHandle:
    """
    Group of partialNetworks and/or VLANs that can be controlled
    collectively.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar partial_network_refs: Reference to a Partial Network that is
        included in the NmNetworkHandle.
    :ivar vlan_refs: Reference to a VLAN that is included in the
        NmNetworkHandle.
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
        name = "NM-NETWORK-HANDLE"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: NmNetworkHandle.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    partial_network_refs: NmNetworkHandle.PartialNetworkRefs | None = field(
        default=None,
        metadata={
            "name": "PARTIAL-NETWORK-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vlan_refs: NmNetworkHandle.VlanRefs | None = field(
        default=None,
        metadata={
            "name": "VLAN-REFS",
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
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PartialNetworkRefs:
        partial_network_ref: list[
            NmNetworkHandle.PartialNetworkRefs.PartialNetworkRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "PARTIAL-NETWORK-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PartialNetworkRef(Ref):
            dest: PncMappingIdentSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class VlanRefs:
        vlan_ref: list[NmNetworkHandle.VlanRefs.VlanRef] = field(
            default_factory=list,
            metadata={
                "name": "VLAN-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class VlanRef(Ref):
            dest: EthernetCommunicationConnectorSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
