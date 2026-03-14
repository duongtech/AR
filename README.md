# HỌC LIỆU SỐ AR – AR Science Lab
### Khóa luận tốt nghiệp · Đại học Sư Phạm – Đại học Đà Nẵng

> **Tác giả:** Lê Thị Khánh Linh &nbsp;|&nbsp; **MSSV:** 3220122138 &nbsp;|&nbsp; **Năm:** 2025–2026

---

## 1. Giới thiệu dự án

**AR Science Lab** là bộ học liệu số tương tác phục vụ môn **Tự Nhiên và Xã Hội lớp 3**. Toàn bộ ứng dụng chạy trực tiếp trên trình duyệt web — không cần cài đặt, không cần plugin — thông qua các công nghệ web hiện đại như **Three.js / WebGL** để mô phỏng không gian 3D.

Hệ thống gồm **1 trang chủ** và **4 mô-đun học tập** (AR1 → AR4), mỗi mô-đun tập trung vào một chủ đề khoa học khác nhau, tích hợp hoạt động tương tác, câu hỏi, và mini-game nhằm tăng tính hấp dẫn cho học sinh.

---

## 2. Cấu trúc thư mục

```
AR/
├── index.html              # Redirect về trang chủ
├── HOME/NEW/               # Trang chủ (Landing page)
│   ├── index.html
│   ├── assets/             # CSS/JS của template Massively
│   └── images/             # Ảnh minh họa các mô-đun
├── AR1/                    # Mô-đun 01: Chuyển Động Mặt Trời
│   └── index.html
├── AR2/                    # Mô-đun 02: Hệ Mặt Trời 3D
│   └── index.html
├── AR3/                    # Mô-đun 03: Bản Đồ Châu Lục & Đại Dương
│   ├── index.html
│   └── worldHigh.svg       # Bản đồ thế giới SVG độ phân giải cao
├── AR4/                    # Mô-đun 04: Đới Khí Hậu Trái Đất
│   ├── index.html
│   └── image/              # Ảnh minh họa các đới khí hậu
└── BT/                     # Bài tập bổ sung (file .docx)
```

---

## 3. Công nghệ sử dụng

### 3.1. HTML5

HTML5 là ngôn ngữ đánh dấu siêu văn bản thế hệ thứ 5, được dùng để xây dựng toàn bộ cấu trúc giao diện của từng mô-đun. Các thẻ ngữ nghĩa như `<canvas>`, `<section>`, `<article>`, `<nav>` được sử dụng xuyên suốt. Thẻ `<canvas>` đặc biệt quan trọng — đây là nơi Three.js vẽ toàn bộ đồ họa 3D.

Ngoài ra, các tính năng HTML5 như **Drag & Drop API** (dùng trong AR3, AR4), **Input Range** (thanh thời gian trong AR1), và **Import Maps** (quản lý module ES6) đều được khai thác triệt để mà không cần thư viện bên ngoài.

### 3.2. CSS3

CSS3 đảm nhận toàn bộ phần giao diện và hiệu ứng trực quan. Các kỹ thuật nổi bật được sử dụng:

- **Glassmorphism** (`backdrop-filter: blur()`, `rgba()`) cho các panel thông tin, thanh điều khiển nổi trên nền 3D.
- **CSS Animations & Keyframes** — hiệu ứng glow bản đồ (`glowNA`, `glowAS`...), pulsating logo, xoay vòng quỹ đạo, ripple khi nhấn nút.
- **CSS Grid & Flexbox** bố cục responsive, tương thích màn hình máy tính bảng.
- **Custom Properties / Variables** quản lý bộ màu thống nhất theo từng chủ đề.

Font chữ tải từ **Google Fonts** (`Inter`) cho giao diện hiện đại, sắc nét.

### 3.3. JavaScript (ES6+)

JavaScript thuần (Vanilla JS) được dùng hoàn toàn — không có framework như React hay Vue. Toàn bộ logic ứng dụng viết theo chuẩn **ES Modules (`type="module"`)**, bao gồm:

- Mô phỏng vật lý (góc cao Mặt Trời, bóng gnomon, quỹ đạo hành tinh).
- Logic game (đoán câu hỏi, kéo thả, đếm giờ, bảng xếp hạng).
- Điều phối camera, animation vòng lặp (`requestAnimationFrame`).
- Touch events hỗ trợ thiết bị di động.
- **Import Maps** khai báo đường dẫn `three` và `three/addons/` từ CDN, cho phép `import * as THREE from 'three'` mà không cần bundler.

### 3.4. Three.js (v0.160.0)

