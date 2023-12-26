from dataclasses import dataclass
from crossref.models.org.crossref.schema.pkg_5.pkg_3.date_t import DateT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class AcceptanceDate(DateT):
    """
    The date a manuscript was accepted for publication.
    """

    class Meta:
        name = "acceptance_date"
        namespace = "http://www.crossref.org/schema/5.3.1"
