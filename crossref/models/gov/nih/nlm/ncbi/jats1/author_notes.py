from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Fn,
    Label,
    P,
    Title,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.corresp import Corresp

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class AuthorNotes:
    """<div>

    <h3>Author Note Group</h3> </div>
    """
    class Meta:
        name = "author-notes"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    corresp: List[Corresp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5391,
        }
    )
    fn: List[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5391,
        }
    )
    p: List[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5391,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )