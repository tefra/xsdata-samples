from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..core.datatypes_base import (
    AdExplicit,
    Bl,
    Cd,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    Int,
    IvlTsExplicit,
    Pq,
    SxcmTsExplicit,
    Tel,
)
from ..core.voc import (
    ActClass,
    ActClassObservation,
    ActMood,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipFulfills,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPertainsValue,
    ActRelationshipPosting,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    ContextControl,
    NullFlavor,
    ParticipationTargetLocation,
    ParticipationTargetSubject,
    ParticipationType,
    RoleClassServiceDeliveryLocation,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XSuccReplPrev,
)
from .coct_mt020000_uv01 import CoctMt020000Uv01Appointment
from .coct_mt040200_uv01 import CoctMt040200Uv01ResponsibleParty
from .coct_mt050000_uv01 import CoctMt050000Uv01Patient
from .coct_mt060000_uv01 import CoctMt060000Uv01Transportation
from .coct_mt090000_uv01 import CoctMt090000Uv01AssignedEntity
from .coct_mt090100_uv01 import CoctMt090100Uv01AssignedPerson
from .coct_mt090200_uv01 import CoctMt090200Uv01AssignedOrganization
from .coct_mt110000_uv04 import CoctMt110000Uv04Account
from .coct_mt120104_uv import CoctMt120104UvObservationDx
from .coct_mt150000_uv02 import CoctMt150000Uv02Organization
from .coct_mt470000_uv import CoctMt470000UvConsent
from .coct_mt710000_uv01 import CoctMt710000Uv01Place

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt010000Uv01AccomodationEvent:
    class Meta:
        name = "COCT_MT010000UV01.AccomodationEvent"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Cd | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: list[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    reason_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "reasonCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.ACCM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Admitter:
    class Meta:
        name = "COCT_MT010000UV01.Admitter"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    mode_code: Ce | None = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_person: CoctMt090100Uv01AssignedPerson | None = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.ADM,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Attender:
    class Meta:
        name = "COCT_MT010000UV01.Attender"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    mode_code: Ce | None = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: Cs | None = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_person: CoctMt090100Uv01AssignedPerson | None = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.ATND,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Authorization:
    class Meta:
        name = "COCT_MT010000UV01.Authorization"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    consent: CoctMt470000UvConsent | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipConditional | ActRelationshipHasComponent | ActRelationshipOutcome | ActRelationshipCostTracking | ActRelationshipPosting | str | ActRelationshipHasSupport | ActRelationshipTemporallyPertains | ActRelationshipPertainsValue | ActRelationshipSequel | XActRelationshipDocument | XActRelationshipEntry | XActRelationshipEntryRelationship | XActRelationshipExternalReference | XActRelationshipPatientTransport | XActRelationshipPertinentInfo | XActRelationshipRelatedAuthorizations | XActReplaceOrRevise | XSuccReplPrev = field(
        init=False,
        default=ActRelationshipPertainsValue.AUTH,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt010000Uv01CauseOf:
    class Meta:
        name = "COCT_MT010000UV01.CauseOf"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    encounter: CoctMt010000Uv01Encounter | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipConditional | ActRelationshipHasComponent | ActRelationshipOutcome | ActRelationshipCostTracking | ActRelationshipPosting | str | ActRelationshipHasSupport | ActRelationshipTemporallyPertains | ActRelationshipPertainsValue | ActRelationshipSequel | XActRelationshipDocument | XActRelationshipEntry | XActRelationshipEntryRelationship | XActRelationshipExternalReference | XActRelationshipPatientTransport | XActRelationshipPertinentInfo | XActRelationshipRelatedAuthorizations | XActReplaceOrRevise | XSuccReplPrev = field(
        init=False,
        default=ActRelationshipPertainsValue.CAUS,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt010000Uv01Component:
    class Meta:
        name = "COCT_MT010000UV01.Component"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    encounter: CoctMt010000Uv01Encounter | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipHasComponent | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )
    context_control_code: ContextControl | None = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass
class CoctMt010000Uv01Consultant:
    class Meta:
        name = "COCT_MT010000UV01.Consultant"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    mode_code: Ce | None = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_person: CoctMt090100Uv01AssignedPerson | None = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.CON,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Discharger:
    class Meta:
        name = "COCT_MT010000UV01.Discharger"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    mode_code: Ce | None = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_person: CoctMt090100Uv01AssignedPerson | None = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.DIS,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01InFulfillmentOf:
    class Meta:
        name = "COCT_MT010000UV01.InFulfillmentOf"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    appointment: CoctMt020000Uv01Appointment | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipFulfills | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01NotificationContact:
    class Meta:
        name = "COCT_MT010000UV01.NotificationContact"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    responsible_party: CoctMt040200Uv01ResponsibleParty | None = field(
        default=None,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.NOT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01ObservationEvent02:
    class Meta:
        name = "COCT_MT010000UV01.ObservationEvent02"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    text: EdExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    value: EdExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClassObservation | None = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )
    negation_ind: str | None = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class CoctMt010000Uv01PertinentInformation2:
    class Meta:
        name = "COCT_MT010000UV01.PertinentInformation2"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    priority_number: Int | None = field(
        default=None,
        metadata={
            "name": "priorityNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    observation_dx: CoctMt120104UvObservationDx | None = field(
        default=None,
        metadata={
            "name": "observationDx",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipCostTracking | ActRelationshipPosting | str | ActRelationshipHasSupport | ActRelationshipTemporallyPertains | ActRelationshipPertainsValue | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt010000Uv01Reference:
    class Meta:
        name = "COCT_MT010000UV01.Reference"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    account: CoctMt110000Uv04Account | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipConditional | ActRelationshipHasComponent | ActRelationshipOutcome | ActRelationshipCostTracking | ActRelationshipPosting | str | ActRelationshipHasSupport | ActRelationshipTemporallyPertains | ActRelationshipPertainsValue | ActRelationshipSequel | XActRelationshipDocument | XActRelationshipEntry | XActRelationshipEntryRelationship | XActRelationshipExternalReference | XActRelationshipPatientTransport | XActRelationshipPertinentInfo | XActRelationshipRelatedAuthorizations | XActReplaceOrRevise | XSuccReplPrev = field(
        init=False,
        default=ActRelationshipPertainsValue.REFR,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt010000Uv01Referrer:
    class Meta:
        name = "COCT_MT010000UV01.Referrer"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    mode_code: Ce | None = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_entity: CoctMt090000Uv01AssignedEntity | None = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.REF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01ResponsibleParty1:
    class Meta:
        name = "COCT_MT010000UV01.ResponsibleParty1"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: Cs | None = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_organization: CoctMt090200Uv01AssignedOrganization | None = (
        field(
            default=None,
            metadata={
                "name": "assignedOrganization",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.RESP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Subject1:
    class Meta:
        name = "COCT_MT010000UV01.Subject1"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    patient: CoctMt050000Uv01Patient | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationTargetSubject | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01TransportedBy:
    class Meta:
        name = "COCT_MT010000UV01.TransportedBy"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    transportation: CoctMt060000Uv01Transportation | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: XActRelationshipPatientTransport | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Location3:
    class Meta:
        name = "COCT_MT010000UV01.Location3"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    accomodation_event: CoctMt010000Uv01AccomodationEvent | None = field(
        default=None,
        metadata={
            "name": "accomodationEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationTargetLocation | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01PertinentInformation3:
    class Meta:
        name = "COCT_MT010000UV01.PertinentInformation3"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    observation_event: CoctMt010000Uv01ObservationEvent02 | None = field(
        default=None,
        metadata={
            "name": "observationEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipCostTracking | ActRelationshipPosting | str | ActRelationshipHasSupport | ActRelationshipTemporallyPertains | ActRelationshipPertainsValue | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt010000Uv01ServiceDeliveryLocation:
    class Meta:
        name = "COCT_MT010000UV01.ServiceDeliveryLocation"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Ce | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    addr: list[AdExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[Tel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: Cs | None = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    location: CoctMt710000Uv01Place | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    service_provider_organization: CoctMt150000Uv02Organization | None = (
        field(
            default=None,
            metadata={
                "name": "serviceProviderOrganization",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    location_of: list[CoctMt010000Uv01Location3] = field(
        default_factory=list,
        metadata={
            "name": "locationOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassServiceDeliveryLocation | None = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Location1:
    class Meta:
        name = "COCT_MT010000UV01.Location1"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: Cs | None = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    service_delivery_location: CoctMt010000Uv01ServiceDeliveryLocation | None = field(
        default=None,
        metadata={
            "name": "serviceDeliveryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationTargetLocation | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01Encounter:
    class Meta:
        name = "COCT_MT010000UV01.Encounter"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    code: Cd | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: Cs | None = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    effective_time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    activity_time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "name": "activityTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    priority_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    confidentiality_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    reason_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "reasonCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    admission_referral_source_code: Ce | None = field(
        default=None,
        metadata={
            "name": "admissionReferralSourceCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    length_of_stay_quantity: Pq | None = field(
        default=None,
        metadata={
            "name": "lengthOfStayQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    discharge_disposition_code: Ce | None = field(
        default=None,
        metadata={
            "name": "dischargeDispositionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    pre_admit_test_ind: Bl | None = field(
        default=None,
        metadata={
            "name": "preAdmitTestInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    special_courtesies_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "specialCourtesiesCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    special_arrangement_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "specialArrangementCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    subject: CoctMt010000Uv01Subject1 | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    responsible_party: list[CoctMt010000Uv01ResponsibleParty1] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    admitter: CoctMt010000Uv01Admitter | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    attender: list[CoctMt010000Uv01Attender] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    discharger: CoctMt010000Uv01Discharger | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    referrer: CoctMt010000Uv01Referrer | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    consultant: list[CoctMt010000Uv01Consultant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    notification_contact: list[CoctMt010000Uv01NotificationContact] = field(
        default_factory=list,
        metadata={
            "name": "notificationContact",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    location: list[CoctMt010000Uv01Location1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    in_fulfillment_of: CoctMt010000Uv01InFulfillmentOf | None = field(
        default=None,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    sequel_to: CoctMt010000Uv01SequelTo | None = field(
        default=None,
        metadata={
            "name": "sequelTo",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    cause_of: list[CoctMt010000Uv01CauseOf] = field(
        default_factory=list,
        metadata={
            "name": "causeOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    authorization: list[CoctMt010000Uv01Authorization] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    reference: list[CoctMt010000Uv01Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    pertinent_information1: list[CoctMt010000Uv01PertinentInformation2] = (
        field(
            default_factory=list,
            metadata={
                "name": "pertinentInformation1",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    pertinent_information2: list[CoctMt010000Uv01PertinentInformation3] = (
        field(
            default_factory=list,
            metadata={
                "name": "pertinentInformation2",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    transported_by: list[CoctMt010000Uv01TransportedBy] = field(
        default_factory=list,
        metadata={
            "name": "transportedBy",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    component_of: list[CoctMt010000Uv01Component] = field(
        default_factory=list,
        metadata={
            "name": "componentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.ENC,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt010000Uv01SequelTo:
    class Meta:
        name = "COCT_MT010000UV01.SequelTo"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    encounter: CoctMt010000Uv01Encounter | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipSequel | None = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )
