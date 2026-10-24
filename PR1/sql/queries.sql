SELECT id, address, object_type, area
FROM accounting_objects
ORDER BY address;

SELECT 
    m.id,
    m.meter_type,
    m.serial_number,
    o.address
FROM meters m
JOIN accounting_objects o ON m.object_id = o.id
ORDER BY o.address;

SELECT id, period, value, reading_date
FROM readings
WHERE meter_id = ?
ORDER BY period DESC;

SELECT 
    o.id,
    o.address,
    COUNT(m.id) AS meters_count
FROM accounting_objects o
LEFT JOIN meters m ON o.id = m.object_id
GROUP BY o.id, o.address
ORDER BY meters_count DESC;

SELECT 
    r.id,
    m.meter_type,
    o.address,
    r.period,
    r.value
FROM readings r
JOIN meters m ON r.meter_id = m.id
JOIN accounting_objects o ON m.object_id = o.id
ORDER BY r.reading_date DESC
LIMIT 10;

SELECT id, address, object_type, area
FROM accounting_objects
WHERE id = ?;

SELECT 
    m.id, m.meter_type, m.serial_number, o.address
FROM meters m
JOIN accounting_objects o ON m.object_id = o.id
WHERE m.id = ?;

SELECT 
    r.id, r.period, r.value, r.reading_date,
    m.meter_type, o.address
FROM readings r
JOIN meters m ON r.meter_id = m.id
JOIN accounting_objects o ON m.object_id = o.id
WHERE r.id = ?;

SELECT id, meter_type, serial_number
FROM meters
WHERE meter_type = ?
ORDER BY id;

SELECT 
    r.id, r.value, m.meter_type, o.address
FROM readings r
JOIN meters m ON r.meter_id = m.id
JOIN accounting_objects o ON m.object_id = o.id
WHERE r.period = ?
ORDER BY o.address;