from dataclasses import dataclass, field
from typing import Optional, Union

from crossref.models.gov.nih.nlm.ncbi.jats1.issue import Issue
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_id import IssueId
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_part import IssuePart
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_sponsor import IssueSponsor
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title import IssueTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title_group import (
    IssueTitleGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.volume import Volume
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_id import VolumeId
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_series import VolumeSeries
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class VolumeIssueGroup:
    """
    <div> <h3>Translated Title Group</h3> </div>.
    """

    class Meta:
        name = "volume-issue-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    volume: list[Volume] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    volume_id: list[VolumeId] = field(
        default_factory=list,
        metadata={
            "name": "volume-id",
            "type": "Element",
        },
    )
    volume_series: Optional[VolumeSeries] = field(
        default=None,
        metadata={
            "name": "volume-series",
            "type": "Element",
        },
    )
    issue: list[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    issue_id: list[IssueId] = field(
        default_factory=list,
        metadata={
            "name": "issue-id",
            "type": "Element",
        },
    )
    issue_title: list[IssueTitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-title",
            "type": "Element",
        },
    )
    issue_title_group: list[IssueTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "issue-title-group",
            "type": "Element",
        },
    )
    issue_sponsor: list[IssueSponsor] = field(
        default_factory=list,
        metadata={
            "name": "issue-sponsor",
            "type": "Element",
        },
    )
    issue_part: Optional[IssuePart] = field(
        default=None,
        metadata={
            "name": "issue-part",
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
