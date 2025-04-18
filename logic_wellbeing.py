def generate_positive_wellbeing_checklist(project_type, frameworks, location, floor_area, orientation):
    checklist = []

    # Core Positive Mental Well-being Recommendations
    checklist.append("Design for natural light access and circadian-friendly lighting systems")
    checklist.append("Incorporate indoor nature, views to outdoors, or biophilic design elements")
    checklist.append("Create quiet, calm zones for retreat, prayer, reading, or reflection")
    checklist.append("Ensure spaces support privacy, dignity, and positive social interaction")

    # Framework-specific logic
    if "WELL" in frameworks:
        checklist.append("Provide acoustic comfort and noise reduction through materials and layout")
        checklist.append("Control glare and visual comfort with shading and diffuse light sources")
        checklist.append("Support mental health awareness through education or policy design")

    if "LEED" in frameworks:
        checklist.append("Optimize daylighting levels in regularly occupied spaces")
        checklist.append("Consider views to nature and interior connectivity")

    if "LBC" in frameworks:
        checklist.append("Use natural materials and design cues to support psychological restoration")
        checklist.append("Avoid sensory overload with simplified, peaceful environments")

    if "Positive Building" in frameworks:
        checklist.append("Support mental and spiritual resilience through design of restorative spaces")
        checklist.append("Embed purpose, beauty, and connection into everyday experiences")
        checklist.append("Design for joy, gratitude, and meaning—not just efficiency")

    # Location or orientation-based logic
    if orientation == "East":
        checklist.append("Position bedrooms or reflective spaces for morning light exposure")

    return checklist

def get_wellbeing_equipment_recommendations():
    return [
        "Circadian lighting system with tunable white or full-spectrum LEDs",
        "Sound masking system or acoustic panels for noise reduction",
        "Smart window controls or motorized blinds for daylight management",
        "Indoor water feature or natural materials (e.g., wood, clay, stone)",
        "CO2 sensors and air purifiers in sleeping and reflective zones",
        "Quiet HVAC equipment with low decibel rating for sleep comfort"
    ]