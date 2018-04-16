#!/usr/bin/python3
"""
created by alex on 4/15/18

"""
from vpython import *


def grav_acc(obj, other):
	""" acceleration of an object due to gravitational force """
	r_vector = obj.pos - other.pos
	acc = -((G * other.mass) / r_vector.mag2)
	acc = acc * r_vector.norm()
	return acc


def v_orbit(radius):
	"""
	Calculates the orbital velocity of a planet around the host star. This only works specifically to the kepler11 star.

	:param radius: semi-major axis of the planet in AU
	:return: velocity of orbit in km/s
	"""
	return ((G * m_star) / radius) ** 0.5


# Constants
G = 6.67428e-11  				# m^3 kg^-1 s^-2
AU = 1.496e11  					# 1 au in meters
m_sun = 1.989e30  				# kg
m_earth = 5.976e24  			# kg
r_sun = 9.957e8					# m
r_earth = 6.37e6  				# m

# Star constants
m_star = 0.961 * m_sun  		# solar masses
r_star = 1.065 * r_sun  	# Solar radii
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

# create the solar system
planets = [
		sphere(pos=vec(0, 0, 0), radius=r_star, color=color.yellow, mass=m_star, velocity=vec(0, 0, 0), make_trail=True),
		sphere(pos=vec(a_b, 0, 0), radius=r_b, color=color.green, mass=m_b, velocity=vec(0, v_b, 0), make_trail=True),
		sphere(pos=vec(a_c, 0, 0), radius=r_c, color=color.cyan, mass=m_c, velocity=vec(0, v_c, 0), make_trail=True),
		sphere(pos=vec(a_d, 0, 0), radius=r_d, color=color.blue, mass=m_d, velocity=vec(0, v_d, 0), make_trail=True),
		sphere(pos=vec(a_e, 0, 0), radius=r_e, color=color.orange, mass=m_e, velocity=vec(0, v_e, 0), make_trail=True),
		sphere(pos=vec(a_f, 0, 0), radius=r_f, color=color.magenta, mass=m_f, velocity=vec(0, v_f, 0), make_trail=True),
		sphere(pos=vec(a_g, 0, 0), radius=r_f, color=color.red, mass=m_g, velocity=vec(0, v_g, 0), make_trail=True)
		]

dt = 5000

while True:

	rate(500)

	for planet1 in planets:
		for planet2 in planets:
			if planet1 != planet2:
				planet1.velocity += grav_acc(planet1, planet2) * dt

	# update the position of the objects
	for planet in planets:
		planet.pos += planet.velocity * dt
