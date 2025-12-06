# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio, logging, os, sys
from config import Config
from pyrogram import Client as VJ, filters, idle
from typing import Union, Optional, AsyncGenerator
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards

# ========== ULTRA FAST MODE FLAGS ==========
FAST_MODE = os.getenv("FAST_MODE", "0") == "1"
NO_DB_LOGS = os.getenv("NO_DB_LOGS", "0") == "1"
FIX_MEDIA_GROUPS = os.getenv("FIX_MEDIA_GROUPS", "0") == "1"

# CLI Flag support
for arg in sys.argv:
    if arg == "--fast-mode": os.environ["FAST_MODE"] = "1"
    if arg == "--no-db-logs": os.environ["NO_DB_LOGS"] = "1"
    if arg == "--fix-media-groups": os.environ["FIX_MEDIA_GROUPS"] = "1"

print(f"⚡ FAST_MODE: {FAST_MODE} | FIX_MEDIA: {FIX_MEDIA_GROUPS} | NO_DB_LOGS: {NO_DB_LOGS}")
# ===========================================

if __name__ == "__main__":
    VJBot = VJ(
        "VJ-Forward-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=dict(root="plugins")
    )  
    
    # ========== ULTRA FAST MEDIA GROUP FIX ==========
    if FIX_MEDIA_GROUPS:
        @VJBot.on_message(filters.media_group & filters.private)
        async def handle_media_group(client, message):
            try:
                if message.media_group_id:
                    await asyncio.sleep(1)  # Wait for full group
                    # Forward ALL files in media group
                    for i in range(1, 4):  # Check 3 previous messages
                        try:
                            prev_msg = await client.get_messages(message.chat.id, message.message_id - i)
                            if prev_msg and prev_msg.media_group_id == message.media_group_id:
                                await prev_msg.forward(Config.TARGET_CHANNEL)
                        except:
                            pass
                    await message.forward(Config.TARGET_CHANNEL)
                    print("✅ COMPLETE Media group forwarded!")
            except Exception as e:
                print(f"Media error: {e}")
    # ================================================
    
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially."""
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
               
    async def main():
        await VJBot.start()
        bot_info = await VJBot.get_me()
        
        # ULTRA FAST MODE - Skip slow DB restart
        if FAST_MODE:
            print("⚡ ULTRA FAST MODE - Direct forwarding active!")
        else:
            await restart_forwards(VJBot)
            
        print(f"Bot Started! @{bot_info.username}")
        print("⚡ ULTRA FAST Forward Bot Live! 🚀")
        print(f"📤 Target Channel: {Config.TARGET_CHANNEL}")
        await idle()

    asyncio.get_event_loop().run_until_complete(main())

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
