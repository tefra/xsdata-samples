from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.clinicaltrials.clinical_trial_number import (
    ClinicalTrialNumber,
)

__NAMESPACE__ = "http://www.crossref.org/clinicaltrials.xsd"


@dataclass
class Program:
    """Accommodates deposit of linked clincal trials metadata.

    The clinical-trial-number value will be a string that must match a
    specific pattern appropriate for a given clinical trial registry.
    The registry is identified in the required attribute 'registry' and
    must be the DOI of a recognized registry (see
    http://dx.doi.org/10.18810/registries)
    """

    class Meta:
        name = "program"
        namespace = "http://www.crossref.org/clinicaltrials.xsd"

    clinical_trial_number: List[ClinicalTrialNumber] = field(
        default_factory=list,
        metadata={
            "name": "clinical-trial-number",
            "type": "Element",
        },
    )
