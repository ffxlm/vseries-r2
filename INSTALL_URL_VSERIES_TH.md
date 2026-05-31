# คู่มือย้ายและเปิดใช้งาน URL-VSeries

อัปเดตล่าสุด: 2026-05-23

โปรเจกต์นี้เป็นระบบจัดการงานวิดีโอ/รูปภาพสำหรับ VSeries ใช้ Python Flask, MongoDB, Cloudflare/R2 และ deploy ได้ด้วย Docker/Render

โครงสร้างหลัก:

```text
URL-VSeries/
  series_manager/
  templates/
  utils/
  app.py
  start.py
  run_worker.py
  requirements.txt
  Dockerfile
  render.yaml
  .env
  .gitignore
  .dockerignore
```

## 1. สิ่งที่ต้องติดตั้งบนเครื่องใหม่

ติดตั้งสิ่งเหล่านี้ก่อน:

1. Python 3.11 หรือใกล้เคียง
2. pip
3. ffmpeg
4. Internet สำหรับติดตั้ง package และเชื่อมต่อ MongoDB/Cloudflare

ตรวจเวอร์ชัน:

```bat
python --version
pip --version
ffmpeg -version
```

## 2. ติดตั้ง dependency

แนะนำให้ใช้ virtual environment:

```bat
cd /d C:\URL-VSeries
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

ถ้าไม่ใช้ virtual environment ก็รัน:

```bat
cd /d C:\URL-VSeries
pip install -r requirements.txt
```

## 3. ไฟล์ environment

โปรเจกต์ใช้ไฟล์:

```text
.env
```

ค่าหลักที่ต้องมี:

```env
MONGODB_URI=mongodb+srv://...
PORT=10000
```

ค่าอื่นที่ระบบอาจใช้:

```env
MONGODB_DB=url_series
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_secure_password
UPLOAD_FOLDER=data/uploads
MAX_UPLOAD_BYTES=16777216
START_EMBEDDED_WORKER=true
```

หมายเหตุ:

- `.env` มี secret และไม่ควร commit ขึ้น Git
- ตอน deploy ให้ตั้งค่า env ใน Render หรือระบบ hosting โดยตรง
- ถ้าต้องการล็อกหน้าเว็บด้วย Basic Auth ให้ตั้ง `ADMIN_USERNAME` และ `ADMIN_PASSWORD`

## 4. เปิดใช้งานแบบ local

เปิดเว็บและ worker ใน process เดียว:

```bat
cd /d C:\URL-VSeries
.venv\Scripts\activate
python app.py
```

แล้วเปิด:

```text
http://localhost:10000
```

ถ้าต้องการรันแบบใกล้ production ที่แยก web และ worker:

```bat
cd /d C:\URL-VSeries
.venv\Scripts\activate
python start.py
```

หมายเหตุบน Windows: `start.py` เรียก `gunicorn` ซึ่งเหมาะกับ Linux/Render มากกว่า ถ้ารันบน Windows แล้วติดปัญหา ให้ใช้ `python app.py` สำหรับ local test

## 5. Deploy ด้วย Render

โปรเจกต์มี `Dockerfile` และ `render.yaml` แล้ว จึง deploy เป็น Docker service ได้

สิ่งที่ต้องตั้งใน Render:

- `MONGODB_URI`
- `MONGODB_DB` ถ้าไม่ใช้ค่า default `url_series`
- `ADMIN_USERNAME` และ `ADMIN_PASSWORD` ถ้าต้องการล็อกหน้าเว็บ
- ค่า Cloudflare/R2 ที่ระบบตั้งค่าผ่านหน้า Settings หรือ env ตามที่ใช้งานจริง

Render จะใช้:

```text
Dockerfile
render.yaml
python start.py
```

## 6. ถ้าจะนำขึ้น Git

ไฟล์ `.gitignore` ถูกตั้งไว้ให้กันไฟล์สำคัญแล้ว เช่น:

- `.env`
- `data/`
- `__pycache__/`
- `.venv/`
- cache Python

เริ่ม Git ใหม่:

```bat
cd /d C:\URL-VSeries
git init
git add .
git status
git commit -m "Initial URL-VSeries project"
```

ก่อน commit ให้ตรวจ `git status` ว่าไม่มี `.env` อยู่ในรายการที่จะ commit

## 7. ไฟล์/โฟลเดอร์ที่สร้างใหม่ได้

ระบบอาจสร้างไฟล์หรือโฟลเดอร์เหล่านี้เอง:

```text
data/
data/uploads/
__pycache__/
```

ไม่จำเป็นต้องส่งขึ้น Git และไม่จำเป็นต้องอยู่ใน ZIP สำหรับ deploy

## 8. สรุปแบบเร็ว

```bat
cd /d C:\URL-VSeries
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

เปิด:

```text
http://localhost:10000
```
