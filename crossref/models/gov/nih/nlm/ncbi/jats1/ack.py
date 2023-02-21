from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Abstract,
    KwdGroup,
    Label,
    P,
    RefList,
    Sec,
    SubjGroup,
    Title,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.object_id import ObjectId
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Ack:
    """<div>

    <h3>Acknowledgments</h3> </div>
    """
    class Meta:
        name = "ack"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
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
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 4906,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequence": 4906,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequence": 4906,
        }
    )
    p: List[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 4906,
        }
    )
    sec: List[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 4906,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequence": 4906,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