Three.js là thư viện JavaScript mã nguồn mở giúp tạo đồ họa 3D trên trình duyệt thông qua WebGL. Đây là **công nghệ cốt lõi** của toàn bộ dự án.

**Các tính năng Three.js được sử dụng:**

| Tính năng | Ứng dụng trong dự án |
|---|---|
| `WebGLRenderer` | Engine render toàn bộ cảnh 3D |
| `PerspectiveCamera` | Góc nhìn phối cảnh, zoom linh hoạt |
| `OrbitControls` | Kéo xoay, zoom bằng chuột/cảm ứng |
| `SphereGeometry` | Tạo Mặt Trời, Trái Đất, các hành tinh, bầu trời |
| `DirectionalLight` | Ánh sáng Mặt Trời chiếu bóng (PCFSoftShadowMap) |
| `Sprite / SpriteMaterial` | Hiệu ứng glow hào quang Mặt Trời |
| `CanvasTexture` | Tạo texture động (nhãn tên, glow dải màu) |
| `BufferGeometry / Line` | Vẽ quỹ đạo hành tinh, đường cung Mặt Trời |
| `ShaderMaterial` | Dải màu đới khí hậu trên Trái Đất (AR4) |
| `Raycaster` | Phát hiện click/touch vào vật thể 3D |
| `AnimationMixer` | Vòng lặp render mượt mà theo `requestAnimationFrame` |

### 3.5. WebGL

WebGL (Web Graphics Library) là API cấp thấp cho phép trình duyệt truy cập GPU để vẽ đồ họa 2D/3D. Three.js hoạt động hoàn toàn trên nền WebGL — người dùng không cần tương tác trực tiếp với WebGL, nhưng toàn bộ hiệu năng 3D mượt mà của dự án đến từ khả năng tăng tốc phần cứng của WebGL.

### 3.6. SVG (Scalable Vector Graphics)

Module AR3 sử dụng file `worldHigh.svg` — bản đồ thế giới vector độ phân giải cao dựa trên lưới chiếu **Mercator của amCharts**. JavaScript tải và inline SVG vào DOM, sau đó tô màu từng `<path>` theo code quốc gia (ISO 3166-1 alpha-2) để phân biệt các châu lục bằng màu sắc. Khu vực kéo thả được xếp chồng lên SVG bằng CSS position tuyệt đối theo phần trăm.

### 3.7. Template Massively (HTML5 UP)

