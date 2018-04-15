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


def create_planet(p):
	"""
	Adds the planet into the scene from radio button press
	"""

	if p.checked:
		s.append(Planet(p.text, p.a, p.r, p.m, p.v, p.c))
	else:
		planet = next((i for i in s if i.name == p.text), None)
		planet.visible = False
		planet.clear_trail()
		del s[s.index(planet)]


class Planet(sphere):
	def __init__(self, name, a, radius, mass, velocity, planet_color, **args):
		super().__init__(**args)
		self.name = name
		self.a = a
		self.radius = radius
		self.mass = mass
		self.x_pos = self.a
		self.y_pos = 0
		self.x_vel = 0
		self.y_vel = velocity
		self.planet_color = planet_color
		sphere.__init__(self, pos=vec(self.a, 0, 0), radius=self.radius, color=self.planet_color, make_trail=True)


# Constants
G = 6.67428e-11  				# m^3 kg^-1 s^-2
AU = 1.496e11  					# 1 au in meters
m_sun = 1.989e30  				# kg
m_earth = 5.976e24  			# kg
r_sun = 9.957e8					# m
r_earth = 6.37e6  				# m

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

total_p = (m_b * v_b) + (m_c * v_c) + (m_d * v_d) + (m_e * v_e) + (m_f * v_f) + (m_g * v_g)

v_star = -total_p / star_mass

# radio buttons, where id values are the index position in names array
rb = radio(bind=create_planet, checked=False, text='planet-b', a=a_b, r=r_b, m=m_b, v=v_b, c=color.green)
rc = radio(bind=create_planet, checked=False, text='planet-c', a=a_c, r=r_c, m=m_c, v=v_c, c=color.cyan)
rd = radio(bind=create_planet, checked=False, text='planet-d', a=a_d, r=r_d, m=m_d, v=v_d, c=color.blue)
re = radio(bind=create_planet, checked=False, text='planet-e', a=a_e, r=r_e, m=m_e, v=v_e, c=color.orange)
rf = radio(bind=create_planet, checked=False, text='planet-f', a=a_f, r=r_f, m=m_f, v=v_f, c=color.magenta)
rg = radio(bind=create_planet, checked=False, text='planet-g', a=a_g, r=r_g, m=m_g, v=v_g, c=color.red)

s = [Planet('kepler-11', 0, star_radius, star_mass, v_star, color.yellow),
	 # Planet("planet-b", a_b, r_b, m_b, v_b, color.green),
	 # Planet("planet-c", a_c, r_c, m_c, v_c, color.cyan),
	 # Planet("planet-d", a_d, r_d, m_d, v_d, color.blue),
	 # Planet("planet-e", a_e, r_e, m_e, v_e, color.orange),
	 # Planet("planet-f", a_f, r_f, m_f, v_f, color.magenta),
	 # Planet("planet-g", a_g, r_g, m_g, v_g, color.red),
	 ]

dt = 5000

while True:

	if len(s) > 1:
		for n in range(1, len(s)):
			try:
				rate(500)

				s[n].x_pos = s[n].x_pos + s[n].x_vel * dt
				s[n].y_pos = s[n].y_pos + s[n].y_vel * dt

				x, y = s[n].x_pos, s[n].y_pos
				s[n].pos = vec(x, y, 0)

				r = sqrt(x ** 2 + y ** 2)

				if r < 7.5e6:
					print("%s HAS CRASHED INTO THE SUN!" % s[n].name)
					break

				if r > 1e10 * 7.5e6:
					print("%s HAS BEEN EJECTED FROM THE SYSTEM" % s[n].name)
					break

				for planet2 in s:
					if s[n] != planet2:

						f = (G * s[n].mass * star_mass) / (r ** 2)

						angle = atan2(-y, -x)

						fx = cos(angle) * f
						fy = sin(angle) * f

						ax = fx / s[n].mass
						ay = fy / s[n].mass

						s[n].x_vel = s[n].x_vel + (ax * dt)
						s[n].y_vel = s[n].y_vel + (ay * dt)

			except IndexError:
				pass
