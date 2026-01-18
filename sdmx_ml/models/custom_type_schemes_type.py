from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.custom_type_scheme_type import CustomTypeSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CustomTypeSchemesType:
    """
    CustomTypeSchemesType describes the structure of the custom type
    schemes container.

    It contains one or more custom type scheme, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar custom_type_scheme: CustomTypeScheme provides the details of a
        custom type scheme, in which user defined operators are
        described.
    """

    custom_type_scheme: tuple[CustomTypeSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CustomTypeScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
