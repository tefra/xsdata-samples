from __future__ import annotations

from dataclasses import dataclass, field

from .execution_dependency import ExecutionDependency
from .function_group_state_in_function_group_set_instance_ref import (
    FunctionGroupStateInFunctionGroupSetInstanceRef,
)
from .ref import Ref
from .resource_consumption import ResourceConsumption
from .resource_group_subtypes_enum import ResourceGroupSubtypesEnum
from .startup_config_subtypes_enum import StartupConfigSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class StateDependentStartupConfig:
    """
    This meta-class defines the startup configuration for the process
    depending on a collection of machine states.

    :ivar execution_dependencys: This attribute defines that all
        processes that are referenced via the ExecutionDependency shall
        be launched and shall reach a certain ProcessState before the
        referencing process is started.
    :ivar function_group_state_irefs: This represent the applicable
        functionGroupMode.
    :ivar resource_consumption: This aggregation provides the ability to
        define resource consumption boundaries on a per-process-startup-
        config basis.
    :ivar resource_group_ref: Reference to an applicable resource group.
    :ivar startup_config_ref: Reference to a reusable startup
        configuration with startup parameters.
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
        name = "STATE-DEPENDENT-STARTUP-CONFIG"

    execution_dependencys: (
        StateDependentStartupConfig.ExecutionDependencys | None
    ) = field(
        default=None,
        metadata={
            "name": "EXECUTION-DEPENDENCYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    function_group_state_irefs: (
        StateDependentStartupConfig.FunctionGroupStateIrefs | None
    ) = field(
        default=None,
        metadata={
            "name": "FUNCTION-GROUP-STATE-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resource_consumption: ResourceConsumption | None = field(
        default=None,
        metadata={
            "name": "RESOURCE-CONSUMPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    resource_group_ref: StateDependentStartupConfig.ResourceGroupRef | None = (
        field(
            default=None,
            metadata={
                "name": "RESOURCE-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    startup_config_ref: StateDependentStartupConfig.StartupConfigRef | None = (
        field(
            default=None,
            metadata={
                "name": "STARTUP-CONFIG-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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

    @dataclass
    class ExecutionDependencys:
        execution_dependency: list[ExecutionDependency] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-DEPENDENCY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class FunctionGroupStateIrefs:
        function_group_state_iref: list[
            FunctionGroupStateInFunctionGroupSetInstanceRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "FUNCTION-GROUP-STATE-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ResourceGroupRef(Ref):
        dest: ResourceGroupSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class StartupConfigRef(Ref):
        dest: StartupConfigSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
