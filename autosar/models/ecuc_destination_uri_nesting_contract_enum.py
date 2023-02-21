from dataclasses import dataclass, field
from typing import Optional
from .ecuc_destination_uri_nesting_contract_enum_simple import EcucDestinationUriNestingContractEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucDestinationUriNestingContractEnum:
    """
    EcucDestinationUriNestingContractEnum is used to determine what is qualified by
    the EcucDestinationUriPolicy.

    :ivar value:
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
        name = "ECUC-DESTINATION-URI-NESTING-CONTRACT-ENUM"

    value: Optional[EcucDestinationUriNestingContractEnumSimple] = field(
        default=None,
        metadata={
            "required": True,
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
