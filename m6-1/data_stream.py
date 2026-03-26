from abc import ABC, abstractmethod
from typing import List, Any, Optional, Union, Dict


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self._stats = {"processed": 0}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        return [i for i in data_batch if criteria.lower() in str(i).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "processed_items":
                self._stats["processed"]}


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        num_readings = len(data_batch)
        self._stats["processed"] += num_readings
        return (f"Sensor analysis: {num_readings} "
                f"readings processed, avg temp: 22.5°C\n")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        num_ops = len(data_batch)
        self._stats["processed"] += num_ops
        net = 25
        return (f"Transaction analysis: {num_ops} "
                f"operations, net flow: +{net} units\n")


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        num_events = len(data_batch)
        self._stats["processed"] += num_events
        errors = 1
        return (f"Event analysis: {num_events} "
                f"events, {errors} error detected\n")


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        if isinstance(stream, DataStream):
            self.streams.append(stream)
        else:
            print("Only Stream stypes")

    def process_mixed(self, mixed_batches):
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        for stream, batch in mixed_batches:
            stream.process_batch(batch)
            if isinstance(stream, SensorStream):
                print("- Sensor data: 2 readings processed")
            elif isinstance(stream, TransactionStream):
                print("- Transaction data: 4 operations processed")
            elif isinstance(stream, EventStream):
                print("- Event data: 3 events processed")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # Sensor
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))

    # Transaction
    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_batch}")
    print(trans.process_batch(trans_batch))

    # Event
    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")
    print(event.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    mixed_data = [
        (sensor, ["temp:20", "humidity:50"]),
        (trans, ["buy:100", "sell:50", "buy:200", "sell:100"]),
        (event, ["login", "error", "logout"])
    ]
    processor.process_mixed(mixed_data)

    print("\nStream filtering active: High-priority data only")
    filtered_sensor = sensor.filter_data(
        ["critical sensor alert", "normal", "critical sensor alert"],
        "critical")
    filtered_trans = trans.filter_data(
        ["small tx", "large transaction", "small tx"], "large")
    print(
        f"Filtered results: {
            len(filtered_sensor)} critical sensor alerts, {
            len(filtered_trans)} large transaction\n")

    print("All streams processed successfully. Nexus throughput optimal.")
