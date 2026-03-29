import cv2
import numpy as np

# 이미지 파일 경로
image_path = '3week/desert.jpg'

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
    
    # BGR을 그레이스케일로 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    print("\n그레이스케일로 변환 완료")
    print("엣지 추출 중...")
    
    # 가우시안 블러 적용 (노이즈 제거)
    blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
    
    # Canny 엣지 검출
    edges = cv2.Canny(blurred, 50, 150)
    
    # 원본 이미지 표시
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    
    # 그레이스케일 이미지 표시
    cv2.imshow('Grayscale Image', gray_img)
    cv2.waitKey(0)
    
    # 엣지 추출 결과 표시
    cv2.imshow('Edges Detected', edges)
    cv2.waitKey(0)
    
    # 모든 창 닫기
    cv2.destroyAllWindows()
    
    print("엣지 추출 완료")

