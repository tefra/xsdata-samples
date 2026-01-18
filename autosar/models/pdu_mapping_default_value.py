from __future__ import annotations

from dataclasses import dataclass, field

from .default_value_element import DefaultValueElement

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PduMappingDefaultValue:
    """
    Default Value which will be distributed if no I-Pdu has been received
    since last sending.

    :ivar default_value_elements: The default value consists of a number
        of elements. Each default value element is represented by the
        element and the position in an array.
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
        name = "PDU-MAPPING-DEFAULT-VALUE"

    default_value_elements: (
        None | PduMappingDefaultValue.DefaultValueElements
    ) = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE-ELEMENTS",
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

    @dataclass
    class DefaultValueElements:
        default_value_element: list[DefaultValueElement] = field(
            default_factory=list,
            metadata={
                "name": "DEFAULT-VALUE-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
