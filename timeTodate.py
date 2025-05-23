import datetime

def timestamp_to_datetime(timestamp_str):
    """支持秒/毫秒/微秒/纳秒级时间戳转换"""
    try:
        ts = float(timestamp_str.strip())
        length = len(timestamp_str.strip().split('.')[0])  # 整数部分位数

        # 根据位数调整时间戳单位
        if length <= 10:  # 秒级（10位）
            dt = datetime.datetime.fromtimestamp(ts)
        elif length <= 13:  # 毫秒级（13位）
            dt = datetime.datetime.fromtimestamp(ts / 1000)
        elif length <= 16:  # 微秒级（16位）
            dt = datetime.datetime.fromtimestamp(ts / 1_000_000)
        else:  # 纳秒级（19位）或其他
            dt = datetime.datetime.fromtimestamp(ts / 1_000_000_000)

        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return f"无效的时间戳: {timestamp_str}"

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    print(timestamp_to_datetime(line))
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 不存在")

if __name__ == "__main__":
    input_file = "time.txt"
    print(f"转换结果（{input_file}）:")
    process_file(input_file)