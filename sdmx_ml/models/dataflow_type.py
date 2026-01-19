from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.dataflow_base_type import DataflowBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataflowType(DataflowBaseType):
    """
    DataflowType describes the structure of a data flow.

    Using a DimensionConstraint and/or a DataConstraint a data flow can
    define a subset of data defined by a DataStructure. Unless the dataflow
    artefact is defined externally, a reference to a DataStructure must be
    provided.
    """
