from dataclasses import dataclass, field
from typing import Optional
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class HardwareConfiguration:
    """
    Describes in which mode the hardware is operating while needing this resource
    consumption.

    :ivar additional_information: Specifies additional information on
        the HardwareConfiguration.
    :ivar processor_mode: Specifies in which mode the processor is
        operating.
    :ivar processor_speed: Specifies the speed the processor is
        operating.
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
        name = "HARDWARE-CONFIGURATION"

    additional_information: Optional[String] = field(
        default=None,
        metadata={
            "name": "ADDITIONAL-INFORMATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    processor_mode: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROCESSOR-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    processor_speed: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROCESSOR-SPEED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
