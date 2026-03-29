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
    
    # BGR 채널 분리
    b, g, r = cv2.split(img)
    
    print("\n각 색 성분 표시 중...")
    
    # 원본 이미지 표시
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    
    # Blue 채널 표시
    cv2.imshow('Blue Channel', b)
    cv2.waitKey(0)
    
    # Green 채널 표시
    cv2.imshow('Green Channel', g)
    cv2.waitKey(0)
    
    # Red 채널 표시
    cv2.imshow('Red Channel', r)
    cv2.waitKey(0)
    
    # 모든 창 닫기
    cv2.destroyAllWindows()
    
    print("색 성분 출력 완료")

