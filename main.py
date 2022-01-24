# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template='Hello, <name>!'):
    greet = template.replace('<name>', name)
    return greet

#print(greet('Justin'))
#print(greet('Bob', "What's up, <name>!"))

gravity = {
    'sun': 274,
    'jupiter': 24.92,
    'earth': 9.798,
    'neptune': 11.15,
    'saturn': 10.44,
    'uranus': 8.87,
    'venus': 8.87,
    'mars': 3.71,
    'mercury': 3.7,
    'moon': 1.62,
    'pluto': 0.58
}

def force(mass, body):
    print(gravity[body])
    force = mass * gravity[body]
    return round(force, 1)

print(force(1, 'earth'))

def pull(m1, m2, d):
    G = 6.674e-11
    pull = G * ((m1 * m2)/ (d ** 2))
    return pull

print(pull(100000, 50000000, 300000000))