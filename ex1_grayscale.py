import cv2

# 이미지 파일 경로
image_path = '3week/Lenna.png'

# 이미지 읽기
img = cv2.imread(image_path)

# 이미지가 정상적으로 읽혔는지 확인
if img is None:
    print(f"이미지를 읽을 수 없습니다: {image_path}")
else:
    # 컬러 이미지를 흑백으로 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 흑백 이미지 표시
    cv2.imshow('Lenna - Grayscale', gray_img)
    
    # 아무 키를 누를 때까지 대기
    cv2.waitKey(0)
    
    # 모든 창 닫기
    cv2.destroyAllWindows()
    
    print("이미지 표시 완료")

