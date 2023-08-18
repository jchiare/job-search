from typing import Any, Dict, List

from pydantic import BaseModel


class PositionLocationItem(BaseModel):
    LocationName: str
    CountryCode: str
    CountrySubDivisionCode: str
    CityName: str
    Longitude: float
    Latitude: float


class JobCategoryItem(BaseModel):
    Name: str
    Code: str


class JobGradeItem(BaseModel):
    Code: str


class PositionScheduleItem(BaseModel):
    Name: str
    Code: str


class PositionOfferingTypeItem(BaseModel):
    Name: str
    Code: str


class PositionRemunerationItem(BaseModel):
    MinimumRange: str
    MaximumRange: str
    RateIntervalCode: str
    Description: str


class PositionFormattedDescriptionItem(BaseModel):
    Label: str
    LabelDescription: str


class WhoMayApply(BaseModel):
    Name: str
    Code: str


class Details(BaseModel):
    JobSummary: str
    WhoMayApply: WhoMayApply
    LowGrade: str
    HighGrade: str
    PromotionPotential: str
    OrganizationCodes: str
    Relocation: str
    HiringPath: List[str]
    TotalOpenings: str
    AgencyMarketingStatement: str
    TravelCode: str
    ApplyOnlineUrl: str
    DetailStatusUrl: str
    MajorDuties: List[str]
    Education: str
    Requirements: str
    Evaluations: str
    HowToApply: str
    WhatToExpectNext: str
    RequiredDocuments: str
    Benefits: str
    BenefitsDisplayDefaultText: bool
    OtherInformation: str
    KeyRequirements: List[str]
    WithinArea: str
    CommuteDistance: str
    ServiceType: str
    AnnouncementClosingType: str
    AgencyContactEmail: str
    AgencyContactPhone: str
    SecurityClearance: str
    DrugTestRequired: str
    AdjudicationType: List
    TeleworkEligible: bool
    RemoteIndicator: bool


class UserArea(BaseModel):
    Details: Details
    IsRadialSearch: bool


class MatchedObjectDescriptor(BaseModel):
    PositionID: str
    PositionTitle: str
    PositionURI: str
    ApplyURI: List[str]
    PositionLocationDisplay: str
    PositionLocation: List[PositionLocationItem]
    OrganizationName: str
    DepartmentName: str
    JobCategory: List[JobCategoryItem]
    JobGrade: List[JobGradeItem]
    PositionSchedule: List[PositionScheduleItem]
    PositionOfferingType: List[PositionOfferingTypeItem]
    QualificationSummary: str
    PositionRemuneration: List[PositionRemunerationItem]
    PositionStartDate: str
    PositionEndDate: str
    PublicationStartDate: str
    ApplicationCloseDate: str
    PositionFormattedDescription: List[PositionFormattedDescriptionItem]
    UserArea: UserArea


class SearchResultItem(BaseModel):
    MatchedObjectId: str
    MatchedObjectDescriptor: MatchedObjectDescriptor
    RelevanceRank: int


class UserArea1(BaseModel):
    NumberOfPages: str
    IsRadialSearch: bool


class SearchResult(BaseModel):
    SearchResultCount: int
    SearchResultCountAll: int
    SearchResultItems: List[SearchResultItem]
    UserArea: UserArea1


class GovernmentJobsApiResponse(BaseModel):
    LanguageCode: str
    SearchParameters: Dict[str, Any]
    SearchResult: SearchResult
