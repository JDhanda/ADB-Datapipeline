from datapipeline.processing import transform_record, aggregate_records


def test_transform_record_with_value():
    record = {"id": "1", "value": 10}
    result = transform_record(record)

    assert result["id"] == "1"
    assert result["value"] == 11.0
    assert result["status"] == "valid"


def test_transform_record_missing_value():
    record = {"id": "2"}
    result = transform_record(record)

    assert result["value"] == 0.0
    assert result["status"] == "invalid"


def test_aggregate_records():
    records = [{"value": 10}, {"value": 20}, {"value": 30}]
    summary = aggregate_records(records)

    assert summary["count"] == 3
    assert summary["total_value"] == 60
    assert summary["average_value"] == 20
