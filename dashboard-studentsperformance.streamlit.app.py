import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_option_menu import *
import pickle

    # Fungsi untuk memuat data
@st.cache_data
def load_data():
    df = pd.read_csv("StudentsPerformance.csv")
    return df

def main():
    # Judul halaman
    st.title("Student Performance Analysis")

    # Pilihan menu di sidebar
    with st.sidebar :
        selected = option_menu('Student Performance',['Beranda','Distribusi','Perbandingan','Relasi','Prediksi'],default_index=0)

    # Menampilkan konten sesuai pilihan menu
    if selected == "Beranda":
        st.header("Selamat datang di aplikasi analisis Student Performance!")
        st.write("Di sini Anda dapat menganalisis berbagai aspek kinerja siswa.")

    elif selected == "Distribusi":
        st.header("Analisis Distribusi")
        st.write("Di sini Anda dapat melihat distribusi dari nilai-nilai yang ada dalam dataset.")
        korelasi()
        show_distribution(load_data())

    elif selected == "Perbandingan":
        st.header("Analisis Perbandingan")
        st.write("Di sini Anda dapat melakukan perbandingan antara berbagai variabel dalam dataset.")
        perbandingan()
        show_relationship(load_data())

    elif selected == "Relasi":
        st.header("Analisis Komposisi")
        st.write("Di sini Anda dapat melihat komposisi dari berbagai kategori dalam dataset.")
        show_composition(load_data())

    elif selected == "Prediksi":
        st.header("Prediksi")
        st.write("Di sini Anda dapat melakukan prediksi berdasarkan data yang ada.")
        prediksi()

def korelasi():
    st.title("Korelasi antara Writing Score dan Math Score Siswa")

    # Memuat data
    data = load_data()

    # Menampilkan scatter plot
    st.subheader("Scatter Plot: Korelasi antara Writing Score dan Math Score Siswa")
    fig, ax = plt.subplots()
    sns.scatterplot(x='writing score', y='math score', data=data)
    plt.title('Korelasi antara Writing Score dan Math Score Siswa')
    plt.xlabel('Writing Score')
    plt.ylabel('Math Score')
    st.pyplot(fig)

def perbandingan():
    # Memuat data
    data = load_data()

    # Menampilkan judul halaman
    st.title("Perbandingan Nilai")

    # Pilihan perbandingan dari dropdown
    comparison_option = st.selectbox("Pilih Perbandingan:", [
        "Rata-rata Nilai Math berdasarkan Gender",
        "Rata-rata Nilai Reading berdasarkan Gender",
        "Rata-rata Nilai Writing berdasarkan Gender"
    ])

    # Menampilkan perbandingan sesuai pilihan
    if comparison_option == "Rata-rata Nilai Math berdasarkan Gender":
        st.subheader("Perbandingan Rata-rata Nilai Math berdasarkan Gender")
        avg_math_score_male = data[data['gender'] == 'male']['math score'].mean()
        avg_math_score_female = data[data['gender'] == 'female']['math score'].mean()
        st.write("Rata-rata Nilai Math Siswa Laki-laki:", avg_math_score_male)
        st.write("Rata-rata Nilai Math Siswa Perempuan:", avg_math_score_female)

    elif comparison_option == "Rata-rata Nilai Reading berdasarkan Gender":
        st.subheader("Perbandingan Rata-rata Nilai Reading berdasarkan Gender")
        avg_reading_score_male = data[data['gender'] == 'male']['reading score'].mean()
        avg_reading_score_female = data[data['gender'] == 'female']['reading score'].mean()
        st.write("Rata-rata Nilai Reading Siswa Laki-laki:", avg_reading_score_male)
        st.write("Rata-rata Nilai Reading Siswa Perempuan:", avg_reading_score_female)

    elif comparison_option == "Rata-rata Nilai Writing berdasarkan Gender":
        st.subheader("Perbandingan Rata-rata Nilai Writing berdasarkan Gender")
        avg_writing_score_male = data[data['gender'] == 'male']['writing score'].mean()
        avg_writing_score_female = data[data['gender'] == 'female']['writing score'].mean()
        st.write("Rata-rata Nilai Writing Siswa Laki-laki:", avg_writing_score_male)
        st.write("Rata-rata Nilai Writing Siswa Perempuan:", avg_writing_score_female)

