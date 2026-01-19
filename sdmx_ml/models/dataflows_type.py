from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.dataflow_type import DataflowType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataflowsType:
    """
    DataflowsType describes the structure of the data flows container.

    It contains one or more data flow, which can be explicitly detailed or
    referenced from an external structure document or registry service.

    :ivar dataflow: Dataflow provides the details of a data flow, which
        is defined as the structure of data that will be provided for
        different reference periods.
    """

    dataflow: tuple[DataflowType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Dataflow",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
