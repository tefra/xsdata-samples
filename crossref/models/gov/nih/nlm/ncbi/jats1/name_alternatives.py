from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.name import Name
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name import StringName

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class NameAlternatives:
    """
    <div> <h3>Name Alternatives</h3> </div>.
    """

    class Meta:
        name = "name-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    name: list[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    string_name: list[StringName] = field(
        default_factory=list,
        metadata={
            "name": "string-name",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
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
