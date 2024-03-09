from dataclasses import dataclass, field
from typing import List, Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Bio,
    FnGroup,
    Glossary,
    Label,
    RefList,
    Sec,
    Title,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.ack import Ack
from crossref.models.gov.nih.nlm.ncbi.jats1.app_group import AppGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.notes import Notes

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Back:
    """
    <div> <h3>Back Matter</h3> </div>
    """

    class Meta:
        name = "back"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ack: List[Ack] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    app_group: List[AppGroup] = field(
        default_factory=list,
        metadata={
            "name": "app-group",
            "type": "Element",
        },
    )
    bio: List[Bio] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: List[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    notes: List[Notes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sec: List[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
