from dataclasses import dataclass, field
from typing import Optional

from .float_mod import Float
from .normalized_instruction import NormalizedInstruction

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DeterministicClientResource:
    """
    This meta-class specifies computing resource needs of
    DeterministicClient library functions.

    :ivar number_of_instructions: This attribute represents the
        normalized runtime consumption on the target system within one
        DeterministicClient::WaitForNextActivation cycle, assuming the
        "worst-case" runtime where the workers would be executed
        sequentially.
    :ivar sequential_instructions_begin: Normalized sequential runtime
        at the beginning of the
        DeterministicClient::WaitForNextActivation cycle (which mostly
        cannot be parallelized), before the main usage of the worker
        pool starts.
    :ivar sequential_instructions_end: WaitForNextActivation cycle
        (which mostly cannot be parallelized), after the main usage of
        the worker pool has ended.
    :ivar speedup: This attribute defines how much faster the
        calculations within one
        DeterministicClient::WaitForNextActivation cycle can be finished
        if numberOfWorkers are physically available, i.e. if enough
        cores were available on the machine to perform parallel
        execution of all workers (sequential runtime / parallelized
        runtime).
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
        name = "DETERMINISTIC-CLIENT-RESOURCE"

    number_of_instructions: Optional[NormalizedInstruction] = field(
        default=None,
        metadata={
            "name": "NUMBER-OF-INSTRUCTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sequential_instructions_begin: Optional[NormalizedInstruction] = field(
        default=None,
        metadata={
            "name": "SEQUENTIAL-INSTRUCTIONS-BEGIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sequential_instructions_end: Optional[NormalizedInstruction] = field(
        default=None,
        metadata={
            "name": "SEQUENTIAL-INSTRUCTIONS-END",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    speedup: Optional[Float] = field(
        default=None,
        metadata={
            "name": "SPEEDUP",
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
