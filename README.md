# Movie Recommendation System (Movie_RS)

Hệ thống gợi ý phim ảnh sử dụng kỹ thuật Content-Based Filtering, xây dựng bằng Django và thư viện Scikit-learn.

![Django Website](https://github.com/KenTyler1/next-portfolio/blob/main/public/images/projects/movie.png)

## 🌟 Tính Năng

*   **Gợi ý phim:** Đề xuất phim tương tự dựa trên nội dung (thể loại, mô tả, v.v.) của phim bạn tìm kiếm.
*   **Tìm kiếm:** Tìm kiếm phim theo tên.
*   **Chi tiết phim:** Hiển thị thông tin chi tiết: poster, tên, điểm đánh giá, ngày phát hành, thể loại.
*   **Hệ thống tài khoản:** Đăng ký và Đăng nhập người dùng.
*   **Giao diện:** React-like UI với API lấy poster thời gian thực từ TMDB.

## 🛠️ Công Nghệ Sử Dụng

*   **Backend:** Python 3, Django
*   **Machine Learning:** Scikit-learn (Cosine Similarity), Pandas
*   **Frontend:** HTML, CSS, JavaScript
*   **Data Source:** The Movie Database (TMDB) API & Pickle datasets

## ⚙️ Cài Đặt & Chạy Dự Án

### 1. Yêu cầu tiên quyết
*   Python 3.9+
*   Pip

### 2. Cài đặt

B1: Clone dự án
```bash
git clone https://github.com/your-username/Movie_RS.git
cd Movie_RS/myproject
```

B2: Cài đặt thư viện dependencies
```bash
pip install django pandas scikit-learn pillow requests
```

B3: Tạo dữ liệu Similarity Matrix (Quan trọng)
*Do file model quá lớn không lưu trên git, chạy script sau để tạo file `similarity.pkl`:*
```bash
python create_similarity.py
```

B4: Chạy Server
```bash
python manage.py runserver
```

Truy cập `http://127.0.0.1:8000/` để trải nghiệm.

## 📝 Hướng Dẫn Sử Dụng

1.  **Trang chủ:** Nhập tên phim bạn thích vào ô tìm kiếm (ví dụ: "Avatar", "Iron Man").
2.  **Kết quả:** Hệ thống sẽ trả về danh sách các phim tương tự nhất dựa trên nội dung.
3.  **Tài khoản:** Bạn có thể đăng ký thành viên mới hoặc đăng nhập để lưu lại lịch sử (tính năng đang phát triển).

## 📂 Cấu Trúc Thư Mục

```
myproject/
├── manage.py           # Django management script
├── create_similarity.py # Script tạo matrix gợi ý
├── db.sqlite3          # Database SQLite
├── myapp/              # App chính chứa logic
│   ├── models.py       # Data models & load pickle
│   ├── views.py        # Logic gợi ý & API call
│   └── urls.py         # Routing
├── model/              # Chứa file dữ liệu training (.pkl)
├── static/             # CSS, JS, Images
└── templates/          # HTML templates
```

## ⚠️ Lưu ý

*   Dự án sử dụng file `movie_list.pkl` và `similarity.pkl` để gợi ý nhanh.
*   API Key TMDB được tích hợp sẵn để demo.