Trang chủ (`HOME/NEW/index.html`) sử dụng template **Massively** của [HTML5 UP](https://html5up.net) — một giao diện đẹp, tối, dạng blog/portfolio. Template này cung cấp layout nền, navigation, và font icon Font Awesome. Nội dung được tùy biến hoàn toàn để phù hợp với bộ học liệu AR.

---

## 4. Các mô-đun học tập

### 4.1. AR1 – Chuyển Động Mặt Trời ☀️

Mô phỏng 3D quỹ đạo Mặt Trời theo 3 mùa (Xuân/Thu phân, Hạ chí, Đông chí). Người dùng điều chỉnh thời gian trong ngày (6:00–18:00) qua thanh timeline để quan sát góc cao Mặt Trời, hướng và chiều dài bóng gnomon thay đổi theo thời gian. Tích hợp bảng câu hỏi có 2 loại: **trắc nghiệm** và **kéo thả** (drag-challenge).

**Tính năng nổi bật:**
- Bầu trời động tô màu theo độ cao Mặt Trời (bình minh → trưa → hoàng hôn)
- La bàn SVG hiển thị hướng Mặt Trời và hướng bóng real-time
- Hệ thống quiz 6 câu, theo dõi điểm, phản hồi tức thì

### 4.2. AR2 – Hệ Mặt Trời 3D 🌌

Mô phỏng 8 hành tinh quay quanh Mặt Trời với tốc độ, khoảng cách và tỉ lệ tùy chỉnh. Hỗ trợ hai chế độ kích thước: **phóng đại** (dễ nhìn) và **tương đối thật**. Nhấp vào hành tinh để xem thông tin chi tiết (khoảng cách, chu kỳ, sự kiện thú vị). Có chế độ "Chuyến bay vũ trụ" (Space Tour) tự động di chuyển camera đến từng hành tinh.

**Tính năng nổi bật:**
- Vành đai Sao Thổ bằng `RingGeometry`
- Chế độ Ban ngày/Ban đêm chuyển đổi màu nền
- Bảng so sánh hành tinh dạng bảng (sidebar)
- Quiz 5 câu tích hợp, camera tự động hướng về hành tinh liên quan

### 4.3. AR3 – Bản Đồ Châu Lục & Đại Dương 🌍

Trò chơi kéo thả nhận diện 7 châu lục và 4 đại dương trên bản đồ thế giới thật (SVG). Hỗ trợ đầy đủ cả **Desktop (Drag & Drop API)** và **Mobile (Touch Events)**. Khi kéo đúng, các đường bờ biển của châu lục phát sáng theo màu đặc trưng (glow animation). Khi kéo sai, vùng thả rung lắc và hiện phản hồi.

**Tính năng nổi bật:**
- Bản đồ thật SVG 180+ quốc gia tô màu theo châu lục
- Toast thông báo kết quả từng lần thả
- Banner chúc mừng khi hoàn thành toàn bộ

### 4.4. AR4 – Đới Khí Hậu Trái Đất 🌏

Địa Cầu 3D hiển thị 5 đới khí hậu bằng các dải màu. Nhấp vào từng đới để xem thông tin (vị trí, đặc điểm, ảnh minh họa). Tích hợp hệ thống **8 mini-game** học tập phong phú.

**8 Mini-games:**

| # | Tên game | Mô tả |
|---|---|---|
| 1 | Đoán Quốc Gia ở Đới Nào | Nhấp đúng đới khí hậu của quốc gia được hỏi |
| 2 | Tìm Đúng Vị Trí | Click vào đới khí hậu khi được gọi tên |
| 3 | Gắn Nhãn Khí Hậu | Kéo nhãn tên đới dán lên Trái Đất 3D |
| 4 | Nhanh Tay Nhanh Mắt | Phản xạ 5 giây tìm đúng đới |
| 5 | Đấu Trường Lớp Học | Thi đấu 5 câu, ghi tên lên bảng xếp hạng |
| 6 | Đoán Đới Của Nước | Câu hỏi sâu hơn về đặc trưng từng nước |
| 7 | Xếp Đúng Thứ Tự | Kéo sắp xếp đới từ cực đến xích đạo |
| 8 | Nhận Biết Ảnh Đới | Xem ảnh thực tế, chọn đúng đới khí hậu |

---

## 5. Kiến trúc kỹ thuật tổng quan

```
┌─────────────────────────────────────────────────────┐
│                  TRÌNH DUYỆT WEB                    │
│                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────────────┐│
│  │  HTML5   │   │   CSS3   │   │   JavaScript ES6 ││
│  │ Structure│   │  Style   │   │     Logic        ││
│  └────┬─────┘   └────┬─────┘   └────────┬─────────┘│
│       │              │                   │           │
│       └──────────────┼───────────────────┘           │
│                      │                               │
│              ┌───────▼───────┐                       │
│              │   Three.js    │                       │
│              │  (v0.160.0)   │                       │
│              └───────┬───────┘                       │
│                      │                               │
│              ┌───────▼───────┐                       │
│              │     WebGL     │  ← GPU Acceleration   │
│              └───────────────┘                       │
└─────────────────────────────────────────────────────┘
```

**Điểm đặc biệt về kiến trúc:**
- **Zero-dependency** ngoại trừ Three.js — không dùng bundler (Webpack/Vite), không cần Node.js để chạy.
- **Import Maps** cho phép dùng cú pháp `import from 'three'` trực tiếp trong trình duyệt mà không build.
- **Single-file per module** — mỗi mô-đun là 1 file HTML duy nhất chứa cả HTML + CSS + JS inline, dễ triển khai và chia sẻ.
- **Responsive & Touch-ready** — hỗ trợ cả máy tính, máy tính bảng; OrbitControls xử lý touch, AR3/AR4 có Touch Event riêng.

---

## 6. Yêu cầu hệ thống

| Yêu cầu | Chi tiết |
|---|---|
| Trình duyệt | Chrome 89+, Edge 89+, Firefox 89+, Safari 15+ |
| WebGL | Phiên bản 2.0 (hầu hết thiết bị từ 2019 trở đi) |
| Kết nối Internet | Cần (để tải Three.js từ CDN và font Google) |
| Phần cứng | GPU tích hợp trở lên (Intel UHD, Apple M1...) |
| Máy chủ web | Cần server để CORS cho SVG (AR3); AR1/AR2/AR4 mở trực tiếp được |

---

## 7. Cách chạy dự án

```bash
# Mở trang chủ → truy cập tất cả module
# Dùng Live Server (VS Code) hoặc bất kỳ HTTP server nào:

npx serve .             # Node.js
python -m http.server   # Python

# Sau đó mở: http://localhost:PORT/
```

---

*AR Science Lab – Bộ học liệu số tương tác 3D hỗ trợ dạy học Khoa Học Tự Nhiên · ĐHSP Đà Nẵng · 2025–2026*
