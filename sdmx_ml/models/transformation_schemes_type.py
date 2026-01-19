from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.transformation_scheme_type import TransformationSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class TransformationSchemesType:
    """
    TransformationSchemesType describes the structure of the
    transformations container.

    It contains one or more transformation schemes, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar transformation_scheme: TransformationScheme provides the
        details of a transformation scheme, in which transformations are
        described.
    """

    transformation_scheme: tuple[TransformationSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransformationScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
