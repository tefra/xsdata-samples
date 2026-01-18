from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class AnnotationUrltype:
    """
    AnnotationURLType defines an external resource.

    These can indicate localisation by specifying a language for the
    resource.

    :ivar value:
    :ivar lang: Indicates the language of the resources at the URL, if
        it is localised. If this does not exist, the resource is not
        localised.
    """

    class Meta:
        name = "AnnotationURLType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
