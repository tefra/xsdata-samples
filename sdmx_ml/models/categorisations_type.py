from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.categorisation_type import CategorisationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CategorisationsType:
    """CategorisationsType describes the structure of the categorisations
    container.

    It contains one or more categorisation of a specific object type,
    which can be explicitly detailed or referenced from an external
    structure document or registry service. This container may contain
    categorisations for multiple types of structural objects.

    :ivar categorisation: Categorisation allows for the association of
        an identifiable object to a category, providing for the
        classifications of the reference identifiable object. This must
        either contain the full details of the categorisation, or
        provide a name and identification information and reference the
        full details from an external structure document or registry
        service.
    """

    categorisation: Tuple[CategorisationType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Categorisation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
