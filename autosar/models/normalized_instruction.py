from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NormalizedInstruction:
    """
    This meta-class is used to describe runtime budget needs on the target
    system within DeterministicClient::WaitForNextActivation cycles.

    NormalizedInstructions does not reflect the actual number of code
    instructions, but allows the description of comparative resource needs.
    NormalizedInstructions is used for configuration of computing resources
    at integration time. NormalizedInstruction = runtime in sec * clock
    frequency in Hz.

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
        name = "NORMALIZED-INSTRUCTION"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[1-9][0-9]*",
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
