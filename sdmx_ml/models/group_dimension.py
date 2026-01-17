from dataclasses import dataclass

from sdmx_ml.models.group_dimension_type import GroupDimensionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GroupDimension(GroupDimensionType):
    """
    GroupDimension is a component which contains only a reference to a
    dimension in the key descriptor (DimensionList).

    Although it is conventional to declare dimensions in the same order as
    they are declared in the ordered key, there is no requirement to do so
    - the ordering of the values of the key are taken from the order in
    which the dimensions are declared. Note that the id of a dimension may
    be inherited from its underlying concept - therefore this reference
    value may actually be the id of the concept.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
