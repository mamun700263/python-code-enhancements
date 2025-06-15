from logger import Logger
from datetime import datetime

# === STEP 1: Create a JSON logger (file + console) ===
json_logger = Logger.get_logger(
    name="scraper_json",
    format="json",
    to_console=True
)

# Log structured JSON events
for i in range(3):
    json_logger.info("Page fetched", extra={"page": i + 1, "status": "success"})

json_logger.warning("Captcha detected", extra={"url": "http://target.com", "type": "recaptcha"})

# === STEP 2: Create a TEXT logger (file only) ===
text_logger = Logger.get_logger(
    name="scraper_text",
    format="text",
    to_console=False
)

# Log plain text events
for i in range(3):
    text_logger.info(f"Retry attempt {i + 1}")

text_logger.error("Scraping failed", extra={"error_code": 429})


# === STEP 3: FILTER LOGS USING DATETIME STRINGS ===

now = datetime.now()
start_time = now.replace(minute=0, second=0, microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
end_time = now.strftime("%Y-%m-%d %H:%M:%S")

print("\n🔍 Filtered JSON logs (WARNING+):")
filtered_json_logs = Logger.filter_logs(
    file_path="logs/scraper_json.log",
    start_time=start_time,
    end_time=end_time,
    level="WARNING",
    name="scraper_json",
    limit=10
)
for line in filtered_json_logs:
    print(line)


print("\n📄 Filtered TEXT logs:")
filtered_text_logs = Logger.filter_logs(
    file_path="logs/scraper_text.log",
    start_time=start_time,
    end_time=end_time,
    limit=5
)
for line in filtered_text_logs:
    print(line)


# === STEP 4: TEST HELPER FUNCTIONS ===

print("\n🕒 Last 30 minutes JSON logs:")
last_30_json = Logger.last_n_minutes_logs(
    file_path="logs/scraper_json.log",
    n=30
)
for line in last_30_json:
    print(line)

print("\n🕒 Last 1 hour TEXT logs:")
last_1hr_text = Logger.last_n_hours_logs(
    file_path="logs/scraper_text.log",
    n=1
)
for line in last_1hr_text:
    print(line)

print("\n🗓️ Last 1 day JSON logs:")
last_1day_json = Logger.last_n_days_logs(
    file_path="logs/scraper_json.log",
    n=1
)
for line in last_1day_json:
    print(line)
