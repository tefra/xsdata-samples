from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.access_indicators.program import (
    Program as AccessIndicatorsProgram,
)
from crossref.models.org.crossref.relations.program import (
    Program as RelationsProgram,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.competing_interest_statement import (
    CompetingInterestStatement,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import (
    Institution,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.peer_review_language import (
    PeerReviewLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.peer_review_recommendation import (
    PeerReviewRecommendation,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.peer_review_stage import (
    PeerReviewStage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.peer_review_type import (
    PeerReviewType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.review_date import (
    ReviewDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.running_number import (
    RunningNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.scn_policies import (
    ScnPolicies,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PeerReview:
    """
    The peer_review content type is intended for assigning DOIs to the reports and
    other artifacts associated with the review of published content.

    :ivar contributors:
    :ivar titles:
    :ivar review_date:
    :ivar institution:
    :ivar competing_interest_statement:
    :ivar running_number:
    :ivar program:
    :ivar crossref_org_relations_program:
    :ivar scn_policies:
    :ivar doi_data:
    :ivar stage:
    :ivar type_value:
    :ivar recommendation:
    :ivar revision_round: Required attribute. First submission defined
        as revision round zero
    :ivar language:
    """

    class Meta:
        name = "peer_review"
        namespace = "http://www.crossref.org/schema/5.3.1"

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
    review_date: Optional[ReviewDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    competing_interest_statement: Optional[CompetingInterestStatement] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    running_number: Optional[RunningNumber] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: Optional[AccessIndicatorsProgram] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        },
    )
    crossref_org_relations_program: Optional[RelationsProgram] = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
            "required": True,
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
    stage: Optional[PeerReviewStage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[PeerReviewType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    recommendation: Optional[PeerReviewRecommendation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    revision_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "revision-round",
            "type": "Attribute",
        },
    )
    language: Optional[PeerReviewLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
