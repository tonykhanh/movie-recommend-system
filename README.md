# Movie Recommendation System

Một hệ thống **Content-Based Movie Recommendation** (Gợi ý phim dựa trên nội dung) được xây dựng bằng **Streamlit** và **Python**. Ứng dụng này gợi ý các bộ phim tương tự dựa trên thể loại (genres) và metadata từ bộ dữ liệu TMDB.

## Các tính năng chính
-   **Interactive UI**: Được xây dựng với Streamlit mang lại trải nghiệm người dùng mượt mà.
-   **Content-Based Filtering**: Sử dụng **Cosine Similarity** trên các thuộc tính của phim như thể loại và thẻ (tags).
-   **Real-time Recommendations**: Chọn một bộ phim và nhận gợi ý tức thì.
-   **TMDB Integration**: Lấy poster phim chất lượng cao từ **The Movie Database API**.

## Cấu trúc Dự án
```
.
├── app.py              # Ứng dụng Streamlit chính
├── utils.py            # Các hàm hỗ trợ (Data loading, API calls, Logic)
├── requirements.txt    # Các thư viện phụ thuộc (Dependencies)
├── model/              # Các model đã được huấn luyện sẵn
│   ├── movie_list.pkl  # DataFrame chứa dữ liệu phim
│   └── similarity.pkl  # Ma trận tương đồng (Similarity matrix) đã tính toán trước
└── Trainning/          # Jupyter notebooks dùng để huấn luyện model
```

## Cài đặt

1.  **Clone repository**:
    ```bash
    git clone <repository-url>
    cd movie-recommend-system
    ```

2.  **Cài đặt các thư viện cần thiết**:
    ```bash
    pip install -r requirements.txt
    ```

## Cách sử dụng

Chạy ứng dụng Streamlit:
```bash
streamlit run app.py
```

Ứng dụng sẽ mở trong trình duyệt mặc định tại địa chỉ `http://localhost:8501`.

## Nguyên lý hoạt động
1.  **Data Loading**: Ứng dụng tải `movie_list` và ma trận `similarity` từ các file pickle đã được xử lý trước.
2.  **Selection**: Người dùng chọn một bộ phim từ dropdown menu.
3.  **Recommendation**: Hệ thống tính toán các phim tương tự nhất bằng cách sử dụng ma trận **Cosine Similarity**.
4.  **Display**: Poster và tiêu đề của 5 bộ phim được gợi ý hàng đầu sẽ được hiển thị thông qua **TMDB API**.
