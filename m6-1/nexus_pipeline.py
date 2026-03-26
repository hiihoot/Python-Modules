from abc import ABC, abstractmethod
from typing import Any, Protocol, List, Union

# Duck-typing interface for stages (no ABC needed here)
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...

# Concrete stages – standalone classes
class InputStage:
    def process(self, data: Any) -> Any:
        # minimal real logic (or fake for demo)
        return {"input_processed": data}

class TransformStage:
    def process(self, data: Any) -> Any:
        return {"transformed": data, "enriched": "yes"}

class OutputStage:
    def process(self, data: Any) -> Any:
        return f"Final output: {data}"

# Abstract base – common pipeline behavior
class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = [
            InputStage(),
            TransformStage(),
            OutputStage()
        ]
        self.stats: Dict[str, int] = {"processed": 0}

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Subclasses MUST implement this – defines how data flows through stages."""
        pass  # ← NO code here! Only pass or raise NotImplementedError

    # Common helper method (NOT abstract)
    def _run_stages(self, data: Any) -> Any:
        current = data
        for stage in self.stages:
            current = stage.process(current)
        self.stats["processed"] += 1
        return current

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)


# Concrete adapters – they inherit & MUST override process()
class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        # This is where the real (or demo) work happens
        try:
            print(f"Input: {data}")
            result = self._run_stages(data)
            print("Transform: Enriched with metadata and validation")
            output = "Processed temperature reading: 23.5°C (Normal range)"
            print(f"Output: {output}")
            return output
        except Exception as e:
            print(f"Error in JSON processing: {e}")
            return None  # or raise, depending on recovery needs


# Same pattern for the others
class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: {data}")
        result = self._run_stages(data)
        print("Transform: Parsed and structured data")
        output = "User activity logged: 1 actions processed"
        print(f"Output: {output}")
        return output


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: {data}")
        result = self._run_stages(data)
        print("Transform: Aggregated and filtered")
        output = "Stream summary: 5 readings, avg: 22.1°C"
        print(f"Output: {output}")
        return output