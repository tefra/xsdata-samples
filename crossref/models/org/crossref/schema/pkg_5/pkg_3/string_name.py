from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.degrees import Degrees
from crossref.models.org.crossref.schema.pkg_5.pkg_3.language_atts_language import LanguageAttsLanguage
from crossref.models.org.crossref.schema.pkg_5.pkg_3.prefix import Prefix
from crossref.models.org.crossref.schema.pkg_5.pkg_3.string_name_name_style import StringNameNameStyle

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StringName:
    class Meta:
        name = "string-name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    name_style: StringNameNameStyle = field(
        default=StringNameNameStyle.WESTERN,
        metadata={
            "name": "name-style",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    language: Optional[LanguageAttsLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
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
                    "type": str,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "collapse",
                    "pattern": r"[^\d\?]*[^\?\s]+[^\d]*",
                },
                {
                    "name": "prefix",
                    "type": Prefix,
                },
                {
                    "name": "surname",
                    "type": str,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "collapse",
                    "pattern": r"[^\d\?]*[^\?\s]+[^\d]*",
                },
                {
                    "name": "suffix",
                    "type": str,
                    "min_length": 1,
                    "max_length": 10,
                },
            ),
        }
    )
