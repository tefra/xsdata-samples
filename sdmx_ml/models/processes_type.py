from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.process_type import ProcessType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class ProcessesType:
    """
    ProcessesType describes the structure of the processes container.

    It contains one or more process, which can be explicitly detailed or
    referenced from an external structure document or registry service.

    :ivar process: Process provides the details of a process, which is a
        scheme which defines or documents the operations performed on
        data in order to validate data or to derive new information
        according to a given set of rules. It is not meant to support
        process automation, but serves as a description of how processes
        occur. The primary use for this structural mechanism is the
        attachment of reference metadata regarding statistical
        processing. This must either contain the full details of the
        category scheme, or provide a name and identification
        information and reference the full details from an external
        structure document or registry service.
    """

    process: tuple[ProcessType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Process",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
