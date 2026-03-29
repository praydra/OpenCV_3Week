import cv2
import numpy as np
import matplotlib.pyplot as plt

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
    
    # BGR을 그레이스케일로 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    print("\n그레이스케일로 변환 완료")
    print("히스토그램 계산 중...")
    
    # 히스토그램 계산
    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
    
    # 이미지와 히스토그램 표시
    plt.figure(figsize=(12, 5))
    
    # 원본 이미지 표시 (그레이스케일)
    plt.subplot(1, 2, 1)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Lenna - Grayscale')
    plt.axis('off')
    
    # 히스토그램 표시
    plt.subplot(1, 2, 2)
    plt.plot(hist, color='black')
    plt.title('Histogram (Grayscale)')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    
    plt.tight_layout()
    plt.show()
    
    print("히스토그램 출력 완료")

