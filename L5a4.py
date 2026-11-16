import math

def trigonometry(angle):
    radian = math.radians(angle)

    print("Angle:", angle, "degrees")
    print("Sin:", round(math.sin(radian), 2))
    print("Cos:", round(math.cos(radian), 2))
    print("Tan:", round(math.tan(radian), 2))


# Function calls
trigonometry(30)
trigonometry(45)
trigonometry(60)