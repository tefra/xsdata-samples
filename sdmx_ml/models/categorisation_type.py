from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.categorisation_base_type import CategorisationBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CategorisationType(CategorisationBaseType):
    """CategorisationType is defines the structure for a categorisation.

    A source object is referenced via an object reference and the target
    category is referenced via the target category.

    :ivar source: Source is a reference to an object to be categorized.
    :ivar target: Target is reference to the category that the
        referenced object is to be mapped to.
    """

    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?",
        },
    )
    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.categoryscheme\.Category=.+",
        },
    )
