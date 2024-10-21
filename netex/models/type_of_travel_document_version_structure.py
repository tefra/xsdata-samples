from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .machine_readable_enumeration import MachineReadableEnumeration
from .media_type_enumeration import MediaTypeEnumeration
from .type_of_entity_version_structure import TypeOfEntityVersionStructure
from .types_of_machine_readabilities_rel_structure import (
    TypesOfMachineReadabilitiesRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTravelDocumentVersionStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfTravelDocument_VersionStructure"

    is_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_smart_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSmartCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_photo: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasPhoto",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    media_type: Optional[MediaTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MediaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    machine_readable: Iterable[MachineReadableEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MachineReadable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_machine_readabilities: Optional[
        TypesOfMachineReadabilitiesRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "typesOfMachineReadabilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
