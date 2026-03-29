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
    
    # BGR을 YUV로 변환
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    
    # YUV 채널 분리
    y, u, v = cv2.split(yuv_img)
    
    print("\nYUV 색상 모델로 변환 완료")
    print("각 성분 표시 중...")
    
    # 원본 이미지 표시
    cv2.imshow('Original Image (BGR)', img)
    cv2.waitKey(0)
    
    # Y 채널 표시 (밝기 성분)
    cv2.imshow('Y Channel (Luminance)', y)
    cv2.waitKey(0)
    
    # U 채널 표시 (색차 - 파란색)
    cv2.imshow('U Channel (Chrominance Blue)', u)
    cv2.waitKey(0)
    
    # V 채널 표시 (색차 - 빨간색)
    cv2.imshow('V Channel (Chrominance Red)', v)
    cv2.waitKey(0)
    
    # 모든 창 닫기
    cv2.destroyAllWindows()
    
    print("YUV 성분 출력 완료")

