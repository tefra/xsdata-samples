from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import Abstract
from crossref.models.org.crossref.access_indicators.program import (
    Program as AccessIndicatorsProgram,
)
from crossref.models.org.crossref.fundref.program import (
    Program as FundrefProgram,
)
from crossref.models.org.crossref.relations.program import (
    Program as RelationsProgram,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.acceptance_date import (
    AcceptanceDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.citation_list import (
    CitationList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.group_title import (
    GroupTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import (
    Institution,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.item_number import (
    ItemNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.posted_content_language import (
    PostedContentLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.posted_content_type import (
    PostedContentType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.posted_date import (
    PostedDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.scn_policies import (
    ScnPolicies,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PostedContent:
    """
    Container for posted content metadata.
    """

    class Meta:
        name = "posted_content"
        namespace = "http://www.crossref.org/schema/5.3.1"

    group_title: Optional[GroupTitle] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    contributors: Optional[Contributors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    titles: Optional[Titles] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    posted_date: Optional[PostedDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    acceptance_date: Optional[AcceptanceDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    item_number: List[ItemNumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        },
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        },
    )
    program: Optional[FundrefProgram] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/fundref.xsd",
        },
    )
    program_1: Optional[AccessIndicatorsProgram] = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        },
    )
    program_2: Optional[RelationsProgram] = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        },
    )
    scn_policies: Optional[ScnPolicies] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi_data: Optional[DoiData] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    citation_list: Optional[CitationList] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    type_value: PostedContentType = field(
        default=PostedContentType.PREPRINT,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    language: Optional[PostedContentLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
