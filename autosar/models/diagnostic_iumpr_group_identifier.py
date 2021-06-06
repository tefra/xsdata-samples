from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .nmtoken_string import NmtokenString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticIumprGroupIdentifier:
    """
    This meta-class provides the ability to the define the group identifier for
    an IumprGroup.

    :ivar group_id: This attribute shall be taken to define an
        identifier for the IUMPR group. Please note that the value of
        this identifier is driven by regulations outside the scope of
        AUTOSAR and can therefore not be limited to the set of
        characters suitable for a shortName.
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
        name = "DIAGNOSTIC-IUMPR-GROUP-IDENTIFIER"

    group_id: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "GROUP-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
