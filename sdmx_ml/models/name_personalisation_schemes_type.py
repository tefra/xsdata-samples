from dataclasses import dataclass, field

from sdmx_ml.models.name_personalisation_scheme_type import (
    NamePersonalisationSchemeType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class NamePersonalisationSchemesType:
    """NamePersonalisationSchemesType describes the structure of the name
    personalisation schemes container.

    It contains one or more name personalisation scheme, which can be
    explicitly detailed or referenced from an external structure
    document or registry service.

    :ivar name_personalisation_scheme: NamePersonalisationScheme
        provides the details of a name personalisation scheme, in which
        name personalisations are described.
    """

    name_personalisation_scheme: tuple[NamePersonalisationSchemeType, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "NamePersonalisationScheme",
                "type": "Element",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                "min_occurs": 1,
            },
        )
    )
