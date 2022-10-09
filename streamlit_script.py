def hate_detection():
    import streamlit as st
    st.title('Hate Speech Detection')
    user = st.text_area('Enter any tweet:')
    if len(user)<1:
        st.write(' ')
    else:
        sample=user
        data = cv.transform([sample]).toarray()
        a = clf.predict(data)
        st.title(a)

