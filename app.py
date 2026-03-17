import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="تطبيق سموال", page_icon="🩸")

st.title("🩸 تطبيق سموال لمتابعة السكري")
st.write("أهلاً بك! سجل قراءاتك هنا.")

# مدخل القراءة
reading = st.number_input("أدخل قراءة السكر الحالية:", min_value=0, max_value=500, value=100)

if st.button("حفظ القراءة"):
    st.success(f"تم تسجيل القراءة بنجاح: {reading}")
        st.balloons()
        