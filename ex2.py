import cv2

# 비디오 파일 경로
video_path = '3week/test_video.mp4'

# 비디오 파일 열기
cap = cv2.VideoCapture(video_path)

# 비디오가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print(f"비디오를 열 수 없습니다: {video_path}")
else:
    # 비디오 정보 출력
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"비디오 정보:")
    print(f"해상도: {width}x{height}")
    print(f"FPS: {fps}")
    print(f"총 프레임 수: {total_frames}")
    print("재생 중... (ESC 키를 누르면 종료)")
    
    # 비디오 재생
    while True:
        ret, frame = cap.read()
        
        # 프레임을 정상적으로 읽었는지 확인
        if not ret:
            print("비디오 재생 완료")
            break
        
        # 프레임 표시
        cv2.imshow('Video Player', frame)
        
        # ESC 키(27)를 누르면 종료
        if cv2.waitKey(1) & 0xFF == 27:
            print("재생 중지됨")
            break
    
    # 모든 창 닫기 및 리소스 해제
    cap.release()
    cv2.destroyAllWindows()

