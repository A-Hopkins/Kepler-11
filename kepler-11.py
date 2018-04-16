#!/usr/bin/python3
"""
created by alex on 4/15/18

"""
from vpython import *


def grav_acc(obj, other):
	"""
	acceleration of an object due to gravitational force

	:param obj: vpython sphere object: First object to calculate the force of gravity
	:param other: vpython sphere object: Second object to calculate the force of gravity on
	:return: acceleration between two objects
	 """
	r_vector = obj.pos - other.pos
	acc = -((G * other.mass) / r_vector.mag2)
	acc = acc * r_vector.norm()
	return acc


def v_orbit(radius):
	"""
	Calculates the orbital velocity of a planet around the host star. This only works specifically to the kepler-11 star.
	Unless you changed m_star value.

	:param radius: semi-major axis of the planet in AU
	:return: velocity of orbit in km/s
	"""
	return ((G * m_star) / radius) ** 0.5


def create_planet(p):
	"""
	Adds the planet into the scene from radio button press
	"""

	if p.checked:
		planets.append(sphere(pos=vec(p.a, 0, 0), radius=p.r, color=p.c, mass=p.m, velocity=vec(0, p.v, 0), make_trail=True))
	else:
		plnet = next((i for i in planets if i.radius == p.r), None)
		plnet.visible = False
		plnet.clear_trail()
		del planets[planets.index(plnet)]


# Constants
G = 6.67428e-11  				# m^3 kg^-1 s^-2
AU = 1.496e11  					# 1 au in meters
m_sun = 1.989e30  				# kg
m_earth = 5.976e24  			# kg
r_sun = 9.957e8					# m
r_earth = 6.37e6  				# m

# Star constants
m_star = 0.961 * m_sun  		# solar masses
r_star = 1.065 * r_sun  		# Solar radii
v_star = 0						# Essentially placeholder

# Planet Masses
m_b = 1.9 * m_earth 	 		# Earth masses
m_c = 2.9 * m_earth				# Earth masses
m_d = 7.3 * m_earth 			# Earth masses
m_e = 8.0 * m_earth  			# Earth masses
m_f = 2.0 * m_earth  			# Earth masses
m_g = 7.5 * m_earth  			# Earth masses

# Planet radii
r_b = 1.80 * r_earth  			# Earth radii
r_c = 2.87 * r_earth  			# Earth radii
r_d = 3.12 * r_earth  			# Earth radii
r_e = 4.19 * r_earth  			# Earth radii
r_f = 2.49 * r_earth  			# Earth radii
r_g = 3.33 * r_earth  			# Earth radii

# Planet semi-major axes
a_b = 0.091 * AU				# m
a_c = 0.107 * AU				# m
a_d = 0.155 * AU				# m
a_e = 0.195 * AU				# m
a_f = 0.250 * AU				# m
a_g = 0.466 * AU  				# m

# Planet orbital velocities
v_b = v_orbit(a_b)  			# m/s
v_c = v_orbit(a_c)  			# m/s
v_d = v_orbit(a_d)  			# m/s
v_e = v_orbit(a_e)  			# m/s
v_f = v_orbit(a_f)  			# m/s
v_g = v_orbit(a_g)  			# m/s

# Momentum
total_p = (m_b * v_b) + (m_c * v_c) + (m_d * v_d) + (m_e * v_e) + (m_f * v_f) + (m_g * v_g)

v_star = -total_p / m_star

# Radio buttons to add/remove planets on screen
rb = radio(bind=create_planet, checked=True, text='planet-b', a=a_b, r=r_b, m=m_b, v=v_b, c=color.green)
rc = radio(bind=create_planet, checked=True, text='planet-c', a=a_c, r=r_c, m=m_c, v=v_c, c=color.cyan)
rd = radio(bind=create_planet, checked=True, text='planet-d', a=a_d, r=r_d, m=m_d, v=v_d, c=color.blue)
re = radio(bind=create_planet, checked=True, text='planet-e', a=a_e, r=r_e, m=m_e, v=v_e, c=color.orange)
rf = radio(bind=create_planet, checked=True, text='planet-f', a=a_f, r=r_f, m=m_f, v=v_f, c=color.magenta)
rg = radio(bind=create_planet, checked=True, text='planet-g', a=a_g, r=r_g, m=m_g, v=v_g, c=color.red)

# Create the kepler-11 system
planets = [
		sphere(pos=vec(0, 0, 0), radius=r_star, color=color.yellow, mass=m_star, velocity=vec(0, v_star, 0), make_trail=True),
		sphere(pos=vec(a_b, 0, 0), radius=r_b, color=color.green, mass=m_b, velocity=vec(0, v_b, 0), make_trail=True),
		sphere(pos=vec(a_c, 0, 0), radius=r_c, color=color.cyan, mass=m_c, velocity=vec(0, v_c, 0), make_trail=True),
		sphere(pos=vec(a_d, 0, 0), radius=r_d, color=color.blue, mass=m_d, velocity=vec(0, v_d, 0), make_trail=True),
		sphere(pos=vec(a_e, 0, 0), radius=r_e, color=color.orange, mass=m_e, velocity=vec(0, v_e, 0), make_trail=True),
		sphere(pos=vec(a_f, 0, 0), radius=r_f, color=color.magenta, mass=m_f, velocity=vec(0, v_f, 0), make_trail=True),
		sphere(pos=vec(a_g, 0, 0), radius=r_f, color=color.red, mass=m_g, velocity=vec(0, v_g, 0), make_trail=True)
		]

dt = 1000

while True:

	rate(500)

	# update the position of the objects
	for planet in planets:
		planet.pos += planet.velocity * dt

	for planet1 in planets:
		for planet2 in planets:
			if planet1 != planet2:
				planet1.velocity += grav_acc(planet1, planet2) * dt

