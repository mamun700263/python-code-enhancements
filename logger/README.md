
# 🔥 `Logger` System – Elite Log Manager for Python Apps

## 📦 Overview

This module defines a **custom, flexible logging system** for production-grade Python applications. It supports:

* 📂 **Rotating file logs**
* 🖥️ **Console output (optional)**
* 🧾 **Text or JSON format**
* 🔎 **Log filtering by time, level, and module**
* 🧠 **Log parsing for analytics and auditing**

---

## 🧱 Directory Structure

```
project/
├── logs/
│   └── scraper.log
├── logger.py
└── logger.md   <-- (this file)
```

Logs are saved inside the `logs/` directory with **rotation and backups**.

---

## ⚙️ Core Components

### 🔧 `Logger.get_logger()`

```python
Logger.get_logger(
    name: str = "default",
    file_name: Optional[str] = None,
    to_console: bool = False,
    format: str = "text"  # or "json"
)
```

#### ✅ Parameters:

| Name         | Type   | Description                              |
| ------------ | ------ | ---------------------------------------- |
| `name`       | `str`  | Logger name (and log level tag).         |
| `file_name`  | `str`  | Filename (optional, defaults to `name`). |
| `to_console` | `bool` | Also log to terminal if `True`.          |
| `format`     | `str`  | `"text"` or `"json"` log format.         |

#### 🪵 Example:

```python
log = Logger.get_logger("scraper", format="json", to_console=True)
log.info("Scraping started")
log.warning("Rate limit triggered", extra={"ip": "127.0.0.1"})
```

---

### 📄 Log Output Formats

#### Text:

```
[2025-06-15 07:30:45] [INFO] [scraper] Scraping started
```

#### JSON:

```json
{
  "timestamp": "2025-06-15T07:30:45.123456",
  "level": "INFO",
  "name": "scraper",
  "message": "Scraping started"
}
```

Supports `extra={...}` for structured logging:

```python
log.info("Login", extra={"user_id": 42, "device": "mobile"})
```

---

## 🔍 `Logger.filter_logs(...)`

```python
Logger.filter_logs(
    file_path: str,
    start_time: str,
    end_time: str,
    level: Optional[str] = None,
    name: Optional[str] = None,
    limit: Optional[int] = None
) -> List[str]
```

### 🎯 Filters:

* Time range (`start_time`, `end_time`)
* Log level (`INFO`, `ERROR`, etc.)
* Logger name/module (`scraper`, `auth`, etc.)
* Optional limit

#### ⏱️ Time Format

Accepts:

* `YYYY-MM-DD`
* `YYYY-MM-DD HH:MM:SS`

#### 📌 Example:

```python
lines = Logger.filter_logs(
    file_path="logs/scraper.log",
    start_time="2025-06-14 00:00:00",
    end_time="2025-06-15 23:59:59",
    level="WARNING",
    name="scraper",
    limit=10
)
```

---

## 🧪 `Logger.parse_log_line(...)`

Parses a single log line and extracts the timestamp.

```python
timestamp, line = Logger.parse_log_line("[2025-06-15 07:30:45] [INFO] [scraper] OK")
```

---

## 🧬 `Logger.parse_to_datetime(...)`

Utility for parsing dates flexibly:

```python
dt = Logger.parse_to_datetime("2025-06-15")
# Returns datetime(2025, 6, 15, 0, 0, 0)
```

---

## 🧾 `JSONFormatter`

Custom formatter to convert logs into structured JSON:

```python
class JSONFormatter(logging.Formatter):
    def format(self, record):
        ...
```

Supports all custom metadata from `.info(..., extra={...})`.

---

## 🛡️ Log Rotation

Uses `RotatingFileHandler`:

* Max size: 5 MB
* Backups: 3 files

When exceeded:

* `scraper.log`
* `scraper.log.1`
* `scraper.log.2`
* `scraper.log.3`

---

## ✅ Best Practices

| ✅ Do                                         | ❌ Don’t                  |
| -------------------------------------------- | ------------------------ |
| Use one logger per module                    | Share a global logger    |
| Use structured logs (JSON) for scrapers/APIs | Parse plaintext manually |
| Use `extra={}` for metadata                  | Encode data in messages  |
| Rotate logs to avoid file bloat              | Let logs grow forever    |

---

## 🔥 Sample Use Case

```python
log = Logger.get_logger("api", format="json", to_console=True)

log.info("User created", extra={"user_id": 101, "role": "admin"})
log.error("Payment failed", extra={"order_id": 443, "retry": False})

filtered = Logger.filter_logs(
    file_path="logs/api.log",
    start_time="2025-06-10",
    end_time="2025-06-15",
    level="ERROR",
    name="api"
)
for line in filtered:
    print(line)
```

---

## 🧠 Designed For:

* 🔌 **Backend services**
* 🤖 **Scrapers**
* 🌐 **APIs**
* 📊 **Log analysis pipelines**
* 🔐 **Audit trails**

---
