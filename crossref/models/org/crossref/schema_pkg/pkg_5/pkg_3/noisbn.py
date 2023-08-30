from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.noisbn_reason import NoisbnReason

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Noisbn:
    """
    Identifies books or conference proceedings that have no ISBN assigned.
    """
    class Meta:
        name = "noisbn"
        namespace = "http://www.crossref.org/schema/5.3.1"

    reason: Optional[NoisbnReason] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
