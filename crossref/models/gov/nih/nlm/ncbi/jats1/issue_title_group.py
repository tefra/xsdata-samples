from dataclasses import dataclass, field
from typing import Optional, Union

from crossref.models.gov.nih.nlm.ncbi.jats1.issue_subtitle import IssueSubtitle
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title import IssueTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_title_group import (
    TransTitleGroup,
)
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class IssueTitleGroup:
    """
    <div> <h3>Issue Title Group</h3> </div>
    """

    class Meta:
        name = "issue-title-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    issue_title: Optional[IssueTitle] = field(
        default=None,
        metadata={
            "name": "issue-title",
            "type": "Element",
            "required": True,
        },
    )
    issue_subtitle: list[IssueSubtitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-subtitle",
            "type": "Element",
        },
    )
    trans_title_group: list[TransTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "trans-title-group",
            "type": "Element",
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
