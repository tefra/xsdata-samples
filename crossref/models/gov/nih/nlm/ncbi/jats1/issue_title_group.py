from dataclasses import dataclass, field

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
    <div> <h3>Issue Title Group</h3> </div>.
    """

    class Meta:
        name = "issue-title-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    issue_title: IssueTitle | None = field(
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
    content_type: str | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: str | None = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
