from dataclasses import dataclass, field
from typing import List, Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Abstract,
    Aff,
    AffAlternatives,
    ContribGroup,
    ExtLink,
    KwdGroup,
    Permissions,
    Product,
    RelatedArticle,
    RelatedObject,
    Supplement,
    SupplementaryMaterial,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_categories import (
    ArticleCategories,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_id import ArticleId
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version import (
    ArticleVersion,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version_alternatives import (
    ArticleVersionAlternatives,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.author_notes import AuthorNotes
from crossref.models.gov.nih.nlm.ncbi.jats1.conference import Conference
from crossref.models.gov.nih.nlm.ncbi.jats1.counts import Counts
from crossref.models.gov.nih.nlm.ncbi.jats1.custom_meta_group import (
    CustomMetaGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.elocation_id import ElocationId
from crossref.models.gov.nih.nlm.ncbi.jats1.email import Email
from crossref.models.gov.nih.nlm.ncbi.jats1.fpage import Fpage
from crossref.models.gov.nih.nlm.ncbi.jats1.funding_group import FundingGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.history import History
from crossref.models.gov.nih.nlm.ncbi.jats1.isbn import Isbn
from crossref.models.gov.nih.nlm.ncbi.jats1.issue import Issue
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_id import IssueId
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_part import IssuePart
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_sponsor import IssueSponsor
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title import IssueTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title_group import (
    IssueTitleGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.lpage import Lpage
from crossref.models.gov.nih.nlm.ncbi.jats1.page_range import PageRange
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date import PubDate
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date_not_available import (
    PubDateNotAvailable,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_history import PubHistory
from crossref.models.gov.nih.nlm.ncbi.jats1.self_uri import SelfUri
from crossref.models.gov.nih.nlm.ncbi.jats1.support_group import SupportGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.title_group import TitleGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_abstract import TransAbstract
from crossref.models.gov.nih.nlm.ncbi.jats1.uri import Uri
from crossref.models.gov.nih.nlm.ncbi.jats1.volume import Volume
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_id import VolumeId
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_issue_group import (
    VolumeIssueGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_series import VolumeSeries

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class FrontStub:
    """
    <div> <h3>Stub Front Metadata</h3> </div>
    """

    class Meta:
        name = "front-stub"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    article_id: List[ArticleId] = field(
        default_factory=list,
        metadata={
            "name": "article-id",
            "type": "Element",
        },
    )
    article_version: Optional[ArticleVersion] = field(
        default=None,
        metadata={
            "name": "article-version",
            "type": "Element",
        },
    )
    article_version_alternatives: Optional[ArticleVersionAlternatives] = field(
        default=None,
        metadata={
            "name": "article-version-alternatives",
            "type": "Element",
        },
    )
    article_categories: Optional[ArticleCategories] = field(
        default=None,
        metadata={
            "name": "article-categories",
            "type": "Element",
        },
    )
    title_group: Optional[TitleGroup] = field(
        default=None,
        metadata={
            "name": "title-group",
            "type": "Element",
        },
    )
    contrib_group: List[ContribGroup] = field(
        default_factory=list,
        metadata={
            "name": "contrib-group",
            "type": "Element",
        },
    )
    aff: List[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    aff_alternatives: List[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
        },
    )
    author_notes: Optional[AuthorNotes] = field(
        default=None,
        metadata={
            "name": "author-notes",
            "type": "Element",
        },
    )
    pub_date: List[PubDate] = field(
        default_factory=list,
        metadata={
            "name": "pub-date",
            "type": "Element",
        },
    )
    pub_date_not_available: Optional[PubDateNotAvailable] = field(
        default=None,
        metadata={
            "name": "pub-date-not-available",
            "type": "Element",
        },
    )
    volume: List[Volume] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    volume_id: List[VolumeId] = field(
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
    issue: List[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    issue_id: List[IssueId] = field(
        default_factory=list,
        metadata={
            "name": "issue-id",
            "type": "Element",
        },
    )
    issue_title: List[IssueTitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-title",
            "type": "Element",
        },
    )
    issue_title_group: List[IssueTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "issue-title-group",
            "type": "Element",
        },
    )
    issue_sponsor: List[IssueSponsor] = field(
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
    volume_issue_group: List[VolumeIssueGroup] = field(
        default_factory=list,
        metadata={
            "name": "volume-issue-group",
            "type": "Element",
        },
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    supplement: Optional[Supplement] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fpage: Optional[Fpage] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lpage: Optional[Lpage] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    page_range: Optional[PageRange] = field(
        default=None,
        metadata={
            "name": "page-range",
            "type": "Element",
        },
    )
    elocation_id: Optional[ElocationId] = field(
        default=None,
        metadata={
            "name": "elocation-id",
            "type": "Element",
        },
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: List[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pub_history: Optional[PubHistory] = field(
        default=None,
        metadata={
            "name": "pub-history",
            "type": "Element",
        },
    )
    permissions: Optional[Permissions] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    self_uri: List[SelfUri] = field(
        default_factory=list,
        metadata={
            "name": "self-uri",
            "type": "Element",
        },
    )
    related_article: List[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: List[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    trans_abstract: List[TransAbstract] = field(
        default_factory=list,
        metadata={
            "name": "trans-abstract",
            "type": "Element",
        },
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    funding_group: List[FundingGroup] = field(
        default_factory=list,
        metadata={
            "name": "funding-group",
            "type": "Element",
        },
    )
    support_group: List[SupportGroup] = field(
        default_factory=list,
        metadata={
            "name": "support-group",
            "type": "Element",
        },
    )
    conference: List[Conference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    counts: Optional[Counts] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    custom_meta_group: Optional[CustomMetaGroup] = field(
        default=None,
        metadata={
            "name": "custom-meta-group",
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
