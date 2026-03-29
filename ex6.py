import cv2
import numpy as np

# 이미지 파일 경로
image_path = '3week/candies.png'

# 이미지 읽기
img = cv2.imread(image_path)

# 이미지가 정상적으로 읽혔는지 확인
if img is None:
    print(f"이미지를 읽을 수 없습니다: {image_path}")
else:
    # 이미지 정보 출력
    print(f"이미지 정보:")
    print(f"크기: {img.shape}")
    print(f"높이: {img.shape[0]}, 너비: {img.shape[1]}, 채널: {img.shape[2]}")
    
    # BGR을 HSV로 변환
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    print("\nHSV로 변환 완료")
    print("붉은색 영역 추출 중...")
    
    # 빨간색 범위 정의 (HSV에서 빨간색은 0~10, 170~180)
    lower_red1 = np.array([0, 100, 100])      # 낮은 범위 1
    upper_red1 = np.array([10, 255, 255])     # 높은 범위 1
    
    lower_red2 = np.array([170, 100, 100])    # 낮은 범위 2
    upper_red2 = np.array([180, 255, 255])    # 높은 범위 2
    
    # 빨간색 마스크 생성
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    
    # 두 마스크 합치기
    mask = cv2.bitwise_or(mask1, mask2)
    
    # 원본 이미지와 마스크를 사용하여 빨간색 영역만 추출
    red_result = cv2.bitwise_and(img, img, mask=mask)
    
    # 원본 이미지 표시
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    
    # 빨간색 마스크 표시
    cv2.imshow('Red Mask', mask)
    cv2.waitKey(0)
    
    # 붉은색 영역만 추출된 이미지 표시
    cv2.imshow('Red Region Extracted', red_result)
    cv2.waitKey(0)
    
    # 모든 창 닫기
    cv2.destroyAllWindows()
    
    print("붉은색 영역 추출 완료")

