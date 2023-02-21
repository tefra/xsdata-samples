from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import ArchiveLocations
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.noisbn import Noisbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import PublicationDate
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import PublisherItem
from crossref.models.org.crossref.schema.pkg_5.pkg_3.reference_distribution_opts_att_reference_distribution_opts import ReferenceDistributionOptsAttReferenceDistributionOpts
from crossref.models.org.crossref.schema.pkg_5.pkg_3.series_metadata import SeriesMetadata

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ProceedingsSeriesMetadata:
    """
    Container for all information that applies to a specific conference proceeding
    that is part of a series.
    """
    class Meta:
        name = "proceedings_series_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    series_metadata: Optional[SeriesMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    proceedings_title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 511,
        }
    )
    volume: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 32,
            "sequence": 239,
        }
    )
    proceedings_subject: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 255,
            "sequence": 251,
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        }
    )
    publication_date: List[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 20,
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )
    noisbn: Optional[Noisbn] = field(
        default=None,
        metadata={
            "type": "Element",
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
    reference_distribution_opts: ReferenceDistributionOptsAttReferenceDistributionOpts = field(
        default=ReferenceDistributionOptsAttReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        }
    )
