from dataclasses import dataclass
from crossref.models.org.crossref.schema.pkg_5.pkg_3.date_t import DateT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PublicationDate(DateT):
    """The date of publication.

    Multiple dates are allowed to allow for different dates of
    publication for online and print versions.
    """

    class Meta:
        name = "publication_date"
        namespace = "http://www.crossref.org/schema/5.3.1"
