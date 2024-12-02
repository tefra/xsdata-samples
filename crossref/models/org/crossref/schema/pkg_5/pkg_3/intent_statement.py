from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.a import A
from crossref.models.org.crossref.schema.pkg_5.pkg_3.intent_statement_language import (
    IntentStatementLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.xref_faces import (
    B,
    I,
    U,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class IntentStatement:
    """
    Member's custom statement of intent to publish content for which a pending
    publication DOI has been created.
    """

    class Meta:
        name = "intent_statement"
        namespace = "http://www.crossref.org/schema/5.3.1"

    language: Optional[IntentStatementLanguage] = field(
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
                    "name": "u",
                    "type": U,
                },
                {
                    "name": "a",
                    "type": A,
                },
            ),
        },
    )
