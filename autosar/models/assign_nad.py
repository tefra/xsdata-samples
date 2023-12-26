from dataclasses import dataclass, field
from typing import Optional
from .annotation import DocumentationBlock
from .integer import Integer
from .lin_slave_config_ident_subtypes_enum import (
    LinSlaveConfigIdentSubtypesEnum,
)
from .lin_slave_subtypes_enum import LinSlaveSubtypesEnum
from .ref import Ref
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AssignNad:
    """
    Schedule entry for an Assign NAD master request.

    :ivar introduction: This represents introductory documentation about
        the schedule table entry.
    :ivar delay: Relative delay between this tableEntry and the start of
        the successor in the schedule table in seconds.
    :ivar position_in_table: Relative position in the schedule table.
        The first entry index in the schedule table is 0.
    :ivar assigned_controller_ref: The LIN slaves controller who is
        target of this assignment. Optional in case
        LinConfigurationEntry.assignedLinSlaveConfig exists.
    :ivar assigned_lin_slave_config_ref: The LIN slave that is target of
        this assignment. Please note that this reference is redundant to
        the assignedController reference. In an Ecu Extract of the
        LinMaster the LinSlave Ecus shall not be available. The
        information that is described here is necessary in the ECU
        Extract for the configuration of the LinMaster.
    :ivar new_nad: The newly assigned NAD value.
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
        name = "ASSIGN-NAD"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    delay: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    position_in_table: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "POSITION-IN-TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    assigned_controller_ref: Optional[
        "AssignNad.AssignedControllerRef"
    ] = field(
        default=None,
        metadata={
            "name": "ASSIGNED-CONTROLLER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    assigned_lin_slave_config_ref: Optional[
        "AssignNad.AssignedLinSlaveConfigRef"
    ] = field(
        default=None,
        metadata={
            "name": "ASSIGNED-LIN-SLAVE-CONFIG-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    new_nad: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "NEW-NAD",
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

    @dataclass
    class AssignedControllerRef(Ref):
        dest: Optional[LinSlaveSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class AssignedLinSlaveConfigRef(Ref):
        dest: Optional[LinSlaveConfigIdentSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
