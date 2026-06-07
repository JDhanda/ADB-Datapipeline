from typing import List, Dict


def transform_record(record: Dict[str, object]) -> Dict[str, object]:
    """Apply basic transformation rules to a record."""
    original_value = record.get("value")
    transformed = {
        "id": record.get("id"),
        "value": (
            float(original_value) * 1.1
            if original_value is not None
            else 0.0
        ),
        "status": "valid" if original_value is not None else "invalid",
    }
    return transformed


def aggregate_records(records: List[Dict[str, object]]) -> Dict[str, object]:
    """Aggregate transformed records into summary counts."""
    total = sum(r.get("value", 0) for r in records)
    return {
        "count": len(records),
        "total_value": total,
        "average_value": total / len(records) if records else 0,
    }
