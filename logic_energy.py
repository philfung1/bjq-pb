def generate_positive_energy_checklist(project_type, frameworks, location, floor_area, orientation):
    checklist = []

    # Core Positive Energy Recommendations
    checklist.append("Design for energy efficiency first: passive strategies, high-performance envelope")
    checklist.append("Use all-electric systems to reduce operational carbon")
    checklist.append("Include energy monitoring systems with user-friendly displays")
    checklist.append("Optimize solar access and shading based on orientation")

    # Framework-specific enhancements
    if "LEED" in frameworks:
        checklist.append("Model predicted energy use and demonstrate energy cost savings over baseline")
        checklist.append("Commission HVAC and lighting systems to ensure performance")

    if "WELL" in frameworks:
        checklist.append("Ensure lighting systems support circadian rhythm and comfort")
        checklist.append("Include emergency backup power for life safety systems")

    if "Passive House" in frameworks:
        checklist.append("Meet or exceed Passive House performance targets for heating/cooling demand")
        checklist.append("Eliminate thermal bridges and ensure airtightness")

    if "LBC" in frameworks:
        checklist.append("Use renewable energy for 100% of operational needs")
        checklist.append("Track net positive energy performance over a 12-month period")

    if "Positive Building" in frameworks:
        checklist.append("Incorporate solar PV sized for site potential and seasonal balance")
        checklist.append("Use battery storage or grid feedback systems to support resilience")
        checklist.append("Design for passive survivability during power outages")

    # Size-based guidance
    if floor_area > 10000:
        checklist.append("Implement zoned mechanical systems with smart controls for large spaces")

    # Orientation-specific
    if orientation == "South":
        checklist.append("Maximize south-facing roof area for solar PV or solar thermal collection")
    elif orientation == "West":
        checklist.append("Include shading devices or thermal mass to buffer afternoon heat gain")

    return checklist

def get_energy_equipment_recommendations():
    return [
        "All-electric HVAC system (cold climate air-source heat pump or ground-source system)",
        "Induction cooktop with high-efficiency electric oven",
        "Energy monitoring system with real-time feedback and smart metering",
        "Solar PV system (roof or ground-mounted) sized to meet annual site demand",
        "Battery storage (e.g., lithium-ion) or vehicle-to-home energy integration",
        "Electric water heater with heat pump or solar thermal backup"
    ]