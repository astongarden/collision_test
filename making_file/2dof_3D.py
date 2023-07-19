import sys
import gjk
import math
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import time

# color

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# information of robot

robot_link1 = 200
robot_link2 = 200
robot_thickness = 20

def run():
    start = time.time()

    for q1_rad in range(0, 360):
        for q2_rad in range(0, 360):
            
            q1 = math.radians(q1_rad) 
            q2 = math.radians(q2_rad) 

            link_1 = (
                (robot_thickness*math.sin(q1),-robot_thickness*math.cos(q1)),
                (-robot_thickness*math.sin(q1),robot_thickness*math.cos(q1)),
                (-robot_thickness*math.sin(q1)+robot_link1*math.cos(q1),robot_thickness*math.cos(q1)+robot_link1*math.sin(q1)),
                (robot_thickness*math.sin(q1)+robot_link1*math.cos(q1),-robot_thickness*math.cos(q1)+robot_link1*math.sin(q1))
                )

            link_2 = (
                (robot_link1*math.cos(q1)+robot_thickness*math.sin(q2),robot_link1*math.sin(q1)-robot_thickness*math.cos(q2)),
                (robot_link1*math.cos(q1)-robot_thickness*math.sin(q2),robot_link1*math.sin(q1)+robot_thickness*math.cos(q2)),
                (robot_link1*math.cos(q1)-robot_thickness*math.sin(q2)+robot_link2*math.cos(q2),robot_link1*math.sin(q1)+robot_thickness*math.cos(q2)+robot_link2*math.sin(q2)),
                (robot_link1*math.cos(q1)+robot_thickness*math.sin(q2)+robot_link2*math.cos(q2),robot_link1*math.sin(q1)-robot_thickness*math.cos(q2)+robot_link2*math.sin(q2))
                )
            


            obstacle = ((300, 0), 20)

            collide_1 = gjk.collidePolyCircle(link_1, obstacle)
            polygon(link_1)
            circle(obstacle)
            collide_2 = gjk.collidePolyCircle(link_2, obstacle)
            polygon(link_2)
            circle(obstacle)


            # # make graph to see robot arm and obstacle

            # fig, ax = plt.subplots()

            # link1_patch = patches.Polygon(link_1, edgecolor='blue', facecolor='blue')
            # ax.add_patch(link1_patch)
            
            # link2_patch = patches.Polygon(link_2, edgecolor='red', facecolor='red')
            # ax.add_patch(link2_patch)

            # obstacle_patch = patches.Circle(obstacle[0], obstacle[1], edgecolor='black', facecolor='black')
            # ax.add_patch(obstacle_patch)

            # ax.set_xlim(-400, 400)
            # ax.set_ylim(-400, 400)
            
            # plt.show()


            # # print result

            # print('True' if (collide_1 or collide_2) else 'fail')

            # save result to txt file continue

            file_path = "/home/jeongil/collision/making_file/2dof_3D_result.txt"
            
            with open(file_path, "a") as file:          
                file.write(f"q1 : {q1_rad}  ")
                file.write(f"q2 : {q2_rad}  ")
                file.write(f"collision resutl : {'True' if (collide_1 or collide_2) else 'fail'}\n")

    end = time.time()

    #check time and print, save in txt file
    
    print(f"{end - start :.5f} sec")

    file_path = "/home/jeongil/collision/making_file/2dof_3D_result.txt"
    with open(file_path, "a") as file:
        file.write(f"\ncalculation time is : {end - start :.5f} sec")


def pairs(points):
    for i, j in enumerate(range(-1, len(points) - 1)):
        yield (points[i], points[j])

def circles(cs, color=BLACK, camera=(0, 0)):
    for c in cs:
        circle(c, color, camera)

def circle(c, color=BLACK, camera=(0, 0)):
    ()

def polygon(points, color=BLACK, camera=(0, 0)):
    for a, b in pairs(points):
        line(a, b, color, camera)

def line(start, end, color=BLACK, camera=(0, 0)):
    ()

def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]



# run code 

if __name__ == '__main__':
    run()

