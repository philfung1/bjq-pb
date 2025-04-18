def generate_positive_air_checklist(project_type, frameworks, location, floor_area, orientation):
    checklist = []

    # Core Recommendations
    checklist.append("Ensure outdoor air ventilation meets ASHRAE 62.1/62.2 standards")
    checklist.append("Use MERV 13 or higher filtration on all mechanical ventilation systems")
    checklist.append("Avoid combustion-based appliances (e.g., gas stoves, gas furnaces)")
    checklist.append("Include operable windows for natural ventilation where feasible")
    checklist.append("Use low-VOC or zero-VOC materials")

    # Framework-Specific Enhancements
    if "WELL" in frameworks:
        checklist.append("Install indoor air quality monitors (PM2.5, CO2) in living/work areas")
        checklist.append("Conduct post-occupancy air quality testing")
        checklist.append("Specify WELL-compliant adhesives, sealants, and finishes")

    if "Passive House" in frameworks:
        checklist.append("Install heat recovery ventilation (HRV) or energy recovery ventilation (ERV)")
        checklist.append("Ensure airtight construction with verified blower door testing")

    if "LEED" in frameworks:
        checklist.append("Use construction air quality management plans during building process")
        checklist.append("Provide separate exhaust systems for high-moisture and pollutant-generating areas")

    if "LBC" in frameworks:
        checklist.append("Use materials listed in the Declare program or Red List Free")
        checklist.append("Avoid any materials with known harmful off-gassing or toxic content")

    if "Positive Building" in frameworks:
        checklist.append("Integrate biophilic ventilation strategies to support mental wellness")
        checklist.append("Use air quality indicators that are visible and accessible to occupants")
        checklist.append("Choose filtration and ventilation systems that enhance both indoor and planetary health")

    # Location-based logic
    if location.lower() == "toronto":
        checklist.append("Account for urban air quality: consider MERV 16 or activated carbon filters")

    # Size-based logic
    if floor_area > 10000:
        checklist.append("Use zoned ventilation or multiple HRVs to manage airflow in large homes")

    # Orientation-based logic
    if orientation == "South":
        checklist.append("Leverage south-facing windows for thermal buoyancy and natural airflow")
    elif orientation == "North":
        checklist.append("Minimize ventilation-related heat loss through north-facing exposures")

    return checklist

def get_air_equipment_recommendations():
    return [
        "ERV or HRV unit with MERV 13+ filtration",
        "High-efficiency ducted or ductless electric heat pump (no combustion)",
        "CO₂ and PM2.5 air quality monitors in key living/work areas",
        "Operable windows with screens and optional smart sensors",
        "Low-VOC materials verified through Declare, GreenGuard, or equivalent"
    ]