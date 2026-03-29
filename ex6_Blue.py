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
    print("파란색 영역 추출 중...")
    
    # 파란색 범위 정의 (HSV에서 파란색은 100~130)
    lower_blue = np.array([100, 100, 100])    # 낮은 범위
    upper_blue = np.array([130, 255, 255])    # 높은 범위
    
    # 파란색 마스크 생성
    mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    
    # 원본 이미지와 마스크를 사용하여 파란색 영역만 추출
    blue_result = cv2.bitwise_and(img, img, mask=mask)
    
    # 원본 이미지 표시
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    
    # 파란색 마스크 표시
    cv2.imshow('Blue Mask', mask)
    cv2.waitKey(0)
    
    # 파란색 영역만 추출된 이미지 표시
    cv2.imshow('Blue Region Extracted', blue_result)
    cv2.waitKey(0)
    
    # 모든 창 닫기
    cv2.destroyAllWindows()
    
    print("파란색 영역 추출 완료")

