# log_config.py
import logging

logger = logging.getLogger("username")

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",    

)

# Create a file handler it shows in the terminal
# ch = logging.StreamHandler()
# ch.setFormatter(formatter)
# logger.addHandler(ch)

#this will show in the file
fh = logging.FileHandler("user_manager.log") #location of the log file
fh.setFormatter(formatter)#this will show in the file
logger.addHandler(fh)

'''
### 🔥 Basic Logging Levels with Emojis

| Level         | Emoji(s)                              | Vibe / Usage                                      |
|---------------|----------------------------------------|---------------------------------------------------|
| **DEBUG**     | 🐛 🔍 🧠 🛠️                          | For dev brain juice, deep dives, internal states  |
| **INFO**      | ℹ️ ✅ 📘 🧾 🪄                         | Regular updates, progress logs                    |
| **SUCCESS**   | ✅ 🎉 🟢 🚀 💯                         | Completed tasks, successful ops                   |
| **WARNING**   | ⚠️ 🟡 👀 🚧 🫣                         | Something sus, but not broken                     |
| **ERROR**     | ❌ 🔴 🛑 💥 🤬                         | Uh oh, something broke                            |
| **CRITICAL**  | 💣 🚨 🔥 😱 💀                        | System failure, fix this ASAP                     |

---

### 🧩 Extra Emojis for Specific Contexts

| Context                   | Emoji(s)                              |
|---------------------------|----------------------------------------|
| API Call                  | 🌐 📡 📲                              |
| Database                  | 🗄️ 💾 📦                              |
| Authentication/Login      | 🔐 🧑‍💻 🪪                            |
| File System               | 📁 📝 📂                              |
| Time/Delay                | ⏳ ⏰ 🕒                              |
| Start/Init                | 🟢 🚀 🛫                              |
| Shutdown/Exit             | 🔚 🛑 👋                              |
| Network/Proxy             | 🌍 🕸️ 🧱                             |
| Retry/Loop                | 🔁 ♻️ 🔄                             |

---

### 🔮 How to Use (Python Logging Example)

```python
from logger import logger

logging.info("ℹ️ App started")
logging.debug("🐛 Debugging connection issue...")
logging.warning("⚠️ Memory usage high")
logging.error("❌ Failed to connect to DB")
logging.critical("💀 System is down!")
```

'''
