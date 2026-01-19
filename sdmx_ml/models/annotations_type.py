from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotation_type import AnnotationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


@dataclass(frozen=True, kw_only=True)
class AnnotationsType:
    """
    AnnotationsType provides for a list of annotations to be attached to
    data and structure messages.
    """

    annotation: tuple[AnnotationType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Annotation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common",
            "min_occurs": 1,
        },
    )
