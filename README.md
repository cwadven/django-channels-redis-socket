<code><img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/></code>
<code><img src="https://img.shields.io/badge/redis%20-%23CC342D.svg?&style=for-the-badge&logo=redis&logoColor=white"/></code>

# 웹 소켓 이용하여 알림 기능 구현 (Channel, WebSocket)

<img alt="inside" src="https://github.com/cwadven/django-channels-redis-socket/blob/master/assets/dj_channels.jpg" />

# 구축 방법

**1. 가상환경 생성**
> python -m venv 가상환경이름

---

**2. 가상환경 실행**
> source 가상환경이름/bin/activate (가상환경 실행)

(Windows : source 가상환경이름/Script/activate)

---

**3. 필요한 모듈 가상환경에 설치**
> pip install -r requirements.txt

---

**4. Redis 서버 설치**
> 설치 방법

(Linux)

https://redis.io/topics/quickstart

(Windows)

https://github.com/tporadowski/redis/releases

---

**5. Redis 실행**

(Linux)

> redis-server

(Windows)

Redis 설치한 곳 Programfiles의 Redis에서 파일 실행

> redis-server.exe

---

**6. WAS 테스트 서버 실행**
> python manage.py runserver 0.0.0.0:8000

---

**7. websocket 연결되어있는 페이지**
> http://my.computer.host.ip/alarm

<img alt="outside" src="https://github.com/cwadven/django-channels-redis-socket/blob/master/assets/toast_popup.png" />

---

**8. receiver에 적용되어있는 websocket 전송 보내는 이벤트**
> http://my.computer.host.ip/send

<img alt="inside" src="https://github.com/cwadven/django-channels-redis-socket/blob/master/assets/button_receiver.png" />