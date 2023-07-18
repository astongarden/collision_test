import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 로봇 정보
robot_length_1 = 1.0    # 로봇 길이 (팔 길이 등)
robot_length_2 = 1.0    # 로봇 길이 (팔 길이 등)
robot_thickness = 0.2
joint_limits = [[-np.pi, np.pi], [-np.pi, np.pi]]  # 관절 각도 제한

# 로봇팔 관절 각도 입력 받기
joint_angle1 = float(input("Enter joint angle 1(deg): "))
joint_angle2 = float(input("Enter joint angle 2(deg): "))


def draw_rectangle(x, y, width, height, color):
    plt.gca().add_patch(Rectangle((x, y), width, height, linewidth=robot_thickness, edgecolor=color, facecolor='none'))

# 워크스페이스 그래프 생성
def plot_workspace(robot_angles):

    robot_angles = np.deg2rad(robot_angles)
    
    # 로봇팔 위치 계산
    x1 = robot_length_1 * np.cos(robot_angles[0])
    y1 = robot_length_1 * np.sin(robot_angles[0])
    x2 = x1 + robot_length_2 * np.cos(robot_angles[0] + robot_angles[1])
    y2 = y1 + robot_length_2 * np.sin(robot_angles[0] + robot_angles[1])

    # 그래프 그리기
    plt.plot([0, x1, x2], [0, y1, y2], 'k-')
    plt.plot(0, 0, 'ro', label='1 joint')
    plt.plot(x1, y1, 'go', label='2 joint')
    plt.plot(x2, y2, 'bo', label='End Effector')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Workspace')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# C-space 그래프 생성
def plot_cspace():
    # 각도 범위
    theta1 = np.linspace(joint_limits[0][0], joint_limits[0][1], 100)
    theta2 = np.linspace(joint_limits[1][0], joint_limits[1][1], 100)
    theta1, theta2 = np.meshgrid(theta1, theta2)

    # 그래프 그리기
    plt.contourf(theta1, theta2, np.zeros_like(theta1), cmap='gray')
    plt.xlabel('Joint 1 Angle')
    plt.ylabel('Joint 2 Angle')
    plt.title('C-space')
    plt.grid(True)
    plt.show()

# 충돌 여부 예측
def predict_collision(robot_angles):
    # 여기에서는 단순히 무작위로 충돌 여부를 예측하는 것으로 가정
    return bool(np.random.randint(0, 2))

# 로봇팔 위치 그리기
robot_angles = [joint_angle1, joint_angle2]
plot_workspace(robot_angles)

# C-space 그래프 그리기
plot_cspace()

# # 장애물 생성 및 충돌 여부 예측
# obstacle_x = np.random.uniform(-1, 1)
# obstacle_y = np.random.uniform(-1, 1)
# obstacle_width = np.random.uniform(0.2, 0.5)
# obstacle_height = np.random.uniform(0.2, 0.5)

# collision = False
# if obstacle_x <= robot_length_1 * np.cos(joint_angle1) + robot_length_2 * np.cos(joint_angle1 + joint_angle2) and \
#    obstacle_y <= robot_length_1 * np.sin(joint_angle1) + robot_length_2 * np.sin(joint_angle1 + joint_angle2):
#     collision = True

# # 예측 결과 출력
# print("Collision Prediction: ", collision)