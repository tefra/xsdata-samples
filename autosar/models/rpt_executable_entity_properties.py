from dataclasses import dataclass, field

from .positive_integer import PositiveInteger
from .rpt_execution_control_enum import RptExecutionControlEnum
from .rpt_service_point_enum import RptServicePointEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RptExecutableEntityProperties:
    """
    Describes the code preparation for rapid prototyping at
    ExecutableEntity invocation.

    :ivar max_rpt_event_id: Highest RPT event id useable for RTE
        generated service points. This attribute is relevant, if
        dedicated id range shall be applied to the ExecutableEntitys of
        a software component or specific ExecutableEntitys.
    :ivar min_rpt_event_id: Lowest RPT event id useable for RTE
        generated service points. This attribute is relevant, if
        dedicated id range shall be applied to the ExecutableEntitys of
        a software component or specific ExecutableEntitys.
    :ivar rpt_execution_control: This attribute specifies the rapid
        prototyping control of the executable
    :ivar rpt_service_point: Enables generation of service points by the
        RTE generator.
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
        name = "RPT-EXECUTABLE-ENTITY-PROPERTIES"

    max_rpt_event_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MAX-RPT-EVENT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_rpt_event_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MIN-RPT-EVENT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_execution_control: RptExecutionControlEnum | None = field(
        default=None,
        metadata={
            "name": "RPT-EXECUTION-CONTROL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_service_point: RptServicePointEnum | None = field(
        default=None,
        metadata={
            "name": "RPT-SERVICE-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
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
