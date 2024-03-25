from dataclasses import dataclass

from sdmx_ml.models.attribute_list_type import AttributeListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AttributeList(AttributeListType):
    """AttributeList describes the attribute descriptor for the data structure
    definition.

    It is a collection of metadata concepts that define the attributes
    of the data structure definition.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
