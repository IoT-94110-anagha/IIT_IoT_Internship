km_to_m=lambda km:km*1000
m_to_mm=lambda m:m*100
mm_to_cm=lambda m:m*1000
feet_to_inc=lambda feet:feet*12
inc_to_cm=lambda inc:inc*2.54
def dist_conv(distance,conv_type,conv_func):
    result =conv_func(distance)
    print(f"{conv_type}:{result}")
distance=float(input("enter distance:"))
dist_conv(distance,"km_m",km_to_m)
dist_conv(distance,"m_mm",m_to_mm)
dist_conv(distance,"mm_cm",mm_to_cm)
dist_conv(distance,"feet_inc",feet_to_inc)
dist_conv(distance,"inc_cm",inc_to_cm)

