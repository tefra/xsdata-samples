from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.original_language_title_language import (
    OriginalLanguageTitleLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.xref_faces import (
    B,
    Em,
    Font,
    I,
    Ovl,
    Scp,
    Strong,
    Sub,
    Sup,
    Tt,
    U,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math import Math

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class OriginalLanguageTitle:
    """
    The title of an item in its original language if the registration is for a
    translation of a work.
    """

    class Meta:
        name = "original_language_title"
        namespace = "http://www.crossref.org/schema/5.3.1"

    language: Optional[OriginalLanguageTitleLanguage] = field(
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
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "u",
                    "type": U,
                },
                {
                    "name": "ovl",
                    "type": Ovl,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "scp",
                    "type": Scp,
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
            ),
        },
    )
