from __future__ import annotations

from dataclasses import dataclass, field

from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ReceptionComSpecProps:
    """
    This meta-class defines a set of reception attributes which the
    application software is assumed to implement.

    :ivar data_update_period: This attribute defines the period in which
        the application shall check for updated data. This attribute is
        used for the configuration of the E2E protection, but may also
        indicate a general data reception period.
    :ivar timeout: This attribute defines the time interval after which
        the application shall assume that the to be received data
        reception has timed out, i.e. the respective data has not been
        received for that amount of time.
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
        name = "RECEPTION-COM-SPEC-PROPS"

    data_update_period: None | TimeValue = field(
        default=None,
        metadata={
            "name": "DATA-UPDATE-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIMEOUT",
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
