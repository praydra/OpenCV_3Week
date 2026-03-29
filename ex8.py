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
    
    # BGR을 RGB로 변환 (matplotlib용)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # R, G, B 채널 분리
    r, g, b = cv2.split(img_rgb)
    
    print("\nR, G, B 채널 분리 완료")
    print("각 채널의 히스토그램 계산 중...")
    
    # 각 채널의 히스토그램 계산
    hist_r = cv2.calcHist([img_rgb], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img_rgb], [1], None, [256], [0, 256])
    hist_b = cv2.calcHist([img_rgb], [2], None, [256], [0, 256])
    
    # 이미지와 히스토그램 표시
    plt.figure(figsize=(15, 10))
    
    # 원본 이미지 표시
    plt.subplot(2, 2, 1)
    plt.imshow(img_rgb)
    plt.title('Lenna - Original Image (RGB)')
    plt.axis('off')
    
    # Red 채널 히스토그램
    plt.subplot(2, 2, 2)
    plt.plot(hist_r, color='red', linewidth=2)
    plt.title('Red Channel Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    
    # Green 채널 히스토그램
    plt.subplot(2, 2, 3)
    plt.plot(hist_g, color='green', linewidth=2)
    plt.title('Green Channel Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    
    # Blue 채널 히스토그램
    plt.subplot(2, 2, 4)
    plt.plot(hist_b, color='blue', linewidth=2)
    plt.title('Blue Channel Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("R, G, B 채널 히스토그램 출력 완료")

