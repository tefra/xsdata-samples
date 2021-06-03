from dataclasses import dataclass, field
from typing import Optional
from autosar.models.rpt_access_enum import RptAccessEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RptSwPrototypingAccess:
    """
    Describes the accessibility of data and modes by the rapid prototyping
    tooling.

    :ivar rpt_hook_access: The related data element can be modified
        using a post-build hooking tool. An ENABLED
        VariableDataPrototype is implicitly READABLE/WRITABLE.
    :ivar rpt_read_access: The related data element can be used as input
        for bypass functionality by RP tool. If rptImplPolicy is not
        specified then RTE generation shall ensure  at least suitable MC
        read points are created.
    :ivar rpt_write_access: The related data element can be used as
        output for bypass functionality by RP tool. The data element
        shall be prepared to rptLevel2 and related write service points
        are present.
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
        name = "RPT-SW-PROTOTYPING-ACCESS"

    rpt_hook_access: Optional[RptAccessEnum] = field(
        default=None,
        metadata={
            "name": "RPT-HOOK-ACCESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rpt_read_access: Optional[RptAccessEnum] = field(
        default=None,
        metadata={
            "name": "RPT-READ-ACCESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rpt_write_access: Optional[RptAccessEnum] = field(
        default=None,
        metadata={
            "name": "RPT-WRITE-ACCESS",
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