def show_correlation_heatmap():
    # Membaca dataset
    df_file = pd.read_csv('StudentsPerformance.csv')

    # Menghapus kolom non-numerik atau melakukan encoding jika diperlukan
    # Misal, melakukan encoding untuk kolom 'category'
    # df_file = pd.get_dummies(df_file, columns=['category'])

    # Menghitung korelasi antar kolom numerik
    numeric_df = df_file.select_dtypes(include=['int64', 'float64'])
    corr = numeric_df.corr()

    # Membuat figure dan axis
    fig, ax = plt.subplots(figsize=(10, 8))

    # Membuat heatmap korelasi
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.title('Heatmap Korelasi Antar Kolom Numerik')

    # Menampilkan heatmap
    st.pyplot(fig)

# Memuat dataset student performance dari path lokal
@st.cache_data
def load_data():
    data = pd.read_csv("StudentsPerformance.csv")
    return data

# Menampilkan beranda
def show_home():
    """
    Menampilkan halaman utama aplikasi.
    """
    st.subheader("Beranda")
    st.write("Selamat datang di halaman utama! Di sini Anda dapat menjelajahi berbagai analisis mengenai dataset Student Performance.")

# Menampilkan distribusi nilai math, reading, dan writing
def show_distribution(data):
    """
    Menampilkan distribusi nilai math, reading, dan writing dalam dataset Student Performance.
    """
    st.title("Distribusi Nilai")
    st.write("Menu ini menampilkan distribusi dari nilai math, reading, dan writing dalam dataset Student Performance.")
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    sns.histplot(data['math score'], kde=True, ax=axes[0])
    sns.histplot(data['reading score'], kde=True, ax=axes[1])
    sns.histplot(data['writing score'], kde=True, ax=axes[2])
    axes[0].set_title("Nilai Math")
    axes[1].set_title("Nilai Reading")
    axes[2].set_title("Nilai Writing")
    st.pyplot(fig)

# Menampilkan hubungan antara nilai math, reading, dan writing
def show_relationship(data):
    """
    Menampilkan hubungan antara nilai math, reading, dan writing dalam dataset Student Performance.
    """
    st.title("Hubungan Nilai")
    st.write("Menu ini menampilkan hubungan antara nilai math, reading, dan writing dalam dataset Student Performance.")
    plot_option = st.selectbox("Pilih Plot:", ["Nilai Math vs Nilai Reading", "Nilai Math vs Nilai Writing", "Nilai Reading vs Nilai Writing"])

    if plot_option == "Nilai Math vs Nilai Reading":
        st.subheader("Scatter Plot: Nilai Math vs Nilai Reading")
        fig, ax = plt.subplots()
        sns.scatterplot(x='math score', y='reading score', data=data)
        ax.set_xlabel("Nilai Math")
        ax.set_ylabel("Nilai Reading")
        st.pyplot(fig)

    elif plot_option == "Nilai Math vs Nilai Writing":
        st.subheader("Scatter Plot: Nilai Math vs Nilai Writing")
        fig, ax = plt.subplots()
        sns.scatterplot(x='math score', y='writing score', data=data)
        ax.set_xlabel("Nilai Math")
        ax.set_ylabel("Nilai Writing")
        st.pyplot(fig)

    elif plot_option == "Nilai Reading vs Nilai Writing":
        st.subheader("Scatter Plot: Nilai Reading vs Nilai Writing")
        fig, ax = plt.subplots()
        sns.scatterplot(x='reading score', y='writing score', data=data)
        ax.set_xlabel("Nilai Reading")
        ax.set_ylabel("Nilai Writing")
        st.pyplot(fig)

