from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.link import Link

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class IdentifiableType(AnnotableType):
    """
    IdentifiableType is an abstract base type for all identifiable objects.

    :ivar link:
    :ivar id: The id is the identifier for the object.
    :ivar urn: The urn attribute holds a valid SDMX Registry URN (see
        SDMX Registry Specification for details).
    :ivar uri: The uri attribute holds a URI that contains a link to a
        resource with additional information about the object, such as a
        web page. This uri is not a SDMX message.
    """

    link: tuple[Link, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    urn: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?",
        },
    )
    uri: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
