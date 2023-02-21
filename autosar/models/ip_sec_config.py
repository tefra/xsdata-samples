from dataclasses import dataclass, field
from typing import List, Optional
from .ip_sec_config_props_subtypes_enum import IpSecConfigPropsSubtypesEnum
from .ip_sec_rule import IpSecRule
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IpSecConfig:
    """
    IPsec is a protocol that is designed to provide "end-to-end" cryptographically-
    based security for IP network connections.

    :ivar ip_sec_config_props_ref: Global IPsec configuration settings
        that are valid for all IPSecRules that are defined on the
        NetworkEndpoint.
    :ivar ip_sec_rules: IPSec rules and filters that are defined in the
        IPSecConfig for a specific NetworkEndpoint.
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
        name = "IP-SEC-CONFIG"

    ip_sec_config_props_ref: Optional["IpSecConfig.IpSecConfigPropsRef"] = field(
        default=None,
        metadata={
            "name": "IP-SEC-CONFIG-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ip_sec_rules: Optional["IpSecConfig.IpSecRules"] = field(
        default=None,
        metadata={
            "name": "IP-SEC-RULES",
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
    class IpSecConfigPropsRef(Ref):
        dest: Optional[IpSecConfigPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class IpSecRules:
        ip_sec_rule: List[IpSecRule] = field(
            default_factory=list,
            metadata={
                "name": "IP-SEC-RULE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
