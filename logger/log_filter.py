import datetime
from typing import List

def parse_log_line(line: str):
    """Extract timestamp and return parsed line info, or None if invalid."""
    if not line.startswith('['):
        return None, None
    
    try:
        date_str = line.split('] [')[0][1:]  # Extract 'YYYY-MM-DD HH:MM:SS'
        log_time = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return log_time, line.strip()
    except Exception:
        return None, None


def filter_logs(
    file_path: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    level: str = None,
    page: str = None
) -> List[str]:
    """Filter log lines by time range, level, and page/module name."""
    results = []

    level_tag = f"[{level.upper()}]" if level else None
    page_tag = f"[{page.lower()}]" if page else None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            log_time, clean_line = parse_log_line(line)
            if not log_time:
                continue
            if not (start_time <= log_time <= end_time):
                continue
            if level_tag and level_tag not in clean_line.upper():
                continue
            if page_tag and page_tag not in clean_line.lower():
                continue
            results.append(clean_line)

    return results



# # ==================== USAGE ==================== #

# if __name__ == "__main__":
#     start = datetime.datetime(2025, 5, 5,0,0,0)
#     till = datetime.datetime(2025, 5, 8,12,0,0)
#     # level = 'warning'
#     # page = 'main'

#     logs = filter_logs('logs/user_manager.log', start, till)

#     for log in logs:
#         print(log)
