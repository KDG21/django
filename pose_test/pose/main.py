import cv2
import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import shutil
import json
from pose.pose_check import Pose_Check

if __name__ == '__main__':
    pose = Pose_Check(
            'C:\\Users\\user\\PycharmProjects\\pythonProject\\openpose-master\\models\\pose\\coco\\pose_deploy_linevec.prototxt',
            'C:\\Users\\user\\PycharmProjects\\pythonProject\\openpose-master\\models\\pose\\coco\\pose_iter_440000.caffemodel',
        )

    #dnn gpu 가속 설정
    pose.set_gpu(gpu=True)


    #초당 한 프레임만 가져와서 저장하기 위한 코드
    n = 0
    idx = 0
    video = cv2.VideoCapture(video_file)
    name = 'frame'
    frame_path = 'C:\\Users\\user\\PycharmProjects\\pythonProject\\frames'
    converted_path = 'C:\\Users\\user\\PycharmProjects\\pythonProject\\new_img'

    #프레임 저장할 디렉토리 설정
    pose.set_dir(frame_path)

    #영상의 초당 프레임을 갖고옴
    FPS = int(video.get(cv2.CAP_PROP_FPS))

    #영상을 재생하면서 저장
    while (video.isOpened()):
        ret, frame = video.read()
        if ret == False:
            break
        n += 1
        idx += 1

        #1초의 마지막 프레임에서 프레임 저장
        if n == FPS:
            cv2.imwrite(frame_path + '/{}{}.jpg'.format(name, idx), frame)
            #판별 코드 초기화
            n = 0
        if cv2.waitKey(1) & 0xff == 27:
            break

    video.release()
    cv2.destroyAllWindows()


    pose.set_dir(converted_path)

    frame_list = pose.get_frame_list(frame_path, name)

    sh_count = []
    eye_count = []
    pel_count = []
    n = 0

    for i in frame_list:
        n += 1
        points, frame = pose.estimation(i)
        cv2.imwrite(i.replace(frame_path, converted_path),frame)
        # print(n,points)
        # print(n, points[2], points[5])
        shoulder = pose.isHorizontal(points[2], points[5])
        eye = pose.isHorizontal(points[14], points[15])
        sh_count.append(shoulder)
        eye_count.append(eye)
        # pelvis =pose.isVertical((points[8], points[9]), (points[11], points[12]))

        if pose.isVertical((points[8], points[9]), (points[11], points[12])) == None or pose.isHorizontal(points[8], points[11]) == None:
            pelvis = None
            pel_count.append(pelvis)
        elif pose.isVertical((points[8], points[9]), (points[11], points[12])) == 1 or pose.isHorizontal(points[8], points[11]) == 1:
            pelvis = 1
            pel_count.append(pelvis)
        else:
            pelvis = 0
            pel_count.append(pelvis)


    # 시각화를 위한 데이터프레임 변환
    sh_count = pd.Series(sh_count, name='sh_count', dtype='float32')
    pel_count = pd.Series(pel_count, name='pel_count', dtype='float32')
    eye_count = pd.Series(eye_count, name='eye_count', dtype='float32')
    all_count = pd.concat([sh_count, pel_count, eye_count], axis=1)

    pose_count = []

    for i in range(len(all_count)):
        if 1 in all_count.iloc[[i]].values:
            pose_count.append(1.0)
        elif 1 not in all_count.iloc[[i]].values and 0 in all_count.iloc[[i]].values:
            pose_count.append(0.0)
        elif all_count.iloc[[i]].all(None):
            pose_count.append(None)

    pose_count = pd.Series(pose_count, name='pose_count', dtype='float32')
    all_count = pd.concat([all_count, pose_count], axis=1)


    pose_json = {'result' : {
        'shoulder' : {
            'len' : len(all_count),
            'unbalance' : all_count['sh_count'].sum(),
            'none' : all_count['sh_count'].isnull().sum()
        },
        'pelvis': {
            'len': len(all_count),
            'unbalance': all_count['pel_count'].sum(),
            'none': all_count['pel_count'].isnull().sum()
        },
        'eye': {
            'len': len(all_count),
            'unbalance': all_count['eye_count'].sum(),
            'none': all_count['eye_count'].isnull().sum()
        },
        'all_pose': {
            'len': len(all_count),
            'unbalance': all_count['pose_count'].sum(),
            'none': all_count['pose_count'].isnull().sum()
        },
    }}
    pose_json = json.dumps(str(pose_json))

    pose.del_dir(frame_path)
    pose.del_dir(converted_path)
    pose.del_file(video_file)
