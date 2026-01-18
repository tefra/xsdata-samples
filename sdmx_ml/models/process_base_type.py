from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ProcessBaseType(MaintainableType):
    """
    ProcessBaseType defines the base refinement of the ProcessType.

    Its purpose is to retrict the urn attribute.
    """
