import cv2

# 이미지 파일 경로
image_path = '3week/Lenna.png'

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
    
    # HSV 채널 분리
    h, s, v = cv2.split(hsv_img)
    
    print("\nHSV 색상 모델로 변환 완료")
    print("각 성분 표시 중...")
    
    # 원본 이미지 표시
    cv2.imshow('Original Image (BGR)', img)
    cv2.waitKey(0)
    
    # Hue 채널 표시
    cv2.imshow('Hue Channel', h)
    cv2.waitKey(0)
    
    # Saturation 채널 표시
    cv2.imshow('Saturation Channel', s)
    cv2.waitKey(0)
    
    # Value 채널 표시
    cv2.imshow('Value Channel', v)
    cv2.waitKey(0)
    
    # 모든 창 닫기
    cv2.destroyAllWindows()
    
    print("HSV 성분 출력 완료")

