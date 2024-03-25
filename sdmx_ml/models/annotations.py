from dataclasses import dataclass

from sdmx_ml.models.annotations_type import AnnotationsType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class Annotations(AnnotationsType):
    """Annotations is a reusable element the provides for a collection of
    annotations.

    It has been made global so that restrictions of types that extend
    AnnotatableType may reference it.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"
