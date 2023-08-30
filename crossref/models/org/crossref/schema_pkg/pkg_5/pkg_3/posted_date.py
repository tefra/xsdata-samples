from dataclasses import dataclass
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.date_t import DateT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PostedDate(DateT):
    """
    The date a pre-print was posted to a repository.
    """
    class Meta:
        name = "posted_date"
        namespace = "http://www.crossref.org/schema/5.3.1"
