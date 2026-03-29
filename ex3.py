import cv2

# 웹캠 열기 (0은 기본 웹캠)
cap = cv2.VideoCapture(0)

# 웹캠이 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다")
else:
    # 웹캠 정보 출력
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(f"웹캠 정보:")
    print(f"해상도: {width}x{height}")
    print(f"FPS: {fps}")
    print("웹캠 실행 중... (ESC 키를 누르면 종료)")
    
    # 웹캠 영상 표시
    while True:
        ret, frame = cap.read()
        
        # 프레임을 정상적으로 읽었는지 확인
        if not ret:
            print("웹캠 읽기 실패")
            break
        
        # 프레임 표시
        cv2.imshow('Webcam', frame)
        
        # ESC 키(27)를 누르면 종료
        if cv2.waitKey(1) & 0xFF == 27:
            print("웹캠 종료됨")
            break
    
    # 모든 창 닫기 및 리소스 해제
    cap.release()
    cv2.destroyAllWindows()

