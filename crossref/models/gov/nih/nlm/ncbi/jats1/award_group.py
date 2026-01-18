from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    AwardId,
    FundingSource,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.award_desc import AwardDesc
from crossref.models.gov.nih.nlm.ncbi.jats1.award_name import AwardName
from crossref.models.gov.nih.nlm.ncbi.jats1.principal_award_recipient import (
    PrincipalAwardRecipient,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.principal_investigator import (
    PrincipalInvestigator,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.support_source import SupportSource
from crossref.models.xlink.actuate_type import ActuateType
from crossref.models.xlink.show_type import ShowType
from crossref.models.xlink.type_type import TypeType
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class AwardGroup:
    """
    <div> <h3>Award Group</h3> </div>.
    """

    class Meta:
        name = "award-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    funding_source: list[FundingSource] = field(
        default_factory=list,
        metadata={
            "name": "funding-source",
            "type": "Element",
        },
    )
    support_source: list[SupportSource] = field(
        default_factory=list,
        metadata={
            "name": "support-source",
            "type": "Element",
        },
    )
    award_id: list[AwardId] = field(
        default_factory=list,
        metadata={
            "name": "award-id",
            "type": "Element",
        },
    )
    award_name: None | AwardName = field(
        default=None,
        metadata={
            "name": "award-name",
            "type": "Element",
        },
    )
    award_desc: None | AwardDesc = field(
        default=None,
        metadata={
            "name": "award-desc",
            "type": "Element",
        },
    )
    principal_award_recipient: list[PrincipalAwardRecipient] = field(
        default_factory=list,
        metadata={
            "name": "principal-award-recipient",
            "type": "Element",
        },
    )
    principal_investigator: list[PrincipalInvestigator] = field(
        default_factory=list,
        metadata={
            "name": "principal-investigator",
            "type": "Element",
        },
    )
    award_type: None | str = field(
        default=None,
        metadata={
            "name": "award-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