# Menampilkan perbandingan rata-rata nilai berdasarkan gender
def show_comparison(data):
    """
    Menampilkan perbandingan rata-rata nilai berdasarkan gender dalam dataset Student Performance.
    """
    st.title("Perbandingan Nilai berdasarkan Gender")
    st.write("Menu ini memberikan perbandingan rata-rata nilai berdasarkan gender dalam dataset Student Performance.")
    comparison_option = st.selectbox("Pilih Perbandingan:", ["Rata-rata Nilai Math", "Rata-rata Nilai Reading", "Rata-rata Nilai Writing"])

    if comparison_option == "Rata-rata Nilai Math":
        st.subheader("Perbandingan Rata-rata Nilai Math berdasarkan Gender")
        avg_math_score = data.groupby('gender')['math score'].mean()
        st.write(avg_math_score)

    elif comparison_option == "Rata-rata Nilai Reading":
        st.subheader("Perbandingan Rata-rata Nilai Reading berdasarkan Gender")
        avg_reading_score = data.groupby('gender')['reading score'].mean()
        st.write(avg_reading_score)

    elif comparison_option == "Rata-rata Nilai Writing":
        st.subheader("Perbandingan Rata-rata Nilai Writing berdasarkan Gender")
        avg_writing_score = data.groupby('gender')['writing score'].mean()
        st.write(avg_writing_score)

# Menampilkan komposisi jenis persiapan ujian
def show_composition(data):
    """
    Menampilkan komposisi dari jenis persiapan ujian dalam dataset Student Performance.
    """
    st.title("Komposisi Persiapan Ujian")
    st.write("Menu ini menampilkan komposisi dari jenis persiapan ujian dalam dataset Student Performance.")
    test_prep_count = data['test preparation course'].value_counts()
    st.write("Jumlah Siswa yang Mengikuti Persiapan Ujian:")
    st.write(test_prep_count)
    st.subheader("Diagram Lingkaran Komposisi Persiapan Ujian")
    fig, ax = plt.subplots()
    ax.pie(test_prep_count, labels=test_prep_count.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(fig)

def prediksi():
    gender = st.selectbox('Select gender',['Male','Female'])
    race = st.selectbox('Select gender',['Group A','Group B','Group C','Group D','Group E'])
    level = st.selectbox('Select parental level of education',["bachelor's degree", 'some college', "master's degree","associate's degree", 'high school', 'some high school'])
    lunch = st.selectbox('Select lunch',['standart','free/reduced'])
    mathScore = st.number_input("Input math score",0,100)
    readingScore = st.number_input("Input reading score",0,100)
    writingScore = st.number_input("Input writing score",0,100)
    mathScoreCategory = st.selectbox("Input math score category",['Intermediate', 'Advanced', 'Elementary', 'Master'])
    readingScoreCategory = st.selectbox("Input reading score category",['Intermediate', 'Advanced', 'Elementary', 'Master'])
    writingScoreCategory = st.selectbox("Input writing score category",['Intermediate', 'Advanced', 'Elementary', 'Master'])

    data = pd.DataFrame({
        'gender' : [0 if gender == 'Female' else 1],
        'race/ethnicity' : [0 if race == 'Group A' else (1 if race == 'Group B' else (2 if race == 'Group C' else (3 if race == 'Group D' else 4)))],
        'parental level of education' : [0 if level == "bachelor's degree" else (1 if level == 'some college' else (2 if level == "master's degree" else (3 if level == "associate's degree" else (4 if level == 'high school' else 5))))],
        'lunch' : [0 if lunch == 'free/reduced' else 1],
        'math score' : [mathScore],
        'reading score' : [readingScore],
        'writing score' : [writingScore],
        'score_category_math' : [0 if mathScoreCategory == 'Intermediate' else (1 if mathScoreCategory == 'Advanced' else (2 if mathScoreCategory == 'Elementary' else 3))],
        'score_category_reading' : [0 if readingScoreCategory == 'Intermediate' else (1 if readingScoreCategory == 'Advanced' else (2 if readingScoreCategory == 'Elementary' else 3))],
        'score_category_writing' : [0 if writingScoreCategory == 'Intermediate' else (1 if writingScoreCategory == 'Advanced' else (2 if writingScoreCategory == 'Elementary' else 3))]
    })
    st.write(data)
    btn = st.button('Predict')
    if btn:
        with open('gnb.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        predicted = loaded_model.predict(data)
        if (predicted[0] == 0):
            st.success("None")
        elif (predicted[0] == 1):
            st.success("Completed") 
        else :
            st.error('Not Defined')

if __name__ == '__main__':
    main()
