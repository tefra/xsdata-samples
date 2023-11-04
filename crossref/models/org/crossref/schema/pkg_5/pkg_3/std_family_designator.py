from dataclasses import dataclass
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_designator_t import StdDesignatorT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdFamilyDesignator(StdDesignatorT):
    """
    Provides for defining a DOI for a broad grouping of standards.
    """
    class Meta:
        name = "std_family_designator"
        namespace = "http://www.crossref.org/schema/5.3.1"
