from dataclasses import dataclass, field
from typing import List

from crossref.models.org.crossref.access_indicators.program import (
    Program as AccessIndicatorsProgram,
)
from crossref.models.org.crossref.clinicaltrials.program import (
    Program as ClinicaltrialsProgram,
)
from crossref.models.org.crossref.fundref.program import (
    Program as FundrefProgram,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.assertion import Assertion

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CustomMetadata:
    """Publishers are encouraged to provided any non-bibliographical metadata that
    they feel might help the researcher evaluate and make better use of the content
    that the Crossmark record refers to.

    For example, publishers might want to provide funding information,
    clinical trial numbers, information about the peer-review process or
    a summary of the publication history of the document.
    """

    class Meta:
        name = "custom_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    assertion: List[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    program: List[FundrefProgram] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/fundref.xsd",
            "max_occurs": 2,
        },
    )
    program_1: List[AccessIndicatorsProgram] = field(
        default_factory=list,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
            "max_occurs": 3,
        },
    )
    program_2: List[ClinicaltrialsProgram] = field(
        default_factory=list,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/clinicaltrials.xsd",
            "max_occurs": 4,
        },
    )
