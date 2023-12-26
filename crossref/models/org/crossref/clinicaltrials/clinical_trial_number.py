from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.clinicaltrials.clinical_trial_number_type import (
    ClinicalTrialNumberType,
)

__NAMESPACE__ = "http://www.crossref.org/clinicaltrials.xsd"


@dataclass
class ClinicalTrialNumber:
    """
    :ivar registry: The clinical trial identifier related to the
        article.
    :ivar type_value: Used to identify the article publication date in
        relation to the issuance of the trial results
    :ivar content:
    """

    class Meta:
        name = "clinical-trial-number"
        namespace = "http://www.crossref.org/clinicaltrials.xsd"

    registry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 12,
            "max_length": 200,
            "pattern": r"10.18810/[a-z-]+",
        },
    )
    type_value: Optional[ClinicalTrialNumberType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
