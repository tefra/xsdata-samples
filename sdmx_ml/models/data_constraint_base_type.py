from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.constraint_type import ConstraintType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class DataConstraintBaseType(ConstraintType):
    """
    DataConstraintBaseType is an abstract base refinement of
    ConstraintType.

    The constraint attachment is restricted to constrainable artefacts
    related to data.
    """
