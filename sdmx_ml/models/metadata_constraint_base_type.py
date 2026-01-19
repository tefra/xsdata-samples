from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.constraint_type import ConstraintType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MetadataConstraintBaseType(ConstraintType):
    """
    MetadataConstraintBaseType is an abstract base refinement of
    ConstraintType to define allowed metadata content.

    The constraint attachment is restricted to constrainable artefacts
    related to metadata.
    """
