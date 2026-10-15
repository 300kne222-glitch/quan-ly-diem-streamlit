import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Ho_ten': [
        'Trần kiều anh', 'Nguyễn công minh', 'Tô lê quốc khánh', 'đặng đình hải', 
        'phùng trâm anh', 'đặng khánh ly', 'phan yến như', 'tường thị mai trinh', 
        'nguyễn hoài anh', 'đinh thị bảo ngọc'
    ],
    'Chuyen_can': [9.0, 8.5, 7.0, 10.0, 8.0, 8.0, 9.5, 8.0, 8.0, 9.0],
    'Giua_ky': [8.0, 7.5, 6.0, 9.0, 7.5, 7.0, 8.5, 7.6, 7.5, 8.5],
    'Cuoi_ky': [8.5, 8.0, 6.5, 9.5, 9.0, 7.5, 9.0, 8.5, 8.0, 9.0]
}
df = pd.DataFrame(data)
df['Tong_ket'] = (df['Chuyen_can'] * 0.2 + df['Giua_ky'] * 0.3 + df['Cuoi_ky'] * 0.5).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

st.set_page_config(page_title="QUẢN LÝ ĐIỂM SINH VIÊN", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("📊 Bảng điểm học sinh")
st.dataframe(df, use_container_width=True)

st.subheader("📊 Thống kê nhanh")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm TB của lớp", f"{df['Tong_ket'].mean():.2f}")
col2.metric("Số SV đạt (>=5.0)", f"{len(df[df['Tong_ket'] >= 5.0])} học sinh")

sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
col3.metric("Tổng kết cao nhất", f"{sv_max['Tong_ket']}", f"{sv_max['Ho_ten']}")
col4.metric("Tổng kết thấp nhất", f"{sv_min['Tong_ket']}", f"{sv_min['Ho_ten']}", delta_color="inverse")

st.subheader("🔍 Tra cứu theo cá nhân")
select_student = st.selectbox("Chọn tên sinh viên:", df['Ho_ten'].tolist())
student_row = df[df['Ho_ten'] == select_student].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.write(f"**Chuyên cần:** {student_row['Chuyen_can']}")
c2.write(f"**Giữa kỳ:** {student_row['Giua_ky']}")
c3.write(f"**Cuối kỳ:** {student_row['Cuoi_ky']}")
c4.write(f"**Tổng kết:** {student_row['Tong_ket']}")
c5.write(f"**Xếp loại:** {student_row['Xep_loai']}")

st.subheader("📉 Biểu đồ phân tích")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df['Ho_ten'], df['Tong_ket'], color='orange', edgecolor='black')
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha='right')
for idx, v in enumerate(df['Tong_ket']):
    ax.text(idx, v + 0.15, f"{v}", ha='center', fontweight='bold')
st.pyplot(fig)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 11px; color: gray;'>Họ tên: Nguyễn Văn A - MSSV: 12345678</p>", unsafe_allow_html=True)
