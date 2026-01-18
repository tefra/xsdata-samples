from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .ref import Ref
from .security_event_filter_chain_subtypes_enum import (
    SecurityEventFilterChainSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SecurityEventFilterChainRefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar security_event_filter_chain_ref:
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
        name = "SECURITY-EVENT-FILTER-CHAIN-REF-CONDITIONAL"

    security_event_filter_chain_ref: (
        None
        | SecurityEventFilterChainRefConditional.SecurityEventFilterChainRef
    ) = field(
        default=None,
        metadata={
            "name": "SECURITY-EVENT-FILTER-CHAIN-REF",
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

    @dataclass(kw_only=True)
    class SecurityEventFilterChainRef(Ref):
        dest: SecurityEventFilterChainSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
