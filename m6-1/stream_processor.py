from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Abstract base class for polymorphic data processing."""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Default implementation (can be overridden)."""
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, list):
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

            total = sum(data)
            count = len(data)
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

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str) or ":" not in data:
                return False
            level = data.split(":", 1)[0].strip()
            return level in ("ERROR", "INFO")
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("not a valid log")

            level, message = data.split(":", 1)
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

    # Numeric
    data_num: List[int] = [1, 2, 3, 4, 5]
    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {data_num}")
    if (num_proc.validate(data_num)):
        print("Validation: Numeric data verified")
    print("Output: " + num_proc.process(data_num))

    # Text
    data_text: str = "Hello Nexus World"
    print("\nInitializing Text Processor...")
    print(f'Processing data: "{data_text}"')
    if (text_proc.validate(data_text)):
        print("Validation: Text data verified")
    print("Output: " + text_proc.process(data_text))

    # Log
    data_log: str = "ERROR: Connection timeout"
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
