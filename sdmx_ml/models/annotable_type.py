from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.annotations import Annotations

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class AnnotableType:
    """
    AnnotableType is an abstract base type used for all annotable
    artefacts.

    Any type that provides for annotations should extend this type.
    """

    annotations: Annotations | None = field(
        default=None,
        metadata={
            "name": "Annotations",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
