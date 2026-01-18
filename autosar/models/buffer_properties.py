from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .compu_scale import CompuScale
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BufferProperties:
    """
    Configuration of the buffer properties the transformer needs to work.

    :ivar buffer_computation: If the transformer changes the size of the
        data, the CompuScale can be used to specify a rule to derive the
        size of the output data based on the size of the input data.
    :ivar header_length: Defines the length of the header (in bits) this
        transformer will add in front of the data.
    :ivar in_place: If set, the transformer uses the input buffer as
        output buffer.
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
        name = "BUFFER-PROPERTIES"

    buffer_computation: CompuScale | None = field(
        default=None,
        metadata={
            "name": "BUFFER-COMPUTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    header_length: Integer | None = field(
        default=None,
        metadata={
            "name": "HEADER-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    in_place: Boolean | None = field(
        default=None,
        metadata={
            "name": "IN-PLACE",
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
