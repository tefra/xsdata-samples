from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.annotation_type import AnnotationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class AnnotationsType:
    """
    AnnotationsType provides for a list of annotations to be attached to data and
    structure messages.
    """

    annotation: Tuple[AnnotationType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Annotation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
            "min_occurs": 1,
        },
    )
