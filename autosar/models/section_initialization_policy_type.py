from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SectionInitializationPolicyType:
    """
    SectionInitializationPolicyType describes the intended initialization
    of MemorySections.

    The following values are standardized in AUTOSAR Methodology: *
    '''NO-INIT''': No initialization and no clearing is performed. Such
    data elements shall not be read before one has written a value into it.
    * '''INIT''': To be used for data that are initialized by every reset
    to the specified value (initValue). * '''POWER-ON-INIT''': To be used
    for data that are initialized by "Power On" to the specified value
    (initValue). Note: there might be several resets between power on
    resets. * '''CLEARED''': To be used for data that are initialized by
    every reset to zero. * '''POWER-ON-CLEARED''': To be used for data that
    are initialized by "Power On" to zero. Note: there might be several
    resets between power on resets. Please note that the values are defined
    similar to the representation of enumeration types in the XML schema to
    ensure backward compatibility.

    :ivar value:
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
        name = "SECTION-INITIALIZATION-POLICY-TYPE"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
