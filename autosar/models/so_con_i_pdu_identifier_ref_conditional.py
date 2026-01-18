from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .ref import Ref
from .so_con_i_pdu_identifier_subtypes_enum import (
    SoConIPduIdentifierSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SoConIPduIdentifierRefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar so_con_i_pdu_identifier_ref:
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
        name = "SO-CON-I-PDU-IDENTIFIER-REF-CONDITIONAL"

    so_con_i_pdu_identifier_ref: (
        None | SoConIPduIdentifierRefConditional.SoConIPduIdentifierRef
    ) = field(
        default=None,
        metadata={
            "name": "SO-CON-I-PDU-IDENTIFIER-REF",
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
    class SoConIPduIdentifierRef(Ref):
        dest: SoConIPduIdentifierSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
