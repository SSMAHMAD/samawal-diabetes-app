import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق سموال للسكري", page_icon="🩸")

st.title("🩸 تطبيق سموال لمتابعة السكري")
st.markdown("مرحباً بك! هذا التطبيق يساعدك في تسجيل قراءات السكر اليومية.")

# خانة إدخال القراءة
reading = st.number_input("أدخل قراءة السكر الحالية:", min_value=0.0, max_value=500.0, step=0.1)

if st.button("حفظ القراءة"):
    st.success(f"تم تسجيل القراءة بنجاح: {reading}")
        st.balloons()

        st.divider()
        st.info("💡 نصيحة: استشر طبيبك دائماً لمراجعة القراءات.")
       import streamlit as st

       st.set_page_config(page_title="تطبيق سموال للسكري", page_icon="🩸")

       st.title("🩸 تطبيق سموال لمتابعة السكري")
       st.write("أهلاً بك يا سموال في تطبيقك الخاص!")

       reading = st.number_input("أدخل قراءة السكر الحالية:", min_value=0.0, max_value=500.0)

       if st.button("حفظ القراءة"):
           st.success(f"تم تسجيل القراءة: {reading}")
               st.balloons()
                