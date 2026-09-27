import discord
import sys
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ⚠️ ضع الـ ID الخاص بك هنا (أرقام فقط)
ADMIN_ID = 1491495718509215774  

# عناوين إخبارية متنوعة لبقية الأعضاء
NEWS_HEADLINES = [
    "وصول رفيع المستوى للروم الصوتي الآن!",
    "رصد تحركات جديدة في القنوات الصوتية!",
    "انضمام عضو جديد إلى المحادثة المباشرة!",
    "ارتفاع وتيرة النشاط في السيرفر!"
]

@bot.event
async def on_ready():
    print(f'----------------------------------------')
    print(f'تم تشغيل القناة الإخبارية باللغة العربية!')
    print(f'الحساب: {bot.user}')
    print(f'----------------------------------------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="الأخبار العاجلة 🔴"))

@bot.event
async def on_voice_state_update(member, before, after):
    # تجاهل البوتات
    if member.bot:
        return

    text_channel = member.guild.system_channel or member.guild.text_channels[0]
    if not text_channel:
        return

    # 1. عند دخول الروم الصوتي
    if before.channel is None and after.channel is not None:
        # إشعار خاص وخاص جداً بالأدمن
        if member.id == ADMIN_ID:
            embed = discord.Embed(
                title="🚨 **تغطية خاصة | دخول الأدمن** 🚨",
                description=(
                    f"👑 **تنبيه هام:** انضم الأدمن {member.mention} إلى الروم الصوتي **{after.channel.name}** الآن!\n\n"
                    f"🎙️ **الحالة:** الأدمن متواجد حالياً ومتاح للحديث."
                ),
                color=discord.Color.gold()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text="نظام رصد الإدارة | بث مباشر 🔴")
            await text_channel.send(embed=embed)

        # باقي الأعضاء
        else:
            headline = random.choice(NEWS_HEADLINES)
            embed = discord.Embed(
                title="🚨 **تغطية خاصة | خبر عاجل** 🚨",
                description=(
                    f"📺 **موجز الأنباء:** {headline}\n\n"
                    f"👤 **العضو:** {member.mention}\n"
                    f"🎙️ **المقر الحالي:** `{after.channel.name}`"
                ),
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text="مركز الأخبار العاجلة | بث مباشر 🔴")
            await text_channel.send(embed=embed)

    # 2. عند الخروج من الروم الصوتي
    elif before.channel is not None and after.channel is None:
        if member.id == ADMIN_ID:
            embed = discord.Embed(
                title="📢 **تحديث إخباري | مغادرة الأدمن**",
                description=f"انتهت التغطية المباشرة للادمن {member.mention} بعد خروجه من الروم الصوتي `{before.channel.name}`.",
                color=discord.Color.dark_gray()
            )
            embed.set_footer(text="نظام رصد الإدارة | ختام الموجز ⚪")
            await text_channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="📢 **تحديث إخباري | مغادرة**",
                description=f"انتهت التغطية المباشرة لـ {member.mention} بعد خروجه من الروم الصوتي `{before.channel.name}`.",
                color=discord.Color.dark_gray()
            )
            embed.set_footer(text="نشرة الأخبار | ختام الموجز ⚪")
            await text_channel.send(embed=embed)

bot.run('MTU1MzY4NjgzNDYzNzQ0MzA4Mg.GANux8.JL84lxwyHlbrsl2lyVIwOnvRdzb72Qoo-lOBzk')