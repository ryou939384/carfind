import streamlit as st
from questions import questions

st.title("車クイズ")

if "current" not in st.session_state:
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False

if st.session_state.current < len(questions):

    question = questions[st.session_state.current]

    st.subheader(
        f"第{st.session_state.current + 1}問"
    )

    st.write(question["question"])

    st.image(question["image"], width=400)

    for i, choice in enumerate(question["choices"]):

        if st.button(choice, key=f"choice_{st.session_state.current}_{i}",
                     disabled=st.session_state.answered):

            st.session_state.answered = True

            if i == question["answer"]:
                st.session_state.score += 1
                st.success("正解！")
            else:
                st.error("不正解！")

            st.rerun()

    if st.session_state.answered:

        if st.button("次の問題へ"):
            st.session_state.current += 1
            st.session_state.answered = False
            st.rerun()

else:
    st.title("クイズ終了！")

    st.write(
        f"{len(questions)}問中{st.session_state.score}問正解！"
    )

    if st.button("もう一度遊ぶ"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()