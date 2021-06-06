from dataclasses import dataclass, field
from typing import Optional
from .do_ip_logic_address_subtypes_enum import DoIpLogicAddressSubtypesEnum
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .ref import Ref
from .tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DoIpTpConnection:
    """A connection identifies the sender and the receiver of this particular
    communication.

    The DoIp module routes a tpSdu through this connection.

    :ivar ident: This adds the ability to become referrable to
        TpConnection.
    :ivar do_ip_source_address_ref: Reference to the address of the
        sender of the tpSdu.
    :ivar do_ip_target_address_ref: Reference to the address of the
        receiver of the tpSdu.
    :ivar tp_sdu_ref: This reference is used to describe the data
        exchange between DoIp and the PduR.
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
        name = "DO-IP-TP-CONNECTION"

    ident: Optional[TpConnectionIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    do_ip_source_address_ref: Optional["DoIpTpConnection.DoIpSourceAddressRef"] = field(
        default=None,
        metadata={
            "name": "DO-IP-SOURCE-ADDRESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    do_ip_target_address_ref: Optional["DoIpTpConnection.DoIpTargetAddressRef"] = field(
        default=None,
        metadata={
            "name": "DO-IP-TARGET-ADDRESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tp_sdu_ref: Optional["DoIpTpConnection.TpSduRef"] = field(
        default=None,
        metadata={
            "name": "TP-SDU-REF",
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
    class DoIpSourceAddressRef(Ref):
        dest: Optional[DoIpLogicAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DoIpTargetAddressRef(Ref):
        dest: Optional[DoIpLogicAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TpSduRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
