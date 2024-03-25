from dataclasses import dataclass

from sdmx_ml.models.metadata_attribute_usage_type import (
    MetadataAttributeUsageType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeUsage(MetadataAttributeUsageType):
    """MetadataAttributeUsage refines the details of how a metadata attribute from
    the metadata structure referenced from the data structure is used.

    By default, metadata attributes can be expressed at any level of the
    data. This allows an attribute relationship to be defined in order
    restrict the reporing of a metadata attribute to a specific part of
    the data.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
