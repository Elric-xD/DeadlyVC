from Deadly import LODER, user2, user3
from Deadly import SESSION1, STRING2,  STRING3

MULTI_ASSISTANT = ["1", "2", "3"]


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



async def get_assistant_details(assistant: int):
    if SESSION_NAME != "None":
       getme1 = await Test.get_me()
       ASSID1 = getme1.id
       ASSIDS.append(ASSID1)
       ASSNAME1 = (
           f"{getme1.first_name} {getme1.last_name}"
           if getme1.last_name
           else getme1.first_name
       )
       ASSUSERNAME1 = getme1.username
       ASSMENTION1 = getme1.mention
    if SESSION2 != "None":
       getme2 = await user.get_me()
       ASSID2 = getme2.id
       ASSIDS.append(ASSID2)
       ASSNAME2 = (
           f"{getme2.first_name} {getme2.last_name}"
           if getme2.last_name
           else getme2.first_name
       )
       ASSUSERNAME2 = getme2.username
       ASSMENTION2 = getme2.mention
    if SESSION3 != "None":
       getme3 = await user3.get_me()
       ASSID3 = getme3.id
       ASSIDS.append(ASSID3)
       ASSNAME3 = (
           f"{getme3.first_name} {getme3.last_name}"
           if getme3.last_name
           else getme3.first_name
       )
       ASSUSERNAME3 = getme3.username
       ASSMENTION3 = getme3.mention


     
    if int(assistant) == 1:
        x = ASS_ID1
        y = ASS_NAME1
        z = ASS_USERNAME1
        a = TEST
    elif int(assistant) == 2:
        x = ASS_ID2
        y = ASS_NAME2
        z = ASS_USERNAME2
        a = user
    elif int(assistant) == 3:
        x = ASS_ID3
        y = ASS_NAME3
        z = ASS_USERNAME3
        a = user3
    elif int(assistant) == 4:
        x = ASSID1
        y = ASSNAME1
        z = ASSUSERNAME1
        a = LODER
    return x, y, z, a
