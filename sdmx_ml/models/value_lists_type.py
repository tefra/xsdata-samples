from dataclasses import dataclass, field

from sdmx_ml.models.value_list_type import ValueListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ValueListsType:
    """ValueListsType describes the structure of the value lists container.

    It contains one or more value list, which can be explicitly detailed
    or referenced from an external structure document or registry
    service.

    :ivar value_list: ValueList provides the details of a value list,
        which is a closed set of values that can occur for a dimension,
        measure, or attribute. This may be a simple list of values, or a
        list of values with names and descriptions (similar to a
        codelist).
    """

    value_list: tuple[ValueListType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValueList",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
