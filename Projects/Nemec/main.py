import cv2
import numpy as np


class SimpleKalmanFilter:
    def __init__(self, mea_e, est_e, q):
        self.mea_e = mea_e
        self.est_e = est_e
        self.q = q

        self.kalman_gain = 0
        self.last_estimate = 0
        self.curr_estimate = 0
    
    def updateEstimate(self, mea):
        self.kalman_gain = self.est_e/(self.est_e + self.mea_e)
        self.curr_estimate = self.last_estimate + self.kalman_gain*(mea-self.last_estimate)
        self.est_e = (1-self.kalman_gain)*self.est_e+abs(self.last_estimate-self.curr_estimate)*self.q
        self.last_estimate = self.curr_estimate

        return self.curr_estimate

class SimpleKalmanFilter_2D:
    def __init__(self, mea_e, est_e, q):
        self.x = SimpleKalmanFilter(mea_e=mea_e,est_e=est_e,q=q)
        self.y = SimpleKalmanFilter(mea_e=mea_e,est_e=est_e,q=q)
    def updateEstimate(self, mea):
        mea[0] = self.x.updateEstimate(mea[0])
        mea[1] = self.y.updateEstimate(mea[1])
        return mea

def distance(p1, p2):
    return np.sqrt(pow(p1[0]-p2[0],2) + pow(p1[1]-p2[1],2))

def rotz(a):
    return np.matrix([[np.cos(a), -np.sin(a), 0],
                      [np.sin(a),  np.cos(a), 0],
                      [        0,          0, 1]])

def points_in_rect(points, rect, center, angle):
    n = len(points)
    rot_matrix = rotz(np.deg2rad(-angle))

    rect = np.vstack([np.matrix(rect).transpose(), np.zeros([1,4])])
    points = np.vstack([np.matrix(points).transpose(), np.zeros([1,n])])

    rect_r = rot_matrix.dot(np.matrix(rect))[0:2,:]
    points_r = rot_matrix.dot(np.matrix(points))[0:2,:]

    x_min, x_max = np.min(rect_r[0,:]), np.max(rect_r[0,:])  
    y_min, y_max = np.min(rect_r[1,:]), np.max(rect_r[1,:])

    new_points = np.zeros([2, n])

    counter = 0
    for i in range(n):
        xx = points_r[0,i]
        yy = points_r[1,i]
        if (xx > x_min) and (xx < x_max):
            if (yy > y_min) and (yy < y_max):
                new_points[:,counter] = np.array([points[0,i],points[1,i]])
                counter+=1

    if counter != 0:
        coords = [np.mean([np.max(new_points[0,0:counter]),np.min(new_points[0,0:counter])]), np.mean([np.max(new_points[1,0:counter]),np.min(new_points[1,0:counter])])]
    else:
        coords = None

    return new_points[:,0:counter].transpose(), counter, coords


