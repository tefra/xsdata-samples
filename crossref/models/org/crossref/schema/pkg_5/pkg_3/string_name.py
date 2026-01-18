from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.degrees import Degrees
from crossref.models.org.crossref.schema.pkg_5.pkg_3.given_name import (
    GivenName,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.prefix import Prefix
from crossref.models.org.crossref.schema.pkg_5.pkg_3.string_name_language import (
    StringNameLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.string_name_name_style import (
    StringNameNameStyle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.suffix import Suffix
from crossref.models.org.crossref.schema.pkg_5.pkg_3.surname import Surname

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StringName:
    class Meta:
        name = "string-name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    content_type: object | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    name_style: StringNameNameStyle = field(
        default=StringNameNameStyle.WESTERN,
        metadata={
            "name": "name-style",
            "type": "Attribute",
        },
    )
    specific_use: object | None = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    language: StringNameLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "degrees",
                    "type": Degrees,
                },
                {
                    "name": "given_name",
                    "type": GivenName,
                },
                {
                    "name": "prefix",
                    "type": Prefix,
                },
                {
                    "name": "surname",
                    "type": Surname,
                },
                {
                    "name": "suffix",
                    "type": Suffix,
                },
            ),
        },
    )
