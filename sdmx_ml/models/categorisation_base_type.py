from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class CategorisationBaseType(MaintainableType):
    """
    CategorisationBaseType defines the base refinement of the
    CategorisationType.

    Its purpose is to restrict the urn attribute.
    """

    version: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
