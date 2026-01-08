

SELECT 
    p.state,
    p.gender,
    COUNT(DISTINCT p.id) AS count_high_risk_patients,
    AVG(p.age) AS average_age,
    AVG(v.blood_pressure) AS average_blood_pressure,
    AVG(v.cholesterol) AS average_cholesterol
FROM 
    patients p
INNER JOIN 
    diagnoses d ON p.id = d.patient_id AND d.diagnosis = 'heart attack'
INNER JOIN 
    vitals v ON p.id = v.patient_id AND v.blood_pressure >= 140 AND v.cholesterol > 200
INNER JOIN 
    wearable w ON p.id = w.patient_id AND w.slope = 2
WHERE 
    p.age > 45
    AND EXISTS (SELECT 1 FROM xrays x WHERE x.patient_id = p.id)
    AND EXISTS (SELECT 1 FROM symptoms s WHERE s.patient_id = p.id)
GROUP BY 
    p.state, p.gender
ORDER BY 
    p.state, p.gender;