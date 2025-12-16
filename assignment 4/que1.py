def km_to_m(km):
    return km*1000
def m_to_mm(m):
    return m*100
def mm_to_cm(m):
    return m*1000
def feet_to_inc(feet):
    return feet*12
def inc_to_cm(inc):
    return inc*2.54
def dist_conv(distance,conv_type,conv_func):
    result =conv_func(distance)
    print(f"{conv_type}:{result}")
distance=float(input("enter distance:"))
dist_conv(distance,"km_m",km_to_m)
dist_conv(distance,"m_mm",m_to_mm)
dist_conv(distance,"mm_cm",mm_to_cm)
dist_conv(distance,"feet_inc",feet_to_inc)
dist_conv(distance,"inc_cm",inc_to_cm)


