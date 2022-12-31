from Deadly import user1, user2, user3, user4, user5, user6, user7
from Deadly import STRING1, STRING2,  STRING3, STRING4, STRING5, STRING6, STRING7

MULTI_ASSISTANT = ["1", "2", "3", "4", "5", " 6", "7"]


ASS_IDS = []
ASS_ID1 = 0
ASS_NAME1 = ""
ASS_USERNAME1 = ""
ASS_MENTION1 = ""
ASS_ID2 = 0
ASS_NAME2 = ""
ASS_USERNAME2 = ""
ASS_MENTION2 = ""
ASS_ID3 = 0
ASS_NAME3 = ""
ASS_USERNAME3 = ""
ASS_MENTION3 = ""
ASS_ID4 = 0
ASS_NAME4 = ""
ASS_USERNAME4 = ""
ASS_MENTION4 = ""
ASS_ID5 = 0
ASS_NAME5 = ""
ASS_USERNAME5 = ""
ASS_MENTION5 = ""
ASS_ID6 = 0
ASS_NAME6 = ""
ASS_USERNAME6 = ""
ASS_MENTION6 = ""
ASS_ID7 = 0
ASS_NAME7 = ""
ASS_USERNAME7 = ""
ASS_MENTION7 = ""


async def get_assistant_details(assistant: int):
# ASSISTANT 1
    if STRING1 != "None":
       getme1 = await user1.get_me()
       ASS_ID1 = getme1.id
       ASS_IDS.append(ASS_ID1)
       ASS_NAME1 = (
           f"{getme1.first_name} {getme1.last_name}"
           if getme1.last_name
           else getme1.first_name
       )
       ASS_USERNAME1 = getme1.username
       ASS_MENTION1 = getme1.mention
# ASSISTANT 2
    if STRING2 != "None":
       getme2 = await user.get_me()
       ASS_ID2 = getme2.id
       ASS_IDS.append(ASS_ID2)
       ASS_NAME2 = (
           f"{getme2.first_name} {getme2.last_name}"
           if getme2.last_name
           else getme2.first_name
       )
       ASS_USERNAME2 = getme2.username
       ASS_MENTION2 = getme2.mention
# ASSISTANT 3
    if STRING3 != "None":
       getme3 = await user3.get_me()
       ASS_ID3 = getme3.id
       ASS_IDS.append(ASS_ID3)
       ASS_NAME3 = (
           f"{getme3.first_name} {getme3.last_name}"
           if getme3.last_name
           else getme3.first_name
       )
       ASS_USERNAME3 = getme3.username
       ASS_MENTION3 = getme3.mention
# ASSISTANT 4
    if STRING4 != "None":
       getme4 = await user4.get_me()
       ASS_ID4 = getme4.id
       ASS_IDS.append(ASS_ID4)
       ASS_NAME4 = (
           f"{getme4.first_name} {getme4.last_name}"
           if getme4.last_name
           else getme4.first_name
       )
       ASS_USERNAME4 = getme4.username
       ASS_MENTION4 = getme4.mention
# ASSISTANT 5
    if STRING5 != "None":
       getme5 = await user5.get_me()
       ASS_ID5 = getme5.id
       ASS_IDS.append(ASS_ID5)
       ASS_NAME5 = (
           f"{getme5.first_name} {getme5.last_name}"
           if getme5.last_name
           else getme5.first_name
       )
       ASS_USERNAME5 = getme5.username
       ASS_MENTION5 = getme5.mention
# ASSISTANT 6
    if STRING6 != "None":
       getme6 = await user6.get_me()
       ASS_ID6 = getme6.id
       ASS_IDS.append(ASS_ID6)
       ASS_NAME6 = (
           f"{getme6.first_name} {getme6.last_name}"
           if getme6.last_name
           else getme6.first_name
       )
       ASS_USERNAME5 = getme5.username
       ASS_MENTION5 = getme5.mention
# ASSISTANT 7
    if STRING7 != "None":
       getme7 = await user7.get_me()
       ASS_ID7 = getme7.id
       ASS_IDS.append(ASS_ID7)
       ASS_NAME7 = (
           f"{getme7.first_name} {getme7.last_name}"
           if getme7.last_name
           else getme7.first_name
       )
       ASS_USERNAME7 = getme7.username
       ASS_MENTION7 = getme7.mention
    if int(assistant) == 1:
        x = ASS_ID1
        y = ASS_NAME1
        z = ASS_USERNAME1
        a = user1
    elif int(assistant) == 2:
        x = ASS_ID2
        y = ASS_NAME2
        z = ASS_USERNAME2
        a = user2
    elif int(assistant) == 3:
        x = ASS_ID3
        y = ASS_NAME3
        z = ASS_USERNAME3
        a = user3
    elif int(assistant) == 4:
        x = ASS_ID4
        y = ASS_NAME4
        z = ASS_USERNAME4
        a = user4
    elif int(assistant) == 5:
        x = ASS_ID5
        y = ASS_NAME5
        z = ASS_USERNAME5
        a = user5
    elif int(assistant) == 6:
        x = ASS_ID6
        y = ASS_NAME6
        z = ASS_USERNAME6
        a = user6
    elif int(assistant) == 7:
        x = ASS_ID7
        y = ASS_NAME7
        z = ASS_USERNAME7
        a = user7

    return x, y, z, a
