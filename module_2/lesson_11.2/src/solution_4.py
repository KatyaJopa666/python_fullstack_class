def convert_units_with_while(metric_units: list[int], metric_type) -> None:
    FOOT: float = 3.28084 #foot_per_meter
    while len(metric_units) > 0:
        print(f'{metric_units[0]} meter(s) = {metric_units.pop(0) * FOOT} foot(feet)')


convert_units_with_while([1, 2], 'meters')