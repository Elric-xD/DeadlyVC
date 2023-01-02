from pyrogram import Client, errors
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from youtubesearchpython import VideosSearch
from Deadly import GROUP_SUPPORT, UPDATES_CHANNEL
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0

def audio_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• Cᴘᴀɴᴀʟ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ •", callback_data=f'cbsupport'),
    ],
    [
      InlineKeyboardButton(text="Close🗑", callback_data=f'cls'),
    ],
  ]
  return buttons

def stream_markup(user_id, videoid):
  buttons = [
    [
      InlineKeyboardButton(text="• Cᴘᴀɴᴀʟ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ •", callback_data=f'cbsupport'),
    ],
    [
      InlineKeyboardButton(text="Close🗑", callback_data=f'cls'),
    ],    
  ]
  return buttons

def menu_markup(user_id, videoid):
  buttons = [
    [
      InlineKeyboardButton(text="IIPause", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷Resume", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="‣‣ISkip", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="▢Stop", callback_data=f'cbstop | {user_id}'), 
    ],
    [
      InlineKeyboardButton(text="Next▶️", callback_data=f'cbnext | {user_id}'), 
      InlineKeyboardButton("Close🗑", callback_data="cls"), 
      
    ], 
  ]
  return buttons

def nexta_markup(user_id, videoid):
  buttons = [
    [
      InlineKeyboardButton(text="🔇Mute", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="🔊Unmute", callback_data=f'cbunmute | {user_id}'), 
    ], 
    [
      InlineKeyboardButton(text="🔽Down", callback_data=f'cbdown | {videoid}'),         
      InlineKeyboardButton(text="• Inline", switch_inline_query_current_chat=""),
    ]
    [
      InlineKeyboardButton(text="◀️Back", callback_data=f'cbmenu'),         
      InlineKeyboardButton(
        "Close🗑", callback_data="cls"
      ), 
    ]
  ]
  return buttons   


def song_download_markup(videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="⬇️ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}",
            ),
            InlineKeyboardButton(
                text="⬇️ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ",
                callback_data="cbhome",
            )
        ],
    ]
    return buttons

close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "Close🗑", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "• ʙᴀᴄᴋ •", callback_data="cbmenu"
      )
    ]
  ]
)
