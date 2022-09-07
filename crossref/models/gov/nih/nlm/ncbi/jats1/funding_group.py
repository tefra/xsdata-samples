from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import OpenAccess
from crossref.models.gov.nih.nlm.ncbi.jats1.award_group import AwardGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.funding_statement import FundingStatement
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class FundingGroup:
    """<div>

    <h3>Funding Group</h3> </div>
    """
    class Meta:
        name = "funding-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    award_group: List[AwardGroup] = field(
        default_factory=list,
        metadata={
            "name": "award-group",
            "type": "Element",
        }
    )
    funding_statement: List[FundingStatement] = field(
        default_factory=list,
        metadata={
            "name": "funding-statement",
            "type": "Element",
        }
    )
    open_access: List[OpenAccess] = field(
        default_factory=list,
        metadata={
            "name": "open-access",
            "type": "Element",
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
