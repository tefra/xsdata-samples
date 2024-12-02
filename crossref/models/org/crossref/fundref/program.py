from dataclasses import dataclass, field

from crossref.models.org.crossref.fundref.assertion import Assertion

__NAMESPACE__ = "http://www.crossref.org/fundref.xsd"


@dataclass
class Program:
    """FundRef documentation and examples: http://help.crossref.org/#fundref
    As part of CrossMark metadata, a deposit may contain what is called FundRef info. This details the funding behind a published article. The schema is a sequence of nested &lt;assertion&gt; tags.
    If a DOI is not participating in CrossMark, FundRef data may be deposited as part of the &lt;journal_article&gt; metadata.
    Note: Some rules will be enforced by the deposit logic (e.g. not the schema).
    FundRef data includes one or more award numbers (award_number), each of which may have one or more funders (funder_name). Each funder may have one or more optional identifiers (funder_identifier).
    A FundRef deposit begins with a &lt;fr:program&gt; tag within the &lt;crossmark&gt; structure (where fr is the namespace for the FundRef program).
    The &lt;program&gt; element is an implicit funder_group and will typically contain:
    A) one or more funder_name assertions and an award_number assertion.
    or
    B) one or more funder_group assertions where each funder_group should contain one or more funder_name assertions and at least one award_number assertion.
    Multiple 'award_number's may be included in a single program or fundgroup. Deposits without an award_number will be accepted, but award_number should be provided whenever possible. Items with several award numbers associated with a single funding organization should be grouped together by enclosing the "funder_name", "funder_identifier", and award_number(s) within a "fundgroup" assertion."""

    class Meta:
        name = "program"
        namespace = "http://www.crossref.org/fundref.xsd"

    assertion: list[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        init=False,
        default="fundref",
        metadata={
            "type": "Attribute",
        },
    )
