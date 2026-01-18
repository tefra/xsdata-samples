from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_id import ContribId
from crossref.models.gov.nih.nlm.ncbi.jats1.name import Name
from crossref.models.gov.nih.nlm.ncbi.jats1.name_alternatives import (
    NameAlternatives,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name import StringName
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class PrincipalInvestigator:
    """
    <div> <h3>Principal Investigator Recipient</h3> </div>.
    """

    class Meta:
        name = "principal-investigator"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
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
                    "name": "contrib-id",
                    "type": ContribId,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "name-alternatives",
                    "type": NameAlternatives,
                },
                {
                    "name": "string-name",
                    "type": StringName,
                },
            ),
        },
    )
