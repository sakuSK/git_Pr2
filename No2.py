import streamlit as st

# BMI計算の方法
st.session_state.bmi = 0
st.session_state.h = 0
st.session_state.w = 0
st.session_state.best_w = 0
if 'resalt' not in st.session_state:
    st.session_state.resalt = 0 
def calculate_bmi(height, weight):
    st.session_state.bmi = weight / ((height / 100) ** 2)
    st.session_state.resalt = f"{st.session_state.bmi:.2f}"  # f-stringを使ってフォーマットするよ！
    st.write(f"あなたのBMIは{st.session_state.resalt}です")

def best_weight(height, weight):
    st.session_state.best_w = ((height/100)** 2) *22   # 適正体重 ＝ (身長m)2 ×22
    st.session_state.resalt_w = f"{st.session_state.best_w:.2f}"  # f-stringを使ってフォーマットするよ！
    st.write(f"あなたの身長の適正体重は{st.session_state.resalt_w}です")

st.session_state.h = st.slider("身長を入力してください", 0, 300, 160)
st.session_state.w = st.slider("体重を入力してください", 0, 300, 60)

# スライダーの後にBMIを計算する
calculate_bmi(st.session_state.h, st.session_state.w)
best_weight(st.session_state.h, st.session_state.w)
def clear_file(file_path):
    try:
        with open(file_path, "w") as file:
            file.truncate(0)
        return True
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False         
with open('text1.txt','a',encoding="utf-8") as file:
    if st.button("結果の保存"):
        file.write(str(st.session_state.resalt) + '\n') # 数値を文字列に変換するよ！
        st.info("保存しました。")
    if st.button("結果のデータを削除"):
        if clear_file('text1.txt'):
            st.success("データを削除しました。")
        else:
            st.error("削除に失敗しました。")
with open('text1.txt','r',encoding="utf-8") as file:
    if st.button("結果を見る"):
        content = file.read()
        st.text_area("履歴",content,)
