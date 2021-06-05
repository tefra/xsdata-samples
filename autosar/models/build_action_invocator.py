from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import Sdg
from autosar.models.verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BuildActionInvocator:
    """
    This meta-class represents the ability to specify the invocation of a task
    in a build action.

    :ivar command: This represents the command to invocate the
        processor. Note that this is a generic string which can be
        interpreted properly in the processor environment. Note that it
        is optional due to the fact that some actions are hardwired in
        the environment and do not need an explicit command. On the
        other hand the properties of an invocator can be complex and not
        standardized.
    :ivar sdgs: This represents a general data structure  intended to
        denote parameters for the BuildAction.
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
        name = "BUILD-ACTION-INVOCATOR"

    command: Optional[VerbatimString] = field(
        default=None,
        metadata={
            "name": "COMMAND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sdgs: Optional["BuildActionInvocator.Sdgs"] = field(
        default=None,
        metadata={
            "name": "SDGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class Sdgs:
        sdg: List[Sdg] = field(
            default_factory=list,
            metadata={
                "name": "SDG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
