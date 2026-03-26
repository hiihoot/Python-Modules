from typing import Any, List, Union, Optional, Dict
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Abstract base class for polymorphic data processing."""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Union[list, int, float]) -> bool:
        try:
            if isinstance(data, (int, float)):
                return True

            if isinstance(data, List):
                for x in data:
                    if not isinstance(x, (int, float)):
                        return False
                return True
            return False
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("no numeric data")
            if not isinstance(data, (int, float)):
                total = sum(data)
                count = len(data)
                avg = total / count
                core = (f"Processed {count} numeric values, "
                        f"sum={total}, avg={avg:.1f}")
            else:
                total = data
                count = 1
                avg = total / count
                core = (f"Processed {count} numeric values, "
                        f"sum={total}, avg={avg:.1f}")
            return self.format_output(core)
        except Exception as e:
            return self.format_output(f"Error: {e}")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            return isinstance(data, str)
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("not text data")
            core = (f"Processed text: {len(data)} characters, "
                    f"{len(data.split())} words")
            return self.format_output(core)
        except Exception as e:
            return self.format_output(f"Error: {e}")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: str) -> bool:
        try:
            if not isinstance(data, str) or ":" not in data:
                return False
            level = data.split(":", 1)[0].strip()
            return level in ("ERROR", "INFO")
        except Exception:
            return False

    def process(self, data: str) -> str:
        try:
            if not self.validate(data):
                raise ValueError("not a valid log")

            level, message = data.split(":")
            level = level.strip()
            message = message.strip()

            if level == "ERROR":
                prefix = "[ALERT]"
            else:
                prefix = f"[{level}]"

            core = f"{prefix} {level} level detected: {message}"
            return self.format_output(core)
        except Exception as e:
            return self.format_output(f"Error: {e}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    data: Dict = {
        "data_num": 1,
        "data_text": "Hello Nexus World",
        "data_log": "ERROR: Connection timeout"
    }

    data_num: List[Optional[int]] = data["data_num"]
    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {data_num}")
    if (num_proc.validate(data_num)):
        print("Validation: Numeric data verified")
    print("Output: " + num_proc.process(data_num))

    data_text: str = data["data_text"]
    print("\nInitializing Text Processor...")
    print(f'Processing data: "{data_text}"')
    if (text_proc.validate(data_text)):
        print("Validation: Text data verified")
    print("Output: " + text_proc.process(data_text))

    data_log: str = data["data_log"]
    print("\nInitializing Log Processor...")
    print(f'Processing data: "{data_log}"')
    if (log_proc.validate(data_log)):
        print("Validation: Log entry verified")
    print("Output: " + log_proc.process(data_log))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    data1: List[int] = [1, 2, 3]
    print("Result 1:", num_proc.process(data1))

    data2: str = "Hello World!"
    print("Result 2:", text_proc.process(data2))

    data3: str = "INFO: System ready"
    print("Result 3:", log_proc.process(data3))

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
