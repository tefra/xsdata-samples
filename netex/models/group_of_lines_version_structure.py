from dataclasses import dataclass, field
from typing import List, Optional
from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .group_of_lines_type_enumeration import GroupOfLinesTypeEnumeration
from .line_ref_structure import LineRefStructure
from .line_refs_rel_structure import LineRefsRelStructure
from .payment_method_enumeration import PaymentMethodEnumeration
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .transport_submode import TransportSubmode
from .type_of_payment_method_value_structure import (
    TypeOfPaymentMethodValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLinesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfLines_VersionStructure"

    use_to_exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "MainLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_lines_type: Optional[GroupOfLinesTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: Optional[
        TypeOfPaymentMethodValueStructure
    ] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purchase_moment: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
