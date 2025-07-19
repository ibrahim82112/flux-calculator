import math 

STEFAN_BOLTZMANN_CONSTANT = 5.670374419e-8

def flux_calculator(sphere_radius, viewer_distance, temperature_celsius, emissivity= 1 ):
    """
    Calculate the flux at a distance from a hot sphere

    Parameters:
    - sphere_radius(float): Radius of the sphere
    - viewer_distance(float) : Distance from the sphere center to the viewer in meters
    - temperature_celsius(float) : Temperature of the sphere in Celsius
    - emissivity(float) : As no specific intructions were given i have decided to use the default value

    Returns: 
    - flux(float): Flux in W/m2 at viewer's location 
    """

    # Convert temperature to Kelvin
    Temperature_kelvin = 273.15 + temperature_celsius

    # Area of a sphere 
    Area_Sphere = 4 * math.pi * sphere_radius**2

    #Total Power radiated
    Total_Power = STEFAN_BOLTZMANN_CONSTANT  * Area_Sphere * Temperature_kelvin**4

    # Area over which the power spreads
    Spread_Area = 4 * math.pi * viewer_distance**2

    # Flux recieved per square meter at a distance
    Flux = Total_Power / Spread_Area

    return Flux

# Using given example 
if __name__ == "__main__":


#Parameters

    sphere_radius = 1.0  # meters
    viewer_distance = 100.0  # meters
    temperature_celsius = 1000.0 # degrees Celsius

# Display the flux
result = flux_calculator(sphere_radius, viewer_distance, temperature_celsius,)
print(f"Flux at {viewer_distance}m: {result:.4f} W/m^2")



