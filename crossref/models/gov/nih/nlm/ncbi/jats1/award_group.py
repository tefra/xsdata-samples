from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import (
    AwardId,
    FundingSource,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.award_desc import AwardDesc
from crossref.models.gov.nih.nlm.ncbi.jats1.award_name import AwardName
from crossref.models.gov.nih.nlm.ncbi.jats1.principal_award_recipient import PrincipalAwardRecipient
from crossref.models.gov.nih.nlm.ncbi.jats1.principal_investigator import PrincipalInvestigator
from crossref.models.gov.nih.nlm.ncbi.jats1.support_source import SupportSource
from crossref.models.xlink.actuate_type import ActuateType
from crossref.models.xlink.show_type import ShowType
from crossref.models.xlink.type_type import TypeType
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class AwardGroup:
    """
    <div> <h3>Award Group</h3> </div>
    """
    class Meta:
        name = "award-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    funding_source: List[FundingSource] = field(
        default_factory=list,
        metadata={
            "name": "funding-source",
            "type": "Element",
        }
    )
    support_source: List[SupportSource] = field(
        default_factory=list,
        metadata={
            "name": "support-source",
            "type": "Element",
        }
    )
    award_id: List[AwardId] = field(
        default_factory=list,
        metadata={
            "name": "award-id",
            "type": "Element",
        }
    )
    award_name: Optional[AwardName] = field(
        default=None,
        metadata={
            "name": "award-name",
            "type": "Element",
        }
    )
    award_desc: Optional[AwardDesc] = field(
        default=None,
        metadata={
            "name": "award-desc",
            "type": "Element",
        }
    )
    principal_award_recipient: List[PrincipalAwardRecipient] = field(
        default_factory=list,
        metadata={
            "name": "principal-award-recipient",
            "type": "Element",
        }
    )
    principal_investigator: List[PrincipalInvestigator] = field(
        default_factory=list,
        metadata={
            "name": "principal-investigator",
            "type": "Element",
        }
    )
    award_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "award-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
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
