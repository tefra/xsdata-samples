from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .diagnostic_data_identifier_set_subtypes_enum import (
    DiagnosticDataIdentifierSetSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticDataIdentifierSetRefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar diagnostic_data_identifier_set_ref:
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
        name = "DIAGNOSTIC-DATA-IDENTIFIER-SET-REF-CONDITIONAL"

    diagnostic_data_identifier_set_ref: (
        DiagnosticDataIdentifierSetRefConditional.DiagnosticDataIdentifierSetRef
        | None
    ) = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-DATA-IDENTIFIER-SET-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class DiagnosticDataIdentifierSetRef(Ref):
        dest: DiagnosticDataIdentifierSetSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