def main():
    hueLower, hueUpper = 0, 50 # in range 0-179 - First part of Hue - it does contains red
    hueLower2, hueUpper2 = 63, 179 # in range 0-179 - Second part of Hue - filtering out part of green

    saturationLower, saturationUpper = 0, 121 # in range 0-255 - I need mostly faded colors, white, grey, etc
    valueLower, valueUpper = 165, 255 # in range 0-255 - I need mostly white grey to white color

    kernel_size = 18 # Best value so far for convolution and blurring the background noise
    greyscale_treshold = 179 # in range 0-255 - Treshold for fully removing background noise

    # Uncomment for live video feed from RPi Camera
    # dispW = 640
    # dispH = 480
    # flip=2
    # camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
    # cam = cv2.VideoCapture(camSet)
    cam = cv2.VideoCapture("video_cap3.mp4")

    background_mask_hsv = cv2.imread("background_hsv.png")
    background_mask_hsv= cv2.cvtColor(background_mask_hsv, cv2.COLOR_BGR2GRAY)

    filter_2d_p1 = SimpleKalmanFilter_2D(1, 1, 0.15)
    filter_2d_p3 = SimpleKalmanFilter_2D(1, 1, 0.15)

    prev_p1 = [0, 0]
    prev_coord1 = [0, 0]
    prev_center = [0, 0]

    counter = 0
    while True:
        counter+=1
        # try - except - only for infinite reloading of video in case of videotape
        try:
            ret, frame = cam.read()
            frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        except:
            cam = cv2.VideoCapture('video_cap3.mp4')
            ret, frame = cam.read()
            frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            counter = 1

        HSV_settings_lower = np.array([hueLower,saturationLower,valueLower])
        HSV_settings_upper = np.array([hueUpper,saturationUpper,valueUpper])
    
        HSV_settings_lower_2 = np.array([hueLower2,saturationLower,valueLower])
        HSV_settings_higher_2 = np.array([hueUpper2,saturationUpper,valueUpper])

        HSV_mask = cv2.inRange(frame_hsv, HSV_settings_lower, HSV_settings_upper)
        HSV_mask2 = cv2.inRange(frame_hsv, HSV_settings_lower_2, HSV_settings_higher_2)
        HSV_mask_final = cv2.add(HSV_mask, HSV_mask2) # First masek made from HSV
        cv2.imshow('HSV_mask', HSV_mask_final)
        cv2.moveWindow('HSV_mask', 640, 0)
        HSV_mask_final = cv2.subtract(HSV_mask_final, background_mask_hsv) # Mask without background
        cv2.imshow('HSV_mask_no_background', HSV_mask_final)
        cv2.moveWindow('HSV_mask_no_background', 640*2, 0)
        HSV_mask_final = cv2.blur(HSV_mask_final, (kernel_size, kernel_size)) # blurring the mask to blur the noise
        cv2.imshow('HSV_mask_blurred', HSV_mask_final)
        cv2.moveWindow('HSV_mask_blurred', 0, 520)
        ret, HSV_mask_final = cv2.threshold(HSV_mask_final, greyscale_treshold, 255, cv2.THRESH_BINARY) # Removing all the blurred noise
        cv2.imshow('final_mask', HSV_mask_final)
        cv2.moveWindow('final_mask', 640, 520)

        contours, _ = cv2.findContours(HSV_mask_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area >= 500 and area <= 4000:
                cv2.drawContours(frame,[cnt],0,(0,0,255),1)

                rows, cols = frame.shape[:2]
                [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.05,0.05)
                lefty = int(((-x*vy/vx) + y))
                righty = int((((cols-x)*vy/vx)+y))
                cv2.line(frame, (cols-1,righty), (0, lefty), (255,0,0), 1)

                k = 100
                p1 = [int(-vx*k+x), int(-vy*k+y)]
                p2 = [int( vx*k+x), int( vy*k+y)]

                diff = np.sqrt(pow(p1[0]-prev_p1[0],2) + pow(p1[1]-prev_p1[1],2))
                if 2*k-20 < diff:
                    p1, p2 = p2,p1
                
                prev_p1 = p1
                
                cv2.circle(frame,tuple(np.int0(p1)),5,(0,255,0),2)
                cv2.circle(frame,tuple(np.int0(p2)),5,(0,0,255),2)
                cv2.line(frame,tuple(np.int0(p1)),tuple(np.int0(p2)),(255,0,0),2)
                
                
                (center, shape, angle) = cv2.minAreaRect(cnt)
                minAreaBox = cv2.boxPoints((center, shape, angle))
                minAreaBox = np.int0(minAreaBox)
                cv2.drawContours(frame,[minAreaBox],0,(255,0,0),1)

                if shape[0] > shape[1]:
                    side_shape = (shape[1], shape[0])
                    angle2 = angle-90
                else:
                    angle2 = angle
                    side_shape = shape

                center_x = np.cos(np.deg2rad(angle2+90)) * (side_shape[1]/2*0.9)
                center_y = np.sin(np.deg2rad(angle2+90)) * (side_shape[1]/2*0.9)

                c1 = [ center_x+center[0],  center_y + center[1]]
                c3 = [-center_x+center[0], -center_y + center[1]]

                # Simple check if the points have swapped.
                diff_coord1 = distance(c1, prev_coord1)
                if  diff_coord1 > 50:
                    c1, c3 = c3, c1                       

                prev_coord1 = c1

                middle_shape = (side_shape[0]*1.1, side_shape[1]*0.3)
                side_shape = (side_shape[0]*1.1, side_shape[1]*0.15)
                
                # Determination of the curvature.
                box1 = cv2.boxPoints((c1, side_shape, angle2))
                box2 = cv2.boxPoints((center, middle_shape, angle2))
                box3 = cv2.boxPoints((c3, side_shape, angle2))

                # Determination of position of tail, head and middle of body. 
                points1, counter1, coord1 = points_in_rect(cnt, box1, c1, angle2)
                points2, counter2, coord2 = points_in_rect(cnt, box2, center, angle2)
                points3, counter3, coord3 = points_in_rect(cnt, box3, c3, angle2)

                box1 = np.int0(box1)
                box2 = np.int0(box2)
                box3 = np.int0(box3)

                cv2.drawContours(frame,[box1],0,(0,0,255),2)
                cv2.drawContours(frame,[box2],0,(255,0,0),2)
                cv2.drawContours(frame,[box3],0,(0,255,0),2)

                # Arrow line of movement, is not very much visible. Would be used for determination where of dog's direction
                # arrow_px = center[0] + (-prev_center[0] + center[0]) * 20
                # arrow_py = center[1] + (-prev_center[1] + center[1]) * 20
                # cv2.line(frame, np.int0(center), np.int0([arrow_px, arrow_py]),(255,0,0), 2)
                # prev_center = center

                if counter1 > 0 and counter2 > 0 and counter3 > 0:

                    cv2.drawContours(frame,[np.int0(points1)],0,(0,0,255),2)
                    cv2.drawContours(frame,[np.int0(points2)],0,(255,0,0),2)
                    cv2.drawContours(frame,[np.int0(points3)],0,(0,255,0),2)

                    coord1[0] = coord1[0] + (-coord2[0] + coord1[0])*1.2
                    coord1[1] = coord1[1] + (-coord2[1] + coord1[1])*1.2

                    coord3[0] = coord3[0] + (-coord2[0] + coord3[0])*1.2
                    coord3[1] = coord3[1] + (-coord2[1] + coord3[1])*1.2

                    cv2.line(frame, tuple(np.int0(coord2)), tuple(np.int0(coord1)), (0,0,255), 2)
                    cv2.line(frame, tuple(np.int0(coord2)), tuple(np.int0(coord3)), (0,255,0), 2)

                    coord1 = filter_2d_p1.updateEstimate(coord1)
                    coord3 = filter_2d_p3.updateEstimate(coord3)
                    
                    # Drawing the points in direaction of tail and head. Probably should by better with circle from 3 points
                    # and its intersection with circle from middle point.
                    cv2.circle(frame, tuple(np.int0(coord1)), 5, (0,0,255), 2)
                    cv2.circle(frame, tuple(np.int0(coord3)), 5, (0,255,0), 2)

                break
        
        cv2.imshow('Final_frame', frame)
        cv2.moveWindow('Final_frame',0,0)

        if cv2.waitKey(1)==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()