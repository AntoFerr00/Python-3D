from vpython import sphere, vector, rate, color, distant_light, scene, sin, cos, ring, label, mag
import random

################################################################################
# SCENE SETUP
################################################################################
scene.background = color.black
scene.title = "3D Interactive Solar System"

################################################################################
# SUN
################################################################################
sun = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.orange, emissive=True)
label(pos=sun.pos, text="Sun", xoffset=20, yoffset=20, color=color.white)

################################################################################
# PLANET DATA
################################################################################
# Format: [distance, radius, color, orbital_speed, spin_speed, name]
# spin_speed: how fast the planet rotates about its own axis
planets_data = [
    [1.0, 0.1,  color.gray(0.5), 1.2,  1.5,  "Mercury"],
    [1.5, 0.15, color.yellow,    0.9,  1.2,  "Venus"],
    [2.0, 0.17, color.blue,      0.7,  2.0,  "Earth"],
    [2.7, 0.12, color.red,       0.5,  1.9,  "Mars"],
    [3.8, 0.3,  color.orange,    0.3,  1.0,  "Jupiter"],
    [5.0, 0.25, color.cyan,      0.2,  0.9,  "Saturn"],
]

planets = []
for dist, radius, col, orbit_speed, spin_speed, name in planets_data:
    planet = sphere(
        pos=vector(dist, 0, 0),
        radius=radius,
        color=col,
        make_trail=True
    )
    label(pos=planet.pos, text=name, xoffset=15, yoffset=15, height=10, color=color.white)
    planets.append({
        "sphere": planet,
        "angle": 0,            # orbital angle
        "orbit_speed": orbit_speed,
        "dist": dist,
        "spin_speed": spin_speed
    })

################################################################################
# SATURN RING
################################################################################
saturn_ring = ring(pos=planets[5]["sphere"].pos, axis=vector(0, 1, 0), radius=0.35, thickness=0.03, color=color.white)

################################################################################
# ASTEROID BELT
################################################################################
asteroids = []
num_asteroids = 100
for i in range(num_asteroids):
    angle = i * (2 * 3.14159 / num_asteroids)
    rock = sphere(
        pos=vector(3.3 * cos(angle), 0, 3.3 * sin(angle)),
        radius=0.02,
        color=color.gray(0.7)
    )
    asteroids.append(rock)

################################################################################
# COMET WITH ELLIPTICAL ORBIT
################################################################################
comet = sphere(pos=vector(0, 0, 0), radius=0.05, color=color.white, make_trail=True)
comet_angle = 0
# Ellipse parameters
a = 6.0  # semi-major axis
b = 3.0  # semi-minor axis

################################################################################
# RANDOM STARFIELD WITH FLICKER
################################################################################
star_count = 150
stars = []
for _ in range(star_count):
    # Place stars far away on random sphere radius 20-30
    r = random.uniform(20, 30)
    theta = random.uniform(0, 2*3.14159)
    phi = random.uniform(0, 3.14159)
    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)
    # Random flicker speed
    flicker_rate = random.uniform(1, 3)
    star_sphere = sphere(pos=vector(x, y, z), radius=0.05, color=color.white, emissive=True)
    stars.append({
        "sphere": star_sphere,
        "phase": random.random() * 6.28,
        "flicker_rate": flicker_rate
    })

################################################################################
# PLAYER-CONTROLLED SPACESHIP
################################################################################
spaceship = sphere(pos=vector(-8, 0, 0), radius=0.15, color=color.green)
# Axis points in +x direction by default
spaceship.axis = vector(1, 0, 0)
spaceship_velocity = vector(0, 0, 0)
acceleration = 0.03
rotation_speed = 0.03

# Keep track of pressed keys
keys_pressed = set()

def keydown(evt):
    keys_pressed.add(evt.key)

def keyup(evt):
    if evt.key in keys_pressed:
        keys_pressed.remove(evt.key)

scene.bind('keydown', keydown)
scene.bind('keyup', keyup)

################################################################################
# LIGHTING
################################################################################
distant_light(direction=vector(1, -0.5, 0), color=color.white)

################################################################################
# ANIMATION LOOP
################################################################################
while True:
    rate(60)

    # Update planet orbits and spins
    for p in planets:
        p["angle"] += p["orbit_speed"] * 0.01
        x = p["dist"] * cos(p["angle"])
        z = p["dist"] * sin(p["angle"])
        p["sphere"].pos = vector(x, 0, z)
        # Spin each planet on its axis
        p["sphere"].rotate(angle=p["spin_speed"]*0.01, axis=vector(0,1,0))

    # Update Saturn ring position
    saturn_ring.pos = planets[5]["sphere"].pos

    # Update comet elliptical orbit
    comet_angle += 0.007
    comet_x = a * cos(comet_angle)
    comet_z = b * sin(comet_angle)
    comet.pos = vector(comet_x, 0, comet_z)

    # Flicker stars
    for star in stars:
        star["phase"] += star["flicker_rate"] * 0.01
        # Flicker intensity: vary between 0.3 and 1.0
        intensity = 0.3 + 0.7 * (0.5 + 0.5 * sin(star["phase"]))
        star["sphere"].color = vector(intensity, intensity, intensity)

    ################################################################################
    # SPACESHIP CONTROLS
    ################################################################################
    if 'up' in keys_pressed:
        # accelerate forward
        forward_dir = spaceship.axis.norm()
        spaceship_velocity += forward_dir * acceleration
    if 'down' in keys_pressed:
        # accelerate backward
        forward_dir = spaceship.axis.norm()
        spaceship_velocity -= forward_dir * acceleration
    if 'left' in keys_pressed:
        # rotate left
        spaceship.rotate(angle=rotation_speed, axis=vector(0,1,0))
    if 'right' in keys_pressed:
        # rotate right
        spaceship.rotate(angle=-rotation_speed, axis=vector(0,1,0))

    # Apply friction
    spaceship_velocity *= 0.98

    # Update spaceship position
    spaceship.pos += spaceship_velocity

    # Detect collision with asteroids
    collided = False
    for rock in asteroids:
        if mag(spaceship.pos - rock.pos) < (spaceship.radius + rock.radius):
            collided = True
            break
    if collided:
        spaceship.color = color.red
    else:
        spaceship.color = color.green
