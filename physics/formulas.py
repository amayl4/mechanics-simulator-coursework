import variables as va

m1 = va.mass
m2 = va.mass2
u1 = va.velocity_init
u2 = va.velocity_init2
v1 = va.velocity
v2 = va.velocity2
λ = va.young_mod
x = va.displacement
l = va.natural_length
k = va.spring_constant
e = va.coefficient_restitution

def calculate_impulse1(m1, u1, v1):
    # Calculates the impulse of object 1 due to the collision with object 2
    impulse1 = (m1 * v1) - (m1 *  u1)
    return impulse1

print(calculate_impulse1(m1, u1, v1))

def calculate_impulse2(m2, u2, v2):
    # Calculates the impulse of object 2 due to the collision with object 1
    impulse2 = (m2 * v2) - (m2 *  u2)
    return impulse2

calculate_impulse2(m2, u2, v2)

def calculate_restitution(u1, u2, v1, v2):
    # Calculates the coefficient of restitution
    restitution = (v2 - v1) / (u1 - u2)
    return restitution

calculate_restitution(u1, u2, v1, v2)

def calculate_tension(λ, x, l):
    # Calculates the tension in a spring
    tension =  (λ * x) / l
    return tension 

calculate_tension(λ, x, l)

def calculate_epe(λ, x, l):
    # Calculates the elastic potential energy in a spring
    epe = (λ * x**2) / (2 * l)
    return epe

calculate_epe(λ, x, l)