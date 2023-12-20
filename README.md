# Calculator_PyQt
Calculator Practice based PyQt

## Goals
* github 저장소 생성 및 관리 실습
* PyQt5 기반 계산기 기능 및 사용방법 개선

## Getting started
* Python 3.x 버전이 설치
  * python3 --version 명령어를 입력하여 정상적으로 설치되었는지 확인
* PyQt5 모듈 설치
  * python -m pip install pyqt5
* 프로젝트를 로컬에 클론
  * git clone [GitHub 프로젝트 링크]
* 프로젝트 디렉토리로 이동
  * cd Calculator_PyQt
* 파이썬 파일 실행
  * python calculator_main.py

## Feature
* 기본적인 산술 연산 (+, -, *, /) 지원
* '=' 버튼을 누른 후에도 이전 연산을 유지하고 복수의 연산을 수행하는 기능
* 유효하지 않은 입력 및 0으로 나누는 경우에 대한 예외 처리
* 추가된 기능
이 계산기는 기본적인 산술 연산 기능 외에도 다음과 같은 추가 기능을 제공

  * C: 현재 입력된 모든 값을 지우는 기능을 수행
  * CE: 가장 최근에 입력된 숫자나 연산자를 지움.
  * x^2: 현재 입력된 숫자를 제곱하는 기능을 수행.
  * 1/x: 현재 입력된 숫자의 역수를 계산.
  * root: 현재 입력된 숫자의 제곱근을 계산.
  * %: 현재 입력된 숫자를 백분율로 변환.

## Project Construct
calculator_main.py: 메인 스크립트 파일로, 이 파일을 실행하여 계산기를 사용

## CONTRIBUTING
프로젝트에 기여하고 싶으신 분들은 언제든지 Pull Request를 보내주시길 바랍니다.  
이슈를 통해 문제점을 지적하거나 새로운 아이디어를 제안하셔도 좋습니다.

## LICENSE
* 이 프로젝트는 MIT 라이선스를 따릅니다.
