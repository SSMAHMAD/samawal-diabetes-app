import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- إعدادات الصفحة والأيقونة ---
st.set_page_config(page_title="سموال للسكري", page_icon="🩸", layout="centered")

# --- رسالة تثبيت التطبيق داخل الصفحة ---
if 'install_closed' not in st.session_state:
    st.session_state.install_closed = False

    if not st.session_state.install_closed:
        st.info("📲 لتحويل التطبيق إلى أيقونة على هاتفك:")
            st.markdown("""
                **📱 أندرويد (Chrome):** اضغط على ⋮ ثم اختر **Install App**  
                    **🍏 آيفون (Safari):** اضغط زر المشاركة ثم **Add to Home Screen**
                        """)
                            col1, col2 = st.columns(2)
                                with col1:
                                        if st.button("✅ فهمت"):
                                                    st.success("🎉 ممتاز! ثبت التطبيق واستفد منه يوميًا")
                                                        with col2:
                                                                if st.button("❌ إخفاء"):
                                                                            st.session_state.install_closed = True

                                                                            # --- التنسيق الجمالي ---
                                                                            st.markdown("""
                                                                                <style>
                                                                                    .stButton>button { width: 100%; border-radius: 20px; background-color: #1a73e8; color: white; }
                                                                                        .stMetric { background-color: #f8f9fa; border-radius: 15px; padding: 15px; border: 1px solid #dee2e6; }
                                                                                            </style>
                                                                                                """, unsafe_allow_html=True)

                                                                                                st.title("🩸 نظام متابعة السكري الذكي")
                                                                                                st.markdown("##### إشراف وتصميم: **سموال سيد محمد أحمد**")

                                                                                                # --- المعادلات الحسابية ---
                                                                                                def calculate_all(df):
                                                                                                    if df.empty: return 0, 0, 0, 0
                                                                                                        avg_mmol = df['value'].mean()
                                                                                                            avg_mgdl = avg_mmol * 18.0182
                                                                                                                hba1c_pct = (avg_mmol + 2.59) / 1.59
                                                                                                                    hba1c_uk = (hba1c_pct - 2.15) * 10.929
                                                                                                                        return round(avg_mmol, 1), round(avg_mgdl, 0), round(hba1c_pct, 1), round(hba1c_uk, 0)

                                                                                                                        # --- إدخال البيانات ---
                                                                                                                        with st.form("input_form", clear_on_submit=True):
                                                                                                                            val = st.number_input("أدخل القراءة (mmol/L):", 1.0, 35.0, step=0.1)
                                                                                                                                status = st.select_slider("الحالة الغذائية:", options=["صائم جاف", "صائم مائي", "بعد الاستيقاظ", "بعد الأكل"])
                                                                                                                                    hours = st.number_input("عدد الساعات:", 0, 48)
                                                                                                                                        submitted = st.form_submit_button("💾 حفظ القراءة الآن")

                                                                                                                                        if 'records' not in st.session_state:
                                                                                                                                            st.session_state.records = []

                                                                                                                                            if submitted:
                                                                                                                                                entry = {
                                                                                                                                                        "date": datetime.now(),
                                                                                                                                                                "value": val,
                                                                                                                                                                        "status": status,
                                                                                                                                                                                "hours": hours
                                                                                                                                                                                    }
                                                                                                                                                                                        st.session_state.records.append(entry)
                                                                                                                                                                                            st.success("تم الحفظ! ستظهر النتائج في السجل أدناه.")

                                                                                                                                                                                            # --- عرض النتائج والدورة الزمنية ---
                                                                                                                                                                                            if st.session_state.records:
                                                                                                                                                                                                df = pd.DataFrame(st.session_state.records)
                                                                                                                                                                                                    # فلترة تلقائية لـ 90 يوم
                                                                                                                                                                                                        ninety_days_ago = datetime.now() - timedelta(days=90)
                                                                                                                                                                                                            df = df[df['date'] > ninety_days_ago]
                                                                                                                                                                                                                
                                                                                                                                                                                                                    m1, m2, m3, m4 = calculate_all(df)
                                                                                                                                                                                                                        
                                                                                                                                                                                                                            # عرض المؤشرات
                                                                                                                                                                                                                                c1, c2 = st.columns(2)
                                                                                                                                                                                                                                    with c1:
                                                                                                                                                                                                                                            st.metric("المتوسط (بريطاني)", f"{m1} mmol/L")
                                                                                                                                                                                                                                                    st.metric("التراكمي (%)", f"{m3} %")
                                                                                                                                                                                                                                                        with c2:
                                                                                                                                                                                                                                                                st.metric("المتوسط (عالمي)", f"{int(m2)} mg/dL")
                                                                                                                                                                                                                                                                        st.metric("التراكمي (mmol/mol)", f"{int(m4)}")

                                                                                                                                                                                                                                                                            st.divider()
                                                                                                                                                                                                                                                                                st.write("### 📂 السجل التاريخي (90 يوماً)")
                                                                                                                                                                                                                                                                                    st.dataframe(df.drop(columns=['date']).sort_index(ascending=False), use_container_width=True)

                                                                                                                                                                                                                                                                                    st.markdown("---")
                                                                                                                                                                                                                                                                                    st.caption("⚠️ هذا التطبيق للمساعدة فقط ولا يغني عن استشارة الطبيب | تصميم سموال سيد محمد أحمد © 2026")