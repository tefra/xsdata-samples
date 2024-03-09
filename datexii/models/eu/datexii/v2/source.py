from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.country_enum import CountryEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.source_type_enum import SourceTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Source:
    """
    Details of the source from which the information was obtained.

    :ivar source_country: ISO 3166-1 two character country code of the
        source of the information.
    :ivar source_identification: Identifier of the organisation or the
        traffic equipment which has produced the information relating to
        this version of the information.
    :ivar source_name: The name of the organisation which has produced
        the information relating to this version of the information.
    :ivar source_type: Information about the technology used for
        measuring the data or the method used for obtaining qualitative
        descriptions relating to this version of the information.
    :ivar reliable: An indication as to whether the source deems the
        associated information to be reliable/correct. "True" indicates
        it is deemed reliable.
    :ivar source_extension:
    """

    source_country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "name": "sourceCountry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    source_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    source_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    source_type: Optional[SourceTypeEnum] = field(
        default=None,
        metadata={
            "name": "sourceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    reliable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    source_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "sourceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
