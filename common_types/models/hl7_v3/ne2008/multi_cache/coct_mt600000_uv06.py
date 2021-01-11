from dataclasses import dataclass, field
from typing import List, Optional, Union
from common_types.models.hl7_v3.ne2008.core.datatypes_base import (
    Any,
    Cd,
    Ce,
    Cs,
    EnExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    PnExplicit,
    St,
    TsExplicit,
)
from common_types.models.hl7_v3.ne2008.core.voc import (
    ActClass,
    ActClassObservation,
    ActClassSupply,
    ActMood,
    ActMoodIntent,
    ActRelationshipCostTracking,
    ActRelationshipFulfills,
    ActRelationshipHasSupport,
    ActRelationshipPertainsValue,
    ActRelationshipPosting,
    ActRelationshipTemporallyPertains,
    EntityClass,
    EntityClassMaterial,
    EntityDeterminer,
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetLocation,
    ParticipationType,
    RoleClassManufacturedProduct,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassRootValue,
    XAccommodationRequestorRole,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
)
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt240000_uv01 import CoctMt240000Uv01ServiceDeliveryLocation
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt240003_uv02 import CoctMt240003Uv02ServiceDeliveryLocation

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt600000Uv06Destination:
    class Meta:
        name = "COCT_MT600000UV06.Destination"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    service_delivery_location: Optional[CoctMt240003Uv02ServiceDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.DST,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06Diagnosis:
    class Meta:
        name = "COCT_MT600000UV06.Diagnosis"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    text: Optional[St] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06Location:
    class Meta:
        name = "COCT_MT600000UV06.Location"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    service_delivery_location: Optional[CoctMt240000Uv01ServiceDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ParticipationTargetLocation] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06Origin:
    class Meta:
        name = "COCT_MT600000UV06.Origin"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    service_delivery_location: Optional[CoctMt240003Uv02ServiceDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.ORG,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06ProviderPerson:
    class Meta:
        name = "COCT_MT600000UV06.ProviderPerson"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[PnExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.PSN,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06SupplyObservationEvent:
    class Meta:
        name = "COCT_MT600000UV06.SupplyObservationEvent"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    target_site_code: Optional[Cd] = field(
        default=None,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06VisionPrescriptionObservationEvent:
    class Meta:
        name = "COCT_MT600000UV06.VisionPrescriptionObservationEvent"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    value: Optional[Any] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    target_site_code: Optional[Cd] = field(
        default=None,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06VisionProduct:
    class Meta:
        name = "COCT_MT600000UV06.VisionProduct"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[EnExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[EntityClassMaterial] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06HealthCareProvider:
    class Meta:
        name = "COCT_MT600000UV06.HealthCareProvider"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    health_care_provider_person: Optional[CoctMt600000Uv06ProviderPerson] = field(
        default=None,
        metadata={
            "name": "healthCareProviderPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, RoleClassRootValue, XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassMutualRelationship.PROV,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt600000Uv06PertinentInformation:
    class Meta:
        name = "COCT_MT600000UV06.PertinentInformation"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    diagnosis: Optional[CoctMt600000Uv06Diagnosis] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue]] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt600000Uv06PertinentInformation1:
    class Meta:
        name = "COCT_MT600000UV06.PertinentInformation1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    vision_prescription_observation_event: Optional[CoctMt600000Uv06VisionPrescriptionObservationEvent] = field(
        default=None,
        metadata={
            "name": "visionPrescriptionObservationEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue]] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt600000Uv06Product2:
    class Meta:
        name = "COCT_MT600000UV06.Product2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    supply_observation_event: Optional[CoctMt600000Uv06SupplyObservationEvent] = field(
        default=None,
        metadata={
            "name": "supplyObservationEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.PRD,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06Author:
    class Meta:
        name = "COCT_MT600000UV06.Author"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    health_care_provider: Optional[CoctMt600000Uv06HealthCareProvider] = field(
        default=None,
        metadata={
            "name": "healthCareProvider",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06ManufacturedProduct:
    class Meta:
        name = "COCT_MT600000UV06.ManufacturedProduct"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufactured_vision_product: Optional[CoctMt600000Uv06VisionProduct] = field(
        default=None,
        metadata={
            "name": "manufacturedVisionProduct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    product_of: List[CoctMt600000Uv06Product2] = field(
        default_factory=list,
        metadata={
            "name": "productOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[RoleClassManufacturedProduct] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06Performer:
    class Meta:
        name = "COCT_MT600000UV06.Performer"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    health_care_provider: Optional[CoctMt600000Uv06HealthCareProvider] = field(
        default=None,
        metadata={
            "name": "healthCareProvider",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ParticipationPhysicalPerformer] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06PrescriptionOrder:
    class Meta:
        name = "COCT_MT600000UV06.PrescriptionOrder"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: Optional[CoctMt600000Uv06Author] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.SBADM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.RQO,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06Product:
    class Meta:
        name = "COCT_MT600000UV06.Product"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufactured_product: Optional[CoctMt600000Uv06ManufacturedProduct] = field(
        default=None,
        metadata={
            "name": "manufacturedProduct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.PRD,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06InFulfillmentOf:
    class Meta:
        name = "COCT_MT600000UV06.InFulfillmentOf"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    prescription_order: Optional[CoctMt600000Uv06PrescriptionOrder] = field(
        default=None,
        metadata={
            "name": "prescriptionOrder",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipFulfills] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06PrescriptionIntent:
    class Meta:
        name = "COCT_MT600000UV06.PrescriptionIntent"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of: Optional[CoctMt600000Uv06InFulfillmentOf] = field(
        default=None,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.SBADM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[ActMoodIntent] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt600000Uv06PertinentInformation2:
    class Meta:
        name = "COCT_MT600000UV06.PertinentInformation2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    prescription_intent: Optional[CoctMt600000Uv06PrescriptionIntent] = field(
        default=None,
        metadata={
            "name": "prescriptionIntent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[Union[ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue]] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt600000Uv06SupplyEvent:
    class Meta:
        name = "COCT_MT600000UV06.SupplyEvent"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    product: List[CoctMt600000Uv06Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    performer: Optional[CoctMt600000Uv06Performer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    origin: Optional[CoctMt600000Uv06Origin] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    destination: Optional[CoctMt600000Uv06Destination] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: Optional[CoctMt600000Uv06Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    pertinent_information1: List[CoctMt600000Uv06PertinentInformation1] = field(
        default_factory=list,
        metadata={
            "name": "pertinentInformation1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    pertinent_information2: Optional[CoctMt600000Uv06PertinentInformation2] = field(
        default=None,
        metadata={
            "name": "pertinentInformation2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    pertinent_information3: List[CoctMt600000Uv06PertinentInformation] = field(
        default_factory=list,
        metadata={
            "name": "pertinentInformation3",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassSupply] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
