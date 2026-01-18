from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import DocumentationBlock
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class BlueprintPolicyList:
    """
    The class represents that the related attribute is modifiable during
    the blueprinting.

    It applies only to attribute with upper multiplicity greater than 1.

    :ivar attribute_name: This identifies the related attribute of a
        BlueprintPolicy. For navigation over the model a subset of xpath
        expressions is used.
    :ivar blueprint_derivation_guide: This role offers the possibility
        to give addtional information to the policy.
    :ivar max_number_of_elements: Maximum number of elements in list. If
        the maximum number is not constraint it shall be set to
        "undefined".
    :ivar min_number_of_elements: Minimum number of elements in the
        list. If the minimum number is not constraint it shall be set to
        "undefined".
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
        name = "BLUEPRINT-POLICY-LIST"

    attribute_name: None | String = field(
        default=None,
        metadata={
            "name": "ATTRIBUTE-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blueprint_derivation_guide: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-DERIVATION-GUIDE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_of_elements: None | PositiveIntegerValueVariationPoint = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_number_of_elements: None | PositiveIntegerValueVariationPoint = field(
        default=None,
        metadata={
            "name": "MIN-NUMBER-OF-ELEMENTS",
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
