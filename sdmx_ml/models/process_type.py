from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.process_base_type import ProcessBaseType
from sdmx_ml.models.process_step_type import ProcessStepType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ProcessType(ProcessBaseType):
    """ProcessType describes the structure of a process, which is a scheme which
    defines or documents the operations performed on data in order to validate data
    or to derive new information according to a given set of rules.

    Processes occur in order, and will continue in order unless a
    transition dictates another step should occur.

    :ivar process_step: ProcessStep defines a process step, which is a
        specific operation, performed on data in order to validate or to
        derive new information according to a given set of rules.
    """

    process_step: Tuple[ProcessStepType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProcessStep",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
