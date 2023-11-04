from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdDesignatorT:
    class Meta:
        name = "std_designator_t"

    std_designator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "required": True,
            "min_length": 2,
            "max_length": 150,
        }
    )
    std_alt_script: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 2,
            "max_length": 150,
        }
    )
    std_variant_form: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 2,
            "max_length": 150,
        }
    )
