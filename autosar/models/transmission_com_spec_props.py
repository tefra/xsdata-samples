from dataclasses import dataclass, field
from typing import Optional

from .time_value import TimeValue
from .transmission_mode_definition_enum import TransmissionModeDefinitionEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TransmissionComSpecProps:
    """
    This meta-class defines a set of transmission attributes which the application
    software is assumed to implement.

    :ivar data_update_period: This attribute defines the period in which
        the application is assumed to transmit the respective data.
    :ivar minimum_send_interval: This attribute defines the minimum
        interval between two consecutive transmissions of the respective
        data the application is assumed to ensure.
    :ivar transmission_mode: The attribute defines the mode in which the
        application is assumed to transmit the respective data.
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
        name = "TRANSMISSION-COM-SPEC-PROPS"

    data_update_period: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "DATA-UPDATE-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_send_interval: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "MINIMUM-SEND-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_mode: Optional[TransmissionModeDefinitionEnum] = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-MODE",
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
