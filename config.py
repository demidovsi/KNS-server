schema_name = 'kns'
user_name = 'superadmin'
password = 'wqzDi8OVw43DjcOOwoTCncKZwpM='
kirill = 'wqzDi8OVw43DjcOOwoTCncKZwpM='
url = "http://159.223.0.234:5000/"
_url = "http://127.0.0.1:5000/"
base_url = "http://knesset.gov.il/Odata/ParliamentInfo.svc/"

entities = [
    # {"endpoint": "KNS_ItemType()", "function_name": "pw_nsi_itemtype", "fields": [
    #     {"field": "ItemTypeID"}, {"field": "Desc", "str": 1}, {"field": "TableName", "str": 1}
    # ]},
    # {"endpoint": "KNS_Status()", "function_name": "pw_nsi_status", "fields": [
    #     {"field": "StatusID"}, {"field": "Desc", "str": 1}, {"field": "TypeID"}, {"field": "TypeDesc", "str": 1},
    #     {"field": "OrderTransition"}, {"field": "IsActive"}, {"field": 'LastUpdatedDate', "str": 1}
    # ]},
    # {"endpoint": "KNS_GovMinistry()", "function_name": "pw_nsi_govministry", "fields": [
    #     {"field": "GovMinistryID"}, {"field": "Name", "str": 1},
    #     {"field": "IsActive"}, {"field": 'LastUpdatedDate', "str": 1}
    # ]},
    # {"endpoint": "KNS_KnessetDates()", "function_name": "pw_nsi_knessetdates", "fields": [
    #     {"field": "KnessetDateID"}, {"field": "Name", "str": 1}, {"field": "KnessetNum"},
    #     {"field": "Assembly"}, {"field": "Plenum"},
    #     {"field": "PlenumStart", "str": 1}, {"field": "PlenumFinish", "str": 1},
    #     {"field": "IsCurrent"}, {"field": 'LastUpdatedDate', "str": 1}
    # ]},
    # {"endpoint": "KNS_Person()", "function_name": "pw_nsi_person", "fields": [
    #     {"field": "PersonID"},
    #     {"field": "GenderID"},
    #     {"field": "IsCurrent"},
    #     {"field": "LastUpdatedDate", "str": 1},
    #
    #     {"field": "LastName", "str": 1},
    #     {"field": "FirstName", "str": 1},
    #     {"field": "GenderDesc", "str": 1},
    #     {"field": "Email", "str": 1}
    # ]},
    # {"endpoint": "KNS_Position()", "function_name": "pw_nsi_position", "fields": [
    #     {"field": "PositionID"},
    #     {"field": "Description", "str": 1},
    #     {"field": "GenderID"},
    #     {"field": "GenderDesc", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_PersonToPosition()", "function_name": "pw_nsi_persontoposition", "fields": [
    #     {"field": "PersonToPositionID"},
    #     {"field": "PersonID"},
    #     {"field": "PositionID"},
    #     {"field": "KnessetNum"},
    #     {"field": "GovMinistryID"},
    #     {"field": "GovMinistryName", "str": 1},
    #     {"field": "DutyDesc", "str": 1},
    #     {"field": "FactionID"},
    #     {"field": "FactionName", "str": 1},
    #     {"field": "GovernmentNum"},
    #     {"field": "CommitteeID"},
    #     {"field": "CommitteeName", "str": 1},
    #     {"field": "StartDate", "str": 1},
    #     {"field": "FinishDate", "str": 1},
    #     {"field": "IsCurrent"},
    #     {"field": "LastUpdatedDate", "str": 1}
    #  ]},
    # {"endpoint": "KNS_Faction()", "function_name": "pw_nsi_faction", "fields": [
    #     {"field": "FactionID"}, {"field": "Name", "str": 1},
    #     {"field": "KnessetNum"},
    #     {"field": "StartDate", "str": 1},
    #     {"field": "FinishDate", "str": 1},
    #     {"field": "IsCurrent"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_PlenumSession()", "function_name": "pw_nsi_plenumsession", "fields": [
    #     {"field": "PlenumSessionID"},
    #     {"field": "Number"},
    #     {"field": "KnessetNum"},
    #     {"field": "Name", "str": 1},
    #     {"field": "StartDate", "str": 1},
    #     {"field": "FinishDate", "str": 1},
    #     {"field": "IsSpecialMeeting"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_PlmSessionItem()", "function_name": "pw_nsi_plmsessionitem", "fields": [
    #     {"field": "plmPlenumSessionID"},
    #     {"field": "ItemID"},
    #     {"field": "PlenumSessionID"},
    #     {"field": "ItemTypeID"},
    #     {"field": "ItemTypeDesc", "str": 1},
    #     {"field": "Ordinal"},
    #     {"field": "Name", "str": 1},
    #     {"field": "StatusID"},
    #     {"field": "IsDiscussion"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_DocumentPlenumSession()", "function_name": "pw_nsi_documentplenumsession", "fields": [
    #     {"field": "DocumentPlenumSessionID"},
    #     {"field": "PlenumSessionID"},
    #     {"field": "GroupTypeID"},
    #
    #     {"field": "GroupTypeDesc", "str": 1},
    #     {"field": "ApplicationID"},
    #     {"field": "ApplicationDesc", "str": 1},
    #     {"field": "FilePath", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_CommitteeSession()", "function_name": "pw_nsi_committeesession", "fields": [
    #     {"field": "CommitteeSessionID"},
    #     {"field": "Number"},
    #     {"field": "KnessetNum"},
    #     {"field": "TypeID"},
    #     {"field": "TypeDesc", "str": 1},
    #     {"field": "CommitteeID"},
    #     {"field": "Location", "str": 1},
    #     {"field": "SessionUrl", "str": 1},
    #     {"field": "BroadcastUrl", "str": 1},
    #     {"field": "StartDate", "str": 1},
    #     {"field": "FinishDate", "str": 1},
    #     {"field": "Note", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_CmtSessionItem()", "function_name": "pw_nsi_cmtsessionitem", "fields": [
    #     {"field": "CmtSessionItemID"},
    #     {"field": "ItemID"},
    #     {"field": "CommitteeSessionID"},
    #     {"field": "Ordinal"},
    #     {"field": "StatusID"},
    #     {"field": "Name", "str": 1},
    #     {"field": "ItemTypeID"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_DocumentCommitteeSession()", "function_name": "pw_nsi_documentcommitteesession", "fields": [
    #     {"field": "DocumentCommitteeSessionID"},
    #     {"field": "CommitteeSessionID"},
    #     {"field": "GroupTypeID"},
    #     {"field": "GroupTypeDesc", "str": 1},
    #     {"field": "ApplicationID"},
    #     {"field": "FilePath", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_Committee()", "function_name": "pw_nsi_committee", "fields": [
    #     {"field": "CommitteeID"},
    #     {"field": "Name", "str": 1},
    #     {"field": "CategoryID"},
    #     {"field": "CategoryDesc", "str": 1},
    #     {"field": "KnessetNum"},
    #     {"field": "CommitteeTypeID"},
    #     {"field": "CommitteeTypeDesc", "str": 1},
    #     {"field": "Email", "str": 1},
    #     {"field": "StartDate", "str": 1},
    #     {"field": "FinishDate", "str": 1},
    #     {"field": "AdditionalTypeID"},
    #     {"field": "AdditionalTypeDesc", "str": 1},
    #     {"field": "ParentCommitteeID"},
    #     {"field": "CommitteeParentName", "str": 1},
    #     {"field": "IsCurrent"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_JointCommittee()", "function_name": "pw_nsi_jointcommittee", "fields": [
    #     {"field": "JointCommitteeID"},
    #     {"field": "CommitteeID"},
    #     {"field": "ParticipantCommitteeID"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_CmtSiteCode()", "function_name": "pw_nsi_cmtsitecode", "fields": [
    #     {"field": "CmtSiteCode"},
    #     {"field": "KnsID"},
    #     {"field": "SiteId"},
    # ]},
    # {"endpoint": "KNS_Query()", "function_name": "pw_nsi_query", "fields": [
    #     {"field": "QueryID"},
    #     {"field": "Number"},
    #     {"field": "KnessetNum"},
    #     {"field": "Name", "str": 1},
    #     {"field": "TypeID"},
    #     {"field": "TypeDesc", "str": 1},
    #     {"field": "StatusID"},
    #     {"field": "PersonID"},
    #     {"field": "GovMinistryID"},
    #     {"field": "SubmitDate", "str": 1},
    #     {"field": "ReplyMinisterDate", "str": 1},
    #     {"field": "ReplyDatePlanned", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_DocumentQuery()", "function_name": "pw_nsi_documentquery", "fields": [
    #     {"field": "DocumentQueryID"},
    #     {"field": "QueryID"},
    #     {"field": "GroupTypeID"},
    #     {"field": "GroupTypeDesc", "str": 1},
    #     {"field": "ApplicationID"},
    #     {"field": "ApplicationDesc", "str": 1},
    #     {"field": "FilePath", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_Agenda()", "function_name": "pw_nsi_agenda", "fields": [
    #     {"field": "AgendaID"},
    #     {"field": "Number"},
    #     {"field": "ClassificationID"},
    #     {"field": "ClassificationDesc", "str": 1},
    #     {"field": "LeadingAgendaID"},
    #     {"field": "KnessetNum"},
    #     {"field": "Name", "str": 1},
    #     {"field": "SubTypeID"},
    #     {"field": "SubTypeDesc", "str": 1},
    #     {"field": "StatusID"},
    #     {"field": "InitiatorPersonID"},
    #     {"field": "GovRecommendationID"},
    #     {"field": "GovRecommendationDesc", "str": 1},
    #     {"field": "PresidentDecisionDate", "str": 1},
    #     {"field": "PostopenmentReasonID"},
    #     {"field": "PostopenmentReasonDesc", "str": 1},
    #     {"field": "CommitteeID"},
    #     {"field": "RecommendCommitteeID"},
    #     {"field": "MinisterPersonID"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_DocumentAgenda()", "function_name": "pw_nsi_documentagenda", "fields": [
    #     {"field": "DocumentAgendaID"},
    #     {"field": "AgendaID"},
    #     {"field": "GroupTypeID"},
    #     {"field": "GroupTypeDesc", "str": 1},
    #     {"field": "ApplicationID"},
    #     {"field": "ApplicationDesc", "str": 1},
    #     {"field": "FilePath", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_DocumentIsraelLaw()", "function_name": "pw_nsi_documentisraellaw", "fields": [
    #     {"field": "DocumentIsraelLawID"},
    #     {"field": "IsraelLawID"},
    #     {"field": "GroupTypeID"},
    #     {"field": "GroupTypeDesc", "str": 1},
    #     {"field": "ApplicationID"},
    #     {"field": "ApplicationDesc", "str": 1},
    #     {"field": "FilePath", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_IsraelLawName()", "function_name": "pw_nsi_israellawname", "fields": [
    #     {"field": "IsraelLawNameID"},
    #     {"field": "IsraelLawID"},
    #     {"field": "LawID"},
    #     {"field": "LawTypeID"},
    #     {"field": "Name", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_IsraelLawMinistry()", "function_name": "pw_nsi_israellawministry", "fields": [
    #     {"field": "LawMinistryID"},
    #     {"field": "IsraelLawID"},
    #     {"field": "GovMinistryID"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_IsraelLawClassificiation()", "function_name": "pw_nsi_israellawclassificiation", "fields": [
    #     {"field": "LawClassificiationID"},
    #     {"field": "IsraelLawID"},
    #     {"field": "ClassificiationID"},
    #     {"field": "ClassificiationDesc", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_IsraelLawBinding()", "function_name": "pw_nsi_israellawbinding", "fields": [
    #     {"field": "IsraelLawBinding"},
    #     {"field": "IsraelLawID"},
    #     {"field": "IsraelLawReplacedID"},
    #     {"field": "LawID"},
    #     {"field": "LawTypeID"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_IsraelLaw()", "function_name": "pw_nsi_israellaw", "fields": [
    #     {"field": "IsraelLawID"},
    #     {"field": "KnessetNum"},
    #     {"field": "Name", "str": 1},
    #     {"field": "IsBasicLaw"},
    #     {"field": "IsFavoriteLaw"},
    #     {"field": "IsBudgetLaw"},
    #     {"field": "PublicationDate", "str": 1},
    #     {"field": "LatestPublicationDate", "str": 1},
    #     {"field": "LawValidityID"},
    #     {"field": "LawValidityDesc", "str": 1},
    #     {"field": "ValidityStartDate", "str": 1},
    #     {"field": "ValidityStartDateNotes", "str": 1},
    #     {"field": "ValidityFinishDate", "str": 1},
    #     {"field": "ValidityFinishDateNotes", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_DocumentLaw()", "function_name": "pw_nsi_documentlaw", "fields": [
    #     {"field": "DocumentLawID"},
    #     {"field": "LawID"},
    #     {"field": "GroupTypeID"},
    #     {"field": "GroupTypeDesc", "str": 1},
    #     {"field": "ApplicationID"},
    #     {"field": "ApplicationDesc", "str": 1},
    #     {"field": "FilePath", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_Law()", "function_name": "pw_nsi_law", "fields": [
    #     {"field": "LawID"},
    #     {"field": "TypeID"},
    #     {"field": "TypeDesc", "str": 1},
    #     {"field": "SubTypeID"},
    #     {"field": "SubTypeDesc", "str": 1},
    #     {"field": "KnessetNum"},
    #     {"field": "Name", "str": 1},
    #     {"field": "PublicationDate", "str": 1},
    #     {"field": "PublicationSeriesID"},
    #     {"field": "PublicationSeriesDesc", "str": 1},
    #     {"field": "MagazineNumber", "str": 1},
    #     {"field": "PageNumber", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_LawBinding()", "function_name": "pw_nsi_lawbinding", "fields": [
    #     {"field": "LawBindingID"},
    #     {"field": "LawID"},
    #     {"field": "LawTypeID"},
    #     {"field": "IsraelLawID"},
    #     {"field": "ParentLawID"},
    #     {"field": "LawParentTypeID"},
    #     {"field": "BindingType"},
    #     {"field": "BindingTypeDesc", "str": 1},
    #     {"field": "PageNumber", "str": 1},
    #     {"field": "AmendmentType"},
    #     {"field": "AmendmentTypeDesc", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_BillSplit()", "function_name": "pw_nsi_billsplit", "fields": [
    #     {"field": "BillSplitID"},
    #     {"field": "MainBillID"},
    #     {"field": "SplitBillID"},
    #     {"field": "Name", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_DocumentBill()", "function_name": "pw_nsi_documentbill", "skip": 53800, "fields": [
    #     {"field": "DocumentBillID"},
    #     {"field": "BillID"},
    #     {"field": "GroupTypeID"},
    #     {"field": "GroupTypeDesc", "str": 1},
    #     {"field": "ApplicationID"},
    #     {"field": "ApplicationDesc", "str": 1},
    #     {"field": "FilePath", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_BillUnion()", "function_name": "pw_nsi_billunion", "fields": [
    #     {"field": "BillUnionID"},
    #     {"field": "MainBillID"},
    #     {"field": "UnionBillID"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_BillHistoryInitiator()", "function_name": "pw_nsi_billhistoryinitiator", "fields": [
    #     {"field": "BillHistoryInitiatorID"},
    #     {"field": "BillID"},
    #     {"field": "PersonID"},
    #     {"field": "IsInitiator"},
    #     {"field": "StartDate", "str": 1},
    #     {"field": "EndDate", "str": 1},
    #     {"field": "ReasonID"},
    #     {"field": "ReasonDesc", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    # {"endpoint": "KNS_BillInitiator()", "function_name": "pw_nsi_billinitiator", "fields": [
    #     {"field": "BillInitiatorID"},
    #     {"field": "BillID"},
    #     {"field": "PersonID"},
    #     {"field": "IsInitiator"},
    #     {"field": "Ordinal"},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},
    {"endpoint": "KNS_BillName()", "function_name": "pw_nsi_billname", "fields": [
        {"field": "BillNameID"},
        {"field": "Name", "str": 1},
        {"field": "BillID"},
        {"field": "NameHistoryTypeID"},
        {"field": "NameHistoryTypeDesc", "str": 1},
        {"field": "LastUpdatedDate", "str": 1}
    ]},
    # {"endpoint": "KNS_Bill()", "function_name": "pw_nsi_bill", "skip": 3000, "fields": [
    #     {"field": "BillID"},
    #     {"field": "KnessetNum"},
    #     {"field": "Name", "str": 1},
    #     {"field": "SubTypeID"},
    #     {"field": "SubTypeDesc", "str": 1},
    #     {"field": "PrivateNumber"},
    #     {"field": "CommitteeID"},
    #     {"field": "StatusID"},
    #     {"field": "Number"},
    #     {"field": "PostponementReasonID"},
    #     {"field": "PostponementReasonDesc", "str": 1},
    #     {"field": "PublicationDate", "str": 1},
    #     {"field": "MagazineNumber"},
    #     {"field": "PageNumber"},
    #     {"field": "IsContinuationBill"},
    #     {"field": "SummaryLaw", "str": 1},
    #     {"field": "PublicationSeriesID"},
    #     {"field": "PublicationSeriesDesc", "str": 1},
    #     {"field": "PublicationSeriesFirstCallID"},
    #     {"field": "PublicationSeriesFirstCallDesc", "str": 1},
    #     {"field": "LastUpdatedDate", "str": 1}
    # ]},

]
