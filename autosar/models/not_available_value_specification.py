from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .identifier import Identifier
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NotAvailableValueSpecification:
    """
    This meta-class provides the ability to specify a ValueSpecification to
    state that the respective element is not available.

    This ability is needed to support the existence of
    ApplicationRecordElements where attribute isOptional ist set to the
    value True.

    :ivar short_label: This can be used to identify particular value
        specifications for human readers, for example elements of a
        record type.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar default_pattern: The content of this attribute shall be used
        to initialize gaps in the memory occupied by a structured data
        type in the case that an NotAvailableValueSpecification is used.
        Note that this pattern is only applied during initialization!
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
        name = "NOT-AVAILABLE-VALUE-SPECIFICATION"

    short_label: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
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
    default_pattern: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "DEFAULT-PATTERN",
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
