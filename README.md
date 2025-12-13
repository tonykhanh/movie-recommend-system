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
*   **Machine Learning:** Scikit-learn (CountVectorizer, Cosine Similarity), Pandas
*   **Frontend:** HTML, CSS, JavaScript (AJAX)
*   **Data Source:** The Movie Database (TMDB) API & Kaggle Dataset (TMDB 5000 Movie Dataset)

## 🧠 Nguyên Lý Hoạt Động (Algorithm)

Hệ thống sử dụng **Content-Based Filtering** (Lọc dựa trên nội dung) để gợi ý phim.

1.  **Dữ liệu huấn luyện:** Sử dụng bộ dữ liệu `tmdb_5000_movies.csv` và `tmdb_5000_credits.csv`.
2.  **Trích xuất đặc trưng (Feature Engineering):**
    *   Tạo ra một trường `tags` duy nhất cho mỗi phim bằng cách kết hợp: `Overview` (mô tả) + `Genres` (thể loại) + `Keywords` (từ khóa) + `Cast` (3 diễn viên chính) + `Crew` (đạo diễn).
    *   Xử lý văn bản: Loại bỏ khoảng trắng tên riêng (ví dụ: `Tony Khanh` -> `TonyKhanh`) để tạo thành các thực thể duy nhất.
3.  **Vector hóa (Vectorization):** Sử dụng `CountVectorizer` để chuyển đổi văn bản `tags` thành các vector số học (giới hạn 5000 từ phổ biến nhất, loại bỏ stop-words tiếng Anh).
4.  **Tính độ tương đồng:** Sử dụng **Cosine Similarity** để tính góc giữa các vector phim. Kết quả là ma trận tương đồng 4805x4805.
5.  **Gợi ý:** Khi người dùng chọn một phim, hệ thống tìm index của phim đó, tra cứu trong ma trận tương đồng để lấy ra 5 phim có điểm số cao nhất.

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
├── create_similarity.py # Script tạo matrix gợi ý (fallback)
├── db.sqlite3          # Database SQLite
├── myapp/              # App chính chứa logic
│   ├── models.py       # Data models & load pickle
│   ├── views.py        # Logic gợi ý & API call
│   └── urls.py         # Routing
├── model/              # Chứa file dữ liệu training (.pkl)
├── static/             # CSS, JS, Images
└── templates/          # HTML templates
Trainning/              # Dữ liệu gốc và Notebook huấn luyện
├── notebook...ipynb    # Jupyter Notebook phân tích & training
├── tmdb_..._movies.csv # Dataset Dataset gốc
└── tmdb_..._credits.csv # Dataset Credits gốc
```

## ⚠️ Lưu ý

*   Dự án sử dụng file `movie_list.pkl` và `similarity.pkl` để gợi ý nhanh.
*   API Key TMDB được tích hợp sẵn để demo.
