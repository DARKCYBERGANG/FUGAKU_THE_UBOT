# FUGAKU-THE-USERBOT

<p align="center">
<img src="https://telegra.ph/file/def827c7ae3b3b17e68bd.jpg" alt="FUGAKU THE  USERBOT">


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



Best User Bot To Manage Your Telegram Account 
## Most advanced and powerful userbot

## by Team DARKCYBER

### For any query or want to know how it works join Group And Channel 

<a href="https://t.me/Fugaku_Userbot_Official"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-blue.svg?logo=Telegram"></a>
<a href="https://t.me/Fugaku_Support_Group"><img src="https://img.shields.io/badge/Join-Telegram%20Group-red.svg?logo=telegram"></a>


### Host FUGAKU  In Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DARKCYBERGANG/FUGAKU_THE_UBOT)

## Telegram-String

[![Run on Repl.it](https://repl.it/badge/github/STARKGANG/friday)](https://Fugakuuserbot.cyb3rm4f1a.repl.run)


### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/DARKCYBER/FUGAKU_THE_UBOT
cd FUGAKU_THE_UBOT
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```


### UniBorg Configuration


The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

