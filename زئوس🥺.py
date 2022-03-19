from requests import get
from re import findall
from rubika import Bot
import time

bot = Bot("ngxzxdschhwcvrpajcbtfmopexnoycng")
target = "g0B9Frl02439c68f9622b9dd0bc953f9"
bot.sendMessage(target, 'اپراتور مینی ربات فعال شد ✔️')
def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me","@","https://rubika.ir","https://rubika.ir/joing/","."," ir","#","https://","/","!"]
	for i in links:
		if i in msg:
			return True
	

# static variable
answered, sleeped, retries = [], False, {}

alerts, blacklist = [] , []

def alert(guid,user,link=False):
	alerts.append(guid)
	coun = int(alerts.count(guid))

	haslink = ""
	if link : haslink = "گزاشتن لینک در گروه ممنوع میباشد .\n\n"

	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (1/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (2/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")

	elif coun == 3:
		blacklist.append(guid)
		bot.sendMessage(target, "🚫 کاربر [ @"+user+" ] \n (3/3) اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid)
answered = [bot.getGroupAdmins]
retries = {}
sleeped = False
# delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص"]
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "/bot" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "The bot is now active", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیو"):
						
						try:
							response = get("https://api.codebazan.ir/bio").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("حذف") and msg.get("author_object_guid") in admins :
							try:
								number = int(msg.get("text").split(" ")[1])
								answered.reverse()
								bot.deleteMessages(target, answered[0:number])

								bot.sendMessage(target, "✅ "+ str(number) +" پیام اخیر با موفقیت حذف شد", message_id=msg.get("message_id"))
								answered.reverse()

							except IndexError:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "✅ پیام با موفقیت حذف شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("دانش"):
						
						try:
							response = get("https://api.codebazan.ir/danestani/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("الکی"):
						
						try:
							response = get("https://api.codebazan.ir/jok/alaki-masalan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("دانستنی"):
						
						try:
							response = get("https://api.codebazan.ir/dastan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ذکر"):
						
						try:
							response = get("http://api.codebazan.ir/zekr/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("خاطره"):
						
						try:
							response = get("http://api.codebazan.ir/jok/khatere").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور رابه طورصحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("پ ن پ"):
						
						try:
							response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					if  msg.get("text").startswith('!user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							
					elif msg.get("text") == "دستورات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "دستوارت زئوس🤖👽\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nبرای کاربران گرارمی👌\n1ـ 😁جوک \n2ـ😉فونت(فونت شاخ) \n3ـ😃دانستی \n4ـ💠 ماشین حاسب (حساب) \n5ـ🔮 بیوگرافی\n6ـ📿ذکر \n7ـ👨‍🎓سوال دانشی(دانشی) \n8ـ🤡 پ ن پ\n9ـ 😻 خاطره \n10ـ👻 الکی مثلا \n11ـ📃 ترجمه ( مترجم) \n12ـ💌 ارسال پیام به پیوی (پیام) \n13ـ👨‍👨‍👦‍👦 ادد ( افزودن کار بر با ایدی) \n14ـ📖 قوانین(قوانین گروه) \n15ـ⏰ تایم (ساعت) \n16ـ📆تاریخ \n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰\nتواجو🤵( داشتی باشد اگه ادمین نت نداشته باشن قابلیت در دست رس نیست🤦‍♂) \n➰➰➰➰➰➰➰➰➰➰➰➰➰➰➰➰\n👮‍♂برای ادمین ها👩‍💻\n1ـ🚫 اخطار(3)بشه ریم \n2ـ❎گپ بسته (گپ سته میشه) \n3ـ✅گپ باز(گپ باز میشه) \n4ـ❌ ریم (کار بر حذف میشه) \n5ـ📝 حذف(حذف پیام)باریپ رویه ان \n6ـ💬 ارام (گروه 10ثانیه میره رو حالت ارام) \n7ـ🗯 غیر فعال ارام (غیر فعال کردن حالت ارام) \n8ـ☣روشن (روشن کردن زئوس) \n9ـ📴 خاموش (خاموش کردن زئوس)\n➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿توجه😄(ربات داری قابلیت حذف فوش وحذف لینک میباشد پس لینک و فوش ندهید چت خوش😘❤️)", message_id=msg.get("message_id"))
							
					
						
					elif msg.get("text").startswith("صکص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیری"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بی ناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بی ناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کسکش"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیرم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادرتو"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادرت"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کون"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کونی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("جنده"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("جند"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادر جنده"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادر جند"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("ممه"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("kir"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("https://"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام تبلیغاتی پاک شد", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایید"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگایدم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایدی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگاید"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگایدیم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایدیم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیر"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					
						
					elif msg.get("text").startswith("کص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("لاشی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("دیوث"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("غیر فعال ارام") and msg.get("author_object_guid") in admins:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						
					elif msg.get("text").startswith("ارام") and msg.get("author_object_guid") in admins:
							try:
								number = 10
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
								
								
			

						
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																						

					if msg.get("text") == "/بات" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "ربات در حال اضر فعال است", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ادد") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر به گپ اضافه شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "کمک" and msg.get("author_object_guid") :
												bot.sendMessage(target, "دستوارت زئوس🤖👽\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nبرای کاربران گرارمی👌\n1ـ 😁جوک \n2ـ😉فونت(فونت شاخ) \n3ـ😃دانستی \n4ـ💠 ماشین حاسب (حساب) \n5ـ🔮 بیوگرافی\n6ـ📿ذکر \n7ـ👨‍🎓سوال دانشی(دانشی) \n8ـ🤡 پ ن پ\n9ـ 😻 خاطره \n10ـ👻 الکی مثلا \n11ـ📃 ترجمه ( مترجم) \n12ـ💌 ارسال پیام به پیوی (پیام) \n13ـ👨‍👨‍👦‍👦 ادد ( افزودن کار بر با ایدی) \n14ـ📖 قوانین(قوانین گروه) \n15ـ⏰ تایم (ساعت) \n16ـ📆تاریخ \n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰\nتواجو🤵( داشتی باشد اگه ادمین نت نداشته باشن قابلیت در دست رس نیست🤦‍♂) \n➰➰➰➰➰➰➰➰➰➰➰➰➰➰➰➰\n👮‍♂برای ادمین ها👩‍💻\n1ـ🚫 اخطار(3)بشه ریم \n2ـ❎گپ بسته (گپ سته میشه) \n3ـ✅گپ باز(گپ باز میشه) \n4ـ❌ ریم (کار بر حذف میشه) \n5ـ📝 حذف(حذف پیام)باریپ رویه ان \n6ـ💬 ارام (گروه 10ثانیه میره رو حالت ارام) \n7ـ🗯 غیر فعال ارام (غیر فعال کردن حالت ارام) \n8ـ☣روشن (روشن کردن زئوس) \n9ـ📴 خاموش (خاموش کردن زئوس)\n➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿توجه😄(ربات داری قابلیت حذف فوش وحذف لینک میباشد پس لینک و فوش ندهید چت خوش😘❤️)", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("حساب"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("پیام ") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "سلام عزیز", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "لیست" and msg.get("author_object_guid") :
												bot.sendMessage(target, "🥇سالار @salar_____m_____sepshy \n 🥈محمد @x_XasggX_x \n 🥉حسین @Hossein1384mo \n 🏅امیر @XIDAMIR \n 🏅افشین @afshinkhalaji \n 🏅دارک بوی @DarkBoy \n ربات 🤖 n\ @Zeus_Bot", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "خوبید" and msg.get("author_object_guid") :
												bot.sendMessage(target, "مرسی ماخوبیم توخوبی", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "سلاپ" and msg.get("author_object_guid") :
												bot.sendMessage(target, "سلاپ داپ🗿", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "نخوندم" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  چون سواد نداری 😜 ", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "عه" and msg.get("author_object_guid") :
												bot.sendMessage(target, "اره", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "نوب" and msg.get("author_object_guid") :
												bot.sendMessage(target, "پلیر", message_id=msg.get("message_id"))							
																		
					elif msg.get("text") == "خوبین" and msg.get("author_object_guid") :
												bot.sendMessage(target, "عالی😜", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "مهدی":
						bot.sendMessage(target, "عشقمه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مهدی":
						bot.sendMessage(target, "عزیزمه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هستی":
						bot.sendMessage(target, "شاخه گپ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "زهرا":
						bot.sendMessage(target, "نوب گپ", message_id=msg.get("message_id"))
						
						
					elif msg.get("text") == "ممد":
						bot.sendMessage(target, "جذاب گپ", message_id=msg.get("message_id"))
						
						
					elif msg.get("text") == "مدی":
						bot.sendMessage(target, "مدیر گپ", message_id=msg.get("message_id"))
						
						
					elif msg.get("text") == "رباط":
						bot.sendMessage(target, "جونم😁", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "باط":
						bot.sendMessage(target, "درست صدام کن (◔‿◔) ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مهدی":
						bot.sendMessage(target, "عشق من در قلب من😍😜", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ممنون":
						bot.sendMessage(target, "عزیزی", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "میتی" and msg.get("author_object_guid") :
												bot.sendMessage(target, "عشق گپ🤤💜", message_id=msg.get("message_id"))	
						
					elif msg.get("text") == "نازی" and msg.get("author_object_guid") :
												bot.sendMessage(target, "خشگل گپ♥😍", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "خبی":
						bot.sendMessage(target, "مرسی تو خبی🙃", message_id=msg.get("message_id"))																			
					if  msg.get("text").startswith('!user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							

					elif msg.get("text") == "خاموش" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "ربات خاموش شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("پینگ"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("اخطار") and msg.get("author_object_guid") in admins:
							try:
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									alert(guid,user)
									
								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
									
							except IndexError:
								guid = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								if not guid in admins:
									alert(guid,user)
								else:
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "قوانین":
							rules = open("rules.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("آپدیت قوانین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("rules.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت قوانین")))
								bot.sendMessage(target, "✅  قوانین بروزرسانی شد", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
						
							
					elif msg.get("text") == "لینک" and msg.get("author_object_guid") :
												bot.sendMessage(target, "بفرما😍 https://rubika.ir/joing/BFFAFFJH0DQCUGZEHAHYVROMZJYJFZGU", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ترجمه"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("فونت"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
												bot.sendMessage(target, "خوبم توخوفی", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "مرسی" and msg.get("author_object_guid") :
												bot.sendMessage(target, "بهش برسی🙂", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "صلام" and msg.get("author_object_guid") :
												bot.sendMessage(target, "صلام گل🥺🌹", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "اصل" and msg.get("author_object_guid") :
												bot.sendMessage(target, "ℤ𝕖𝕦𝕤𝔹𝕠𝕥 ¦ زئوس‌بات هستم (0)ساله درقلبت🌹😜♥", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
												bot.sendMessage(target, "چیه پوکرمیدی🤨", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "😐💔" and msg.get("author_object_guid") :
												bot.sendMessage(target, "💔😐", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "💔" and msg.get("author_object_guid") :
												bot.sendMessage(target, "😶", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "😂" and msg.get("author_object_guid") :
												bot.sendMessage(target, "نخند مسواک گرون میشه😐", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "😂😂" and msg.get("author_object_guid") :
												bot.sendMessage(target, "جون توفقط بخند", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "😂😂😂" and msg.get("author_object_guid") :
												bot.sendMessage(target, "یکی اینو بگیره مرد از خنده", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "زئوس" and msg.get("author_object_guid") :
												bot.sendMessage(target, "جانا🙃", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "چخبر" and msg.get("author_object_guid") :
												bot.sendMessage(target, "سلامتیت♥", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "فدات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "نشی🤗", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "قربونت" and msg.get("author_object_guid") :
												bot.sendMessage(target, "♥🌹", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "بای":
						bot.sendMessage(target, "بای بای🖖🖖", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "خداحافظ":
						bot.sendMessage(target, "خداحافظ گل🌹🥺", message_id=msg.get("message_id"))	
						
					elif msg.get("text") == "س":
						bot.sendMessage(target, "س🗿", message_id=msg.get("message_id"))											
																			
												
																			
												
																							
												
				 
												
																																					
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "جانم😜", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "بات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "نمی تونی درست صدام کنی🗿🚬", message_id=msg.get("message_id"))
												
												
																									



					elif msg.get("text").startswith("جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text") == "تایم":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "تاریخ":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "حذف" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))

					# elif msg.get("text").split(" ")[0] in  delmess:
					# 	bot.deleteMessages(target, [msg.get("message_id")])
					# 	bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))


					elif msg.get("text") == "گپ بسته" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ بسته شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "گپ باز" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ریم") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"✅ کاربر حذف شد", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"❎ کاربر حذف نشد", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"کاربر حذف نشد ❌", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر حذف شد ✅", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "روشن" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "ربات فعال شد ✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"اگه قوانین رو رعایت میکردی حذف نمیشدی !", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user} به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"بسلامت {user} 🗑️", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user}  به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅                                               برای اطلاعات بیشتر از کلمه(قوانین)استفاده کنید😊", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
