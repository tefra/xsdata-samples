from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.axle_spacing import AxleSpacing
from datexii.models.eu.datexii.v2.axle_weight import AxleWeight
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.hazardous_materials import HazardousMaterials
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)
from datexii.models.eu.datexii.v2.vehicle_status_enum import VehicleStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Vehicle:
    """
    Details of an individual vehicle.

    :ivar vehicle_colour: The colour of the vehicle.
    :ivar vehicle_country_of_origin: Specification of the country in
        which the vehicle is registered.  The code is the 2-alpha code
        as given in EN ISO 3166-1 which is updated by the ISO 3166
        Maintenance Agency.
    :ivar vehicle_identifier: A vehicle identification number (VIN)
        comprising 17 characters that is based on either ISO 3779 or ISO
        3780  and uniquely identifies the individual vehicle. This is
        normally securely attached to the vehicle chassis.
    :ivar vehicle_manufacturer: Indicates the stated manufacturer of the
        vehicle i.e. Ford.
    :ivar vehicle_model: Indicates the model (or range name) of the
        vehicle i.e. Mondeo.
    :ivar vehicle_registration_plate_identifier: An identifier or code
        displayed on a vehicle registration plate attached to the
        vehicle used for official identification purposes. The
        registration identifier is numeric or alphanumeric and is unique
        within the issuing authority's region.
    :ivar vehicle_status: Vehicle status.
    :ivar vehicle_characteristics:
    :ivar axle_spacing_on_vehicle: The spacing between axles on the
        vehicles.
    :ivar specific_axle_weight: The weight details relating to a
        specific axle on the vehicle.
    :ivar hazardous_goods_associated_with_vehicle: Details of hazardous
        goods carried by the vehicle.
    :ivar vehicle_extension:
    """

    vehicle_colour: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_country_of_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleCountryOfOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    vehicle_manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleManufacturer",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    vehicle_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    vehicle_registration_plate_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleRegistrationPlateIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    vehicle_status: Optional[VehicleStatusEnum] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    axle_spacing_on_vehicle: List[AxleSpacing] = field(
        default_factory=list,
        metadata={
            "name": "axleSpacingOnVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    specific_axle_weight: List[AxleWeight] = field(
        default_factory=list,
        metadata={
            "name": "specificAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    hazardous_goods_associated_with_vehicle: Optional[HazardousMaterials] = (
        field(
            default=None,
            metadata={
                "name": "hazardousGoodsAssociatedWithVehicle",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    vehicle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
