print("🍀Welcome to PlantPal - Your Plant Care Assistant🍀\n")
# Dictionary to store plant data
plant_info= {
    "tulsi": {
        "water": "water daily in summer, every other day in winter.",
        "sunlight": "loves sunlight, 4-6 hours of direct sunlight daily",
        "tip": "pinch off flower buds to help plant grow bushier."
    },
    "aloevera": {
        "water": "water deeply but rarely. once every 3 weeks is enough.",
        "sunlight": "bright, indirect light or some direct morning sun.",
        "tip": "make sure the pot has drainage holes to avoid root rots"
    }
    
}
# ask user for their plant
plant_name= input("Enter the name of your plant:").lower()
if plant_name in plant_info:
    info = plant_info[plant_name]
    print(f"\n care tips for {plant_name.title()}")
    print(f"Watering: {info['water']}")
    print(f"Sunlight: {info['sunlight']}")
    print(f"Extra tip: {info['tip']}")
else:
    print("\n oops! I don't have info on that plant yet")
    print("\n Thanks for using PlantPal! Happy Growing")