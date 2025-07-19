<<<<<<< HEAD
# Flux Calculator

A simple Python tool that calculates the  flux  received at a distance from a hot spherical object, based on the **Stefan–Boltzmann Law**.


---

## What It Does

Given:
- The radius of a hot sphere
- Its surface temperature (in Celsius)
- The distance from the sphere to the observer
- (Optional) surface emissivity

It calculates the **energy per square meter (W/m^2)** reaching the observer.

---

## Formula Used

The Stefan–Boltzmann law is used in combination with the inverse-square law:
P=ε⋅σ⋅4πr^2 * T^4

But that power is spread out in all directions (like a balloon), over an area:
A= 4πd^2

So the flux at distace d is:
Flux = P/A

Where:
- `r` = sphere radius (m)  
- `d` = viewer distance (m)  
- `T` = temperature in **Kelvin**  
- `ε` = emissivity (default 1 for perfect blackbody)  
- `σ` = Stefan–Boltzmann constant = 5.670374419 × 10⁻⁸ W/m²·K⁴ 

# How to Run

1. download repository
2. make sure Pythin 3.6+ is installed
3. Run the program 
# python main.py


