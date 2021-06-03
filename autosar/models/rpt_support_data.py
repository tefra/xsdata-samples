from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.rpt_component import RptComponent
from autosar.models.rpt_execution_context import RptExecutionContext
from autosar.models.rpt_service_point import RptServicePoint

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RptSupportData:
    """Root element for rapid prototyping support data related to one
    Implementation artifact on an ECU, in particular the RTE.

    The rapid prototyping support data may reference to elements
    provided for McSupportData.

    :ivar execution_contexts: Defines an environment for the execution
        of ExecutableEntites.
    :ivar rpt_components: Description of components for which rapid
        prototyping support is implemented. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar rpt_service_points: This aggregation represents the collection
        of service points associated with the enclosing RptSuportData
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
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
        name = "RPT-SUPPORT-DATA"

    execution_contexts: Optional["RptSupportData.ExecutionContexts"] = field(
        default=None,
        metadata={
            "name": "EXECUTION-CONTEXTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rpt_components: Optional["RptSupportData.RptComponents"] = field(
        default=None,
        metadata={
            "name": "RPT-COMPONENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rpt_service_points: Optional["RptSupportData.RptServicePoints"] = field(
        default=None,
        metadata={
            "name": "RPT-SERVICE-POINTS",
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
    class ExecutionContexts:
        rpt_execution_context: List[RptExecutionContext] = field(
            default_factory=list,
            metadata={
                "name": "RPT-EXECUTION-CONTEXT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class RptComponents:
        rpt_component: List[RptComponent] = field(
            default_factory=list,
            metadata={
                "name": "RPT-COMPONENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class RptServicePoints:
        rpt_service_point: List[RptServicePoint] = field(
            default_factory=list,
            metadata={
                "name": "RPT-SERVICE-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
