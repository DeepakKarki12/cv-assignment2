# Importing all modules
import cv2
import numpy as np
import time
import pandas as pd


new_data = {'colour': [],
            'entry': [],
            'exit': [],
            'quadrant': []
            }
df = pd.DataFrame(new_data)

# Specifying upper and lower ranges of color to detect in hsv format
# yellow
y_lower = np.array([15, 150, 20])
y_upper = np.array([35, 255, 255]) # (These ranges will detect Yellow)
# orange np.array()
o_lower=np.array([0, 100, 180])
o_upper=np.array([10, 255, 255])
# blue
b_lower=np.array([50, 50, 50])
b_upper=np.array([100, 255, 255])
#white
w_lower = np.array([13, 20, 207])
w_upper = np.array([22, 36, 255])

# Capturing webcam footage
webcam_video = cv2.VideoCapture('AI_Assignment_video.avi')
cv2.namedWindow('My Window',cv2.WINDOW_KEEPRATIO)
# cv2.setWindowProperty('My Window',cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_KEEPRATIO)
# cv2.setWindowProperty('My Window',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# webcam_video.set(3,640)
# webcam_video.set(4,480)
x_o = 0
y_o = 0
first_1_time_enable_o = 1
first_2_time_enable_b= 1
first_3_time_enable= 1
first_4_time_enable= 1

first_3_time_enable_b= 1
first_4_time_enable_b = 1
first_time_y = 0
entry_blue_time = 0
quadrant_blue = 0

first_time_y_1 = 0

ptime = time.time()
enter_exit_time = 0

ball_inside_3_quadrant = False
ball_inside_3_quadrant_b = False
ball_inside_2_quadrant_b = False
ball_inside_1_quadrant = False
ball_inside_4_quadrant_b = 0
ball_inside_1_quadrant_o = 0

quadrant_yellow = 0

entry_yellow_time_enter = 0
entry_yellow_time = 0

exit_yellow_time = 0
colour_yellow = ""


conture_value_b = []
ball_in_b = 0
average_b = 0


text=''





while True:
    ctime = time.time()
    ctime = int(ctime-ptime)
    # print(ctime)
    success, video = webcam_video.read() # Reading webcam footage
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format
    text = str(ctime)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(video, text, (10, 100), font, 2.5, (255, 255, 255), 2)

# detecting for yellow ball
    mask_yellow = cv2.inRange(img, y_lower, y_upper)# Masking the image to find our color
    mask_orange = cv2.inRange(img, o_lower, o_upper)
    # print("mask_yellow",mask_yellow)
    mask_blue = cv2.inRange(img, b_lower, b_upper)
    mask_contours_y, hierarchy_y = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    mask_contours_o, hierarchy_o = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask_contours_b, hierarchy_b = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Finding position of all contours

