from dataclasses import dataclass, field

from crossref.models.org.crossref.relations.description_language import (
    DescriptionLanguage,
)
from crossref.models.org.crossref.relations.xref_faces import (
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

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


@dataclass
class Description:
    """
    A narrative description of the relationship target item.
    """

    class Meta:
        name = "description"
        namespace = "http://www.crossref.org/relations.xsd"

    language: DescriptionLanguage | None = field(
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
            ),
        },
    )
