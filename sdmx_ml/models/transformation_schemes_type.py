from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.transformation_scheme_type import TransformationSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TransformationSchemesType:
    """TransformationSchemesType describes the structure of the transformations
    container.

    It contains one or more transformation schemes, which can be
    explicitly detailed or referenced from an external structure
    document or registry service.

    :ivar transformation_scheme: TransformationScheme provides the
        details of a transformation scheme, in which transformations are
        described.
    """

    transformation_scheme: Tuple[TransformationSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransformationScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