#   for yellow
    if len(mask_contours_y) != 0:
        # print("ye")
        for mask_contour in mask_contours_y:
            if cv2.contourArea(mask_contour) > 500:
                # print('yes')
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle
                colour_yellow = "yellow"
                if (x>800 and x<1220) and (y>25 and y<500): # yellow in quadrant 3 and recording quadrant entry time color
                    if first_3_time_enable:
                        first_time_y_3= ctime
                        first_3_time_enable = 0
                        # print(first_time)
                    if (ctime - first_time_y_3) > 2:
                        entry_yellow_time = first_time_y_3
                        ball_inside_3_quadrant = True
                        quadrant_yellow = 3
                elif (x<800 or x>1220) and (y<25 or y>500) and ball_inside_3_quadrant: # logic for exit time
                    exit_yellow_time = ctime
                    ball_inside_3_quadrant = False
                    # first_time = 0
                    first_3_time_enable = 1
                    first_1_time_enable =1


                    list1 = [colour_yellow, entry_yellow_time, exit_yellow_time,quadrant_yellow]
                    print(list1)

                if (x > 1250 and x < 1730) and (y > 530 and y< 1000):  # yellow in quadrant 1
                    if first_1_time_enable:
                        first_time_y_1 = ctime
                        first_1_time_enable = 0
                        # print("enter")
                    if (x > 1250 and x < 1730) and (y > 530 and y < 1000) and ((ctime - first_time_y_1)>2): # logic for quadrant entry time
                        # print("first time y 1 ", first_time_y_1, ctime)
                        entry_yellow_time = first_time_y_1
                        quadrant_yellow = 1
                        ball_inside_1_quadrant = True
                        # print("for sure 1")
        # print("in")
    else:
        # first_time_y_1 = 0
        first_1_time_enable = 1
        if ball_inside_1_quadrant:
            ball_inside_1_quadrant = False
            exit_yellow_time = ctime
            list1 = [colour_yellow, entry_yellow_time, exit_yellow_time, quadrant_yellow]
            print(list1)





    # for blue
    if len(mask_contours_b) != 0:
        # print("in")
        for mask_contour_b in mask_contours_b:
        #     conture_value_b.append(int(cv2.contourArea(mask_contour_b)))
            # print(conture_value_b,len(conture_value_b),'before 15')
            # print(int(cv2.contourArea(mask_contour)))
            # print(conture_value_b)
            if cv2.contourArea(mask_contour_b) > 500:
                # print('yes')
                x, y, w, h = cv2.boundingRect(mask_contour_b)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle
        #         # print(x,y)
        #         # print("in")
                colour_blue = "blue"
                if (x>800 and x<1220) and (y>25 and y<500): # blue in quadrant 3 and recording quadrant entry time color
                    if first_3_time_enable_b:
                        first_time_b_3= ctime
                        first_3_time_enable_b = 0
                        # print(first_time_b_3)
                    if (ctime - first_time_b_3) > 2:
                        entry_blue_time = first_time_b_3
                        ball_inside_3_quadrant_b = True
                        quadrant_blue = 3
                elif (x<800 or x>1220) and (y<25 or y>500) and ball_inside_3_quadrant_b: # logic for exit time
                    exit_blue_time = ctime
                    ball_inside_3_quadrant_b = False
                    # first_time = 0
                    first_3_time_enable_b = 1
                    # first_1_time_enable =1
        # #
        # #
                    list_b = [colour_blue, entry_blue_time, exit_blue_time, quadrant_blue]
                    print(list_b)

                if (x > 1260 and x < 1730) and (y > 25 and y < 500):  # blue in quadrant 4 and recording quadrant entry time color
                    if first_4_time_enable_b:
                        first_time_b_4 = ctime
                        # print("ues")
                        first_4_time_enable_b = 0
                            # print(first_time_b_3)
                    if (ctime - first_time_b_4) > 2:
                        entry_blue_time = first_time_b_4
                        ball_inside_4_quadrant_b = True
                        quadrant_blue = 4
                elif ball_inside_4_quadrant_b:  # logic for exit time
                    exit_blue_time = ctime
                    ball_inside_4_quadrant_b = False
                    first_4_time_enable_b = 1
                    list_b_4 = [colour_blue, entry_blue_time, exit_blue_time, quadrant_blue]
                    print(list_b_4)

                # if (x > 800 and x < 1210) and (y > 530 and y < 1000):  # blue in quadrant 2
                #     # print("inside 2nd")
                #     if first_2_time_enable_b:
                #         first_time_y_2 = ctime
                #         first_2_time_enable_b = 0
                #         print("enter")
                #     if (ctime - first_time_y_2 > 3):  # logic for quadrant entry time
                #         # print("first time y 1 ", first_time_y_1, ctime)
                #         entry_blue_time = first_time_y_2
                #         quadrant_blue = 2
                #         ball_inside_2_quadrant_b = True
                #         print("for sure 2")
                #     print(ball_inside_2_quadrant_b)
                # elif ball_inside_2_quadrant_b:
                #     print('exit')
                    # ball_inside_2_quadrant_b = False

        # conture_value_b.clear()
    # # for orange
    # if len(mask_contours_o) != 0:
    #     # print(len(mask_contours_o))
    #     for mask_contour in mask_contours_o:
    #         if cv2.contourArea(mask_contour) > 500:
    #             # print(cv2.contourArea(mask_contour))
    #             x_o, y_o, w, h = cv2.boundingRect(mask_contour)
    #             # print("starting point",(x, y))
    #             # print("end point",(x + w, y + h))
    #             cv2.rectangle(video, (x_o, y_o), (x_o + w, y_o + h), (0, 0, 255), 3) #drawing rectangle
    #             colour_orange = "orange"
    #             if cv2.contourArea(mask_contour)>3000: # orange in quadrant 1 and recording quadrant entry time color
    #                 if first_1_time_enable_o:
    #                     first_time_o_1= ctime
    #                     first_1_time_enable_o = 0
    #                     # print("helo")
    #
    #                     # print(first_time_o_1)
    #                 if (ctime - first_time_o_1) > 2:
    #                     entry_orange_time = first_time_o_1
    #                     ball_inside_1_quadrant_o = True
    #                     quadrant_orange = 1
    #                     # print("orange in side quadrant 1")
    #                     # print("True")
    #             else :
    #                 # for 2 sec
    #
    #                 if ball_inside_1_quadrant_o:  # logic for exit time
    #                     exit_orange_time = ctime
    #                     # print("exit from quadrant 1")
    #                     ball_inside_1_quadrant_o = False
    #                     # first_time = 0
    #                     first_1_time_enable_o = 1
    #                     # first_1_time_enable =1
    #
    #                     list1_o = [colour_orange, entry_orange_time, exit_orange_time, quadrant_orange]
    #                     print(list1_o)
    #                     df = df.append(pd.DataFrame([list1_o], columns=df.columns), ignore_index=True)
    # quadrant_3 cordinate = (800, 25),(1220, 500)
    # quadrant_4 cordinate = (1260, 25),(1730, 500)
    # quadrant_2 cordinate = (800, 530),(1210, 1000)
    # quadrant_1 cordinate = (1250, 530),(1730, 1000)
    # cv2.rectangle(video,(800, 25),(1220, 500), (0, 0, 255), 3)  # drawing rectangle
    # cv2.rectangle(video,(1260, 25),(1730, 500),  (0, 0, 255), 3)  # drawing rectangle
    # cv2.rectangle(video,(790, 535),(1210, 1010),  (0, 0, 255), 3)  # drawing rectangle
    # cv2.line(video,(1250, 530),(1730, 1000),  (0, 0, 255), 3)  # drawing rectangle

    # center_coordinates = (1730, 1000)
    # radius = 10
    # color = (255, 255, 255)
    # image = cv2.circle(video, center_coordinates, radius, color)
    # cv2.imshow("mask image", mask_orange) # Displaying mask image

    cv2.imshow("My Window", video) # Displaying webcam image

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()