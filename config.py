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
    {"endpoint": "KNS_PlmSessionItem()", "function_name": "pw_nsi_plmsessionitem", "fields": [
        {"field": "plmPlenumSessionID"},
        {"field": "ItemID"},
        {"field": "PlenumSessionID"},
        {"field": "ItemTypeID"},
        {"field": "ItemTypeDesc", "str": 1},
        {"field": "Ordinal"},
        {"field": "Name", "str": 1},
        {"field": "StatusID"},
        {"field": "IsDiscussion"},
        {"field": "LastUpdatedDate", "str": 1}
    ]},
    {"endpoint": "KNS_DocumentPlenumSession()", "function_name": "pw_nsi_documentplenumsession", "fields": [
        {"field": "DocumentPlenumSessionID"},
        {"field": "PlenumSessionID"},
        {"field": "GroupTypeID"},
        {"field": "GroupTypeDesc", "str": 1},
        {"field": "ApplicationID"},
        {"field": "ApplicationDesc", "str": 1},
        {"field": "FilePath", "str": 1},
        {"field": "LastUpdatedDate", "str": 1}
    ]},
    ]
