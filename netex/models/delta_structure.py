from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.models.delta_values_rel_structure import DeltaValuesRelStructure
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.simple_object_ref import SimpleObjectRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeltaStructure:
    simple_object_ref: Optional[SimpleObjectRef] = field(
        default=None,
        metadata={
            "name": "SimpleObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_version_ref: Optional["DeltaStructure.FromVersionRef"] = field(
        default=None,
        metadata={
            "name": "FromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_version_ref: Optional["DeltaStructure.ToVersionRef"] = field(
        default=None,
        metadata={
            "name": "ToVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    modification: Optional[ModificationEnumeration] = field(
        default=None,
        metadata={
            "name": "Modification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delta_values: Optional[DeltaValuesRelStructure] = field(
        default=None,
        metadata={
            "name": "deltaValues",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class FromVersionRef:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ToVersionRef:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
