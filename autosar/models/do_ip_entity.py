from dataclasses import dataclass, field
from typing import Optional

from .do_ip_entity_role_enum import DoIpEntityRoleEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DoIpEntity:
    """
    ECU providing this infrastructure service is a DoIP-Entity.

    :ivar do_ip_entity_role: Identifies the role in terms of DoIP this
        network-node has.
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
        name = "DO-IP-ENTITY"

    do_ip_entity_role: DoIpEntityRoleEnum | None = field(
        default=None,
        metadata={
            "name": "DO-IP-ENTITY-ROLE",
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
