# OpenCV 영상 처리 기초

OpenCV로 이미지와 영상 입출력, 색 공간 변환, 색상 검출, 히스토그램, 필터링, 에지 검출을 구현한 예제 모음입니다.

## 데이터

- 이미지: `3week/` 폴더의 `Lenna.png`, `apple.png`, `candies.png`, `Hawkes.jpg`, `desert.JPG`, `mountain.jpg` (최상위 폴더에도 같은 파일이 있습니다)
- 동영상: `3week/test_video.vol1.egg`, `vol2.egg` (분할 압축, 반디집 등으로 압축 해제)

## 소스 구성

| 파일 | 내용 | 주요 함수 |
| --- | --- | --- |
| `ex1.py`, `ex1_grayscale.py` | 이미지 읽기, 그레이스케일 변환 | `imread`, `cvtColor` |
| `ex2.py` | 동영상 파일 재생 | `VideoCapture` |
| `ex3.py` | 웹캠 영상 출력 | `VideoCapture(0)` |
| `ex4.py` | BGR 채널 분리 | `split` |
| `ex5.py` | HSV 색 공간 변환 및 채널 분리 | `cvtColor`, `split` |
| `ex5_YUV.py` | YUV 색 공간 변환 | `cvtColor`, `split` |
| `ex6.py`, `ex6_Blue.py` | 특정 색상(빨강/파랑) 영역 검출 | `inRange` |
| `ex7.py`, `ex8.py` | 히스토그램 계산 및 시각화 | `calcHist` |
| `ex9.py` | 가우시안 블러, Canny 에지 검출 | `GaussianBlur`, `Canny` |

## 실행 방법

```bash
pip install opencv-python numpy matplotlib
python ex1.py
```

이미지와 동영상은 상대 경로 `3week/...`로 읽습니다. `OpenCV_3Week` 폴더에서 실행하세요.
