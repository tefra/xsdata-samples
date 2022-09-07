from dataclasses import dataclass
from crossref.models.org.crossref.schema.pkg_5.pkg_3.date_t import DateT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CreationDate(DateT):
    """
    The date a database or dataset item was created.
    """
    class Meta:
        name = "creation_date"
        namespace = "http://www.crossref.org/schema/5.3.1"
