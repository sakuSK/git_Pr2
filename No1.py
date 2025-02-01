import streamlit as st

def dentaku():
    st.title("電卓")
    st.session_state.num=0
    st.session_state.num2=0
    st.session_state.resalt=0
    symbol=["＋","－","×","÷"]
    st.session_state.title1 = st.text_input("1つ目の数字を入力してください。")
    st.session_state.num=st.session_state.title1
    st.session_state.title2 = st.text_input("2つ目の数字を入力してください。")
    st.session_state.num2=st.session_state.title2
    title3 = st.radio("演算子を入力してください。",(symbol))
    if st.button("計算", type="primary"):
        if title3=="＋":
            st.session_state.resalt=int(st.session_state.num)+int(st.session_state.num2)
        if title3=="－":
            st.session_state.resalt=int(st.session_state.num)-int(st.session_state.num2)
        if title3=="×":
            st.session_state.resalt=int(st.session_state.num)*int(st.session_state.num2)
        if title3=="÷":
            st.session_state.resalt=int(st.session_state.num)/int(st.session_state.num2)
        st.write(st.session_state.resalt)
        with open('text1.txt','a',encoding="utf-8") as file:
            first= st.session_state.title1
            second= st.session_state.title2
            ennzann=title3
            kekka=str(st.session_state.resalt)
            file.write(first + ennzann + second + '=' + kekka + '\n') #'\n'は改行を表すよ!
            print("履歴に保存されています。")

    def clear_file(file_path):
        try:
            with open(file_path, "w") as file:
                file.truncate(0)
            return True
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            return False

    if st.button("履歴を閲覧"):
        with open('text1.txt','r',encoding="utf-8") as file:
            content = file.read()
            st.text(content) 

    if st.button("履歴を削除"):
            if clear_file('text1.txt'):
                st.success("履歴を削除しました。")
            else:
                st.error("削除に失敗しました。")