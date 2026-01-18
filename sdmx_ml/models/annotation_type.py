from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotation_urltype import AnnotationUrltype
from sdmx_ml.models.text_type import TextType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True, kw_only=True)
class AnnotationType:
    """
    AnnotationType provides for non-documentation notes and annotations to
    be embedded in data and structure messages.

    It provides optional fields for providing a title, a type description,
    a URI, and the text of the annotation.

    :ivar annotation_title: AnnotationTitle provides a title for the
        annotation.
    :ivar annotation_type: AnnotationType is used to distinguish between
        annotations designed to support various uses. The types are not
        enumerated, as these can be specified by the user or creator of
        the annotations. The definitions and use of annotation types
        should be documented by their creator.
    :ivar annotation_url: AnnotationURL is a URI - typically a URL -
        which points to an external resource which may contain or
        supplement the annotation. These can be localised by indicating
        a language for the resource. If a language is not specified, the
        resource is assumed to not be localised. If a specific behavior
        is desired, an annotation type should be defined which specifies
        the use of this field more exactly.
    :ivar annotation_text: AnnotationText holds a language-specific
        string containing the text of the annotation.
    :ivar annotation_value: AnnotationValue holds a non-localised value
        for the annotation.
    :ivar id: The id attribute provides a non-standard identification of
        an annotation. It can be used to disambiguate annotations.
    """

    annotation_title: None | str = field(
        default=None,
        metadata={
            "name": "AnnotationTitle",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    annotation_type: None | str = field(
        default=None,
        metadata={
            "name": "AnnotationType",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    annotation_url: tuple[AnnotationUrltype, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AnnotationURL",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    annotation_text: tuple[TextType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AnnotationText",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    annotation_value: None | str = field(
        default=None,
        metadata={
            "name": "AnnotationValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
