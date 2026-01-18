from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotations import Annotations

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True, kw_only=True)
class AnnotableType:
    """
    AnnotableType is an abstract base type used for all annotable
    artefacts.

    Any type that provides for annotations should extend this type.
    """

    annotations: None | Annotations = field(
        default=None,
        metadata={
            "name": "Annotations",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
