from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.relations.program import Program
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import ArchiveLocations
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import Contributors
from crossref.models.org.crossref.schema.pkg_5.pkg_3.database_date import DatabaseDate
from crossref.models.org.crossref.schema.pkg_5.pkg_3.description import Description
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import Institution
from crossref.models.org.crossref.schema.pkg_5.pkg_3.language_atts_language import LanguageAttsLanguage
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import PublisherItem
from crossref.models.org.crossref.schema.pkg_5.pkg_3.reference_distribution_opts_att_reference_distribution_opts import ReferenceDistributionOptsAttReferenceDistributionOpts
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DatabaseMetadata:
    """
    database_metadata contains metadata about the database.
    """
    class Meta:
        name = "database_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: Optional[Contributors] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    titles: Optional[Titles] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    database_date: List[DatabaseDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        }
    )
    publisher: Optional[Publisher] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        }
    )
    publisher_item: Optional[PublisherItem] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    archive_locations: Optional[ArchiveLocations] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    doi_data: Optional[DoiData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        }
    )
    language: Optional[LanguageAttsLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference_distribution_opts: ReferenceDistributionOptsAttReferenceDistributionOpts = field(
        default=ReferenceDistributionOptsAttReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        }
    )
