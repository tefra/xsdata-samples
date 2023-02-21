from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_designator_t import StdDesignatorT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdUndatedDesignator(StdDesignatorT):
    """
    Provides for defining a DOI for a group of closely related standard documents
    (undated form is a stem for any dated form)
    """
    class Meta:
        name = "std_undated_designator"
        namespace = "http://www.crossref.org/schema/5.3.1"

    family: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
