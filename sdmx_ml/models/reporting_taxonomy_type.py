from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.item_scheme_type import ItemSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ReportingTaxonomyType(ItemSchemeType):
    """
    ReportingTaxonomyType describes the structure of a reporting taxonomy, which is
    a scheme which defines the composition structure of a data report where each
    component can be described by an independent structure or structure usage
    description.
    """

    choice_1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
