# Seyed Mahdi Mahdavian / 40012341106069

# Importing libraries
import numpy as np
import math 

def exercise_1():

   # Inputs and Constants
   Velocity = psidot = float(input("Velocity(psidot)= "))
   phi = float(input("phi= "))
   phi_rad = float((3.14/180) * phi)
   theta_1 = 0
   psi = 0
   g = float(9.81) 

   # Calculation of P1 , Q1 , R1 for cordinated turn
   P1 = -Velocity * math.sin(theta_1)
   Q1 = Velocity * math.cos(theta_1) * math.sin(phi_rad)
   R1 = Velocity * math.cos(theta_1) * math.cos(phi_rad)

   #Angular velocity in body frame  matrix 
   Angular_velocity_in_body_frame  = np.array  ([[P1],
                                              [Q1],
                                              [R1]])
   #print Angular velocity in body frame matrix 
   print("Angular_velocity_in_body_frame: ")
   print(Angular_velocity_in_body_frame)

   # Transformation Matrix (Inertia to body)
   C_bi = np.array ([[np.cos(psi) * np.cos(theta_1), np.cos(theta_1) * np.sin(psi), -np.sin(theta_1)],
                     [np.cos(psi) * np.sin(phi) * np.sin(theta_1) - np.cos(phi) * np.sin(psi), 
                      np.cos(phi) * np.cos(psi) + np.sin(phi) * np.sin(theta_1) * np.sin(psi), 
                      np.cos(theta_1) * np.sin(phi)],
                      [np.sin(phi) * np.sin(psi) + np.cos(phi) * np.cos(psi) * np.sin(theta_1), 
                      np.cos(phi) * np.cos(theta_1)]])

   # Transformation Matrix (Inertia to body)
   C_ib = C_bi.T

   # Angular velocity in inertial frame matrix 
   Angular_velocity_in_inertial_frame = np.dot(C_ib, Angular_velocity_in_body_frame)

   # print Angular velocity in inertial frame
   print("Angular_velocity_in_inertial_frame: ")
   print(Angular_velocity_in_inertial_frame)



def exercise_2():
   
   # Inputs
   P = float(input("P(Roll rate): "))
   Q = float(input("Q(Pitch rate): "))
   R = float(input("R(Yaw rate): "))
   psi_dot = float(input("psi_dot: "))

   # Matrix of P , Q , R according to the question 
   Angular_velocity  = np.array  ([[P],
                                   [Q],
                                   [R]])

   # print Angular velocity
   print("Angular_velocity")
   print(Angular_velocity)

   # Calculation of thta_1 , phi _1 , psi_1
   theta_1 = math.asin(-P / psi_dot)
   phi_1 = math.asin(Q / (psi_dot * math.cos(theta_1)))
   psi_1 = -P / math.sin(theta_1)

   # print theta , phi , psi
   print("Euler_angles: ")

   print("theta:")
   print(theta_1)

   print("phi ")
   print(phi_1)

   print("psi")
   print(psi_1)

 


def exercise_3():

    # Transformation Matrix (Inertia to body) 
    C_bi = np.array([ 
                     [float(input("The element at (1,1)[0,0]: ")), float(input("The element at (1,2)[0,1]: ")), float(input("The element at (1,3)[0,2]: "))],
                     [float(input("The element at (2,1)[1,0]: ")), float(input("The element at (2,2)[1,1]: ")), float(input("The element at (2,3)[1,2]: "))],
                     [float(input("The element at (3,1)[2,0]: ")), float(input("The element at (3,2)[2,1]: ")), float(input("The element at (3,3)[2,2]: "))]
                                                                                                                                                            ])
   # برای اینکه یک ماتریس انتقال باشد، طبق اسلاید 19 فصل اول اسلاید  باید دترمینان آن برابر با 1 باشد پس دترمینان آن را حساب میکنیم
   # det_C_bi
    det_C_bi = np.linalg.det(C_bi)
    print("det_C_bi= " , det_C_bi)


    if det_C_bi == 1: 
       print("ماتریس ورودی شرایط یک ماتریس انتقال است")
   
       # Calculation of theta , psi , phi
       theta = math.asin(-C_bi[0, 2])
       cos_theta = math.cos(theta)

       # Prevent division by zero (singularity)
       if abs(cos_theta) > 1e-6:
         psi = math.asin(C_bi[0, 1]/cos_theta)
         phi = math.asin(C_bi[1, 2]/cos_theta)

         #Euler_angles 
         print("Euler_angles: ")
         print("theta = ", theta)
         print("psi = ", psi)
         print("phi = ", phi)

         # Calculation of a , b , c , d for Quaternion_vector
         a = (math.cos(phi/2) * math.cos(theta/2) * math.cos(psi/2)) - (math.sin(phi/2) * math.sin(theta/2) * math.sin(psi/2))
         b = (math.sin(phi/2) * math.cos(theta/2) * math.cos(psi/2)) + (math.cos(phi/2) * math.sin(theta/2) * math.sin(psi/2))
         c = (math.cos(phi/2) * math.sin(theta/2) * math.cos(psi/2)) - (math.sin(phi/2) * math.cos(theta/2) * math.sin(psi/2))
         d = (math.cos(phi/2) * math.cos(theta/2) * math.sin(psi/2)) - (math.sin(phi/2) * math.sin(theta/2) * math.cos(psi/2))

         #Quaternion vector
         Quaternion_vector = np.array([[a],
                                       [b],
                                       [c],
                                       [d]])
         print("Quaternion_vector= " ) 
         print(Quaternion_vector)

         # Prevent division by zero (singularity)
         if abs(math.sin(phi/2)) > 1e-6:
               phi_x = (b / math.sin(phi/2)) * phi
               phi_y = (c / math.sin(phi/2)) * phi
               phi_z = (d / math.sin(phi/2)) * phi
  
               #Rotaion Vector
               Rotaion_Vector = np.array([[phi_x]
                                          [phi_y]
                                          [phi_z]])
               print("Rotaion_Vector= " , Rotaion_Vector)
         else:
               print("singularity")                                  
       else:
            print("singularity")

    else:
       print("ماتریس ورودی شرایط یک ماتریس انتقال را ندارد")


if __name__ == "__main__":
    print("choose exercise  ")
    choice = input("exercise 1 or 2 or 3: ")

    if choice == "1":
        exercise_1()
    elif choice == "2":
        exercise_2()
    elif choice == "3":
        exercise_3()
    else:
        print("انتخاب اشتباه است")