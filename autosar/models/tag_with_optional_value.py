from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TagWithOptionalValue:
    """
    A tagged value is a combination of a tag (key) and a value that gives
    supplementary information that is attached to a model element.

    Please note that keys without a value are allowed.

    :ivar key: Defines a key.
    :ivar value: Defines the corresponding value.
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
        name = "TAG-WITH-OPTIONAL-VALUE"

    key: None | String = field(
        default=None,
        metadata={
            "name": "KEY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value: None | String = field(
        default=None,
        metadata={
            "name": "VALUE",
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
