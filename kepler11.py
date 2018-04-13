#!/usr/bin/python3
"""
created by alex on 4/13/18
Models kepler 11 with vpython
"""
from vpython import *


def v_orbit(radius):
	"""
	Calculates the orbital velocity of a planet around the host star. This only works specifically to the kepler11 star.

	:param radius: semi-major axis of the planet in AU
	:return: velocity of orbit in km/s
	"""
	return ((G * star_mass) / radius) ** 0.5


# Constants
G = 6.67428e-11  				# m^3 kg^-1 s^-2
AU = 1.496e11  					# 1 au in meters
m_sun = 1.989e30  				# kg
m_earth = 5.976e24  			# kg
# r_sun = 9.957e8					# m
# r_earth = 6.37e6  				# m
r_sun = 10						# Arbitrary number
r_earth = 1						# Arbitrary numbers
scale = 1e9  					# Scaling factor

# Star constants
star_mass = 0.961 * m_sun  		# solar masses
star_radius = 1.065 * r_sun  	# Solar radii
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

names = ["Sun", "planet-b", "planet-c", "planet-d", "planet-e", "planet-f", "planet-g"]

mass_list = [star_mass, m_b, m_c, m_d, m_e, m_f, m_g]

sizes = [star_radius, r_b, r_c, r_d, r_e, r_f, r_g]

colors = [color.yellow, color.green, color.cyan, color.blue, color.orange, color.magenta, color.red]

trails = [True, True, True, True, True, True, True]

initial_velocity = [v_star, v_b, v_c, v_d, v_e, v_f, v_g]

x_vel = [0, 0, 0, 0, 0, 0, 0]

y_vel = initial_velocity

total_p = (m_b * v_b) + (m_c * v_c) + (m_d * v_d) + (m_e * v_e) + (m_f * v_f) + (m_g * v_g)

v_star = -total_p / star_mass

dist_from_star = [vec(0, 0, 0), vec(a_b / scale, 0, 0), vec(a_c / scale, 0, 0), vec(a_d / scale, 0, 0),
				  vec(a_e / scale, 0, 0), vec(a_f / scale, 0, 0), vec(a_g / scale, 0, 0)]

x_pos = [0, a_b, a_c, a_d, a_e, a_f, a_g]

y_pos = [0, 0, 0, 0, 0, 0, 0]

dt = 5000

s = []

for n in range(0, len(names)):
	s.append(sphere(pos=vec(dist_from_star[n]), radius=sizes[n], color=colors[n], make_trail=trails[n]))

while True:
	for n in range(1, len(names)):
		rate(500)

		y_pos[n] = y_pos[n] + y_vel[n] * dt
		x_pos[n] = x_pos[n] + x_vel[n] * dt
		x, y = x_pos[n], y_pos[n]
		s[n].pos = vec(x / scale, y / scale, 0)

		r = sqrt(x ** 2 + y ** 2)

		if r < 7e8:
			print("%s HAS CRASHED INTO THE SUN!" % (names[n]))
			break

		if r > 1e10 * 7e8:
			print("%s HAS BEEN EJECTED FROM THE SYSTEM" % (names[n]))
			break

		f = (G * mass_list[n] * mass_list[0]) / (r ** 2)

		angle = atan2(-y, -x)

		fx = cos(angle) * f
		fy = sin(angle) * f

		ax = fx / mass_list[n]
		ay = fy / mass_list[n]

		x_vel[n] = x_vel[n] + (ax * dt)
		y_vel[n] = y_vel[n] + (ay * dt)
