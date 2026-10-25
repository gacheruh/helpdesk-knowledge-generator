import streamlit as st
import pandas as pd
from utils.analyzer import load_tickets, get_category_counts, generate_kb_article

st.set_page_config(
    page_title="Helpdesk Ticket Analytics & KB Generator",
    page_icon="📋",
    layout="wide"
)

st.title("Automated Helpdesk Ticket Analytics & Knowledge Base Generator")
st.markdown("Analyze recurring IT support requests, track ticket volumes, and automatically draft troubleshooting knowledge base articles.")

df = load_tickets()

tab1, tab2 = st.tabs(["Ticket Analytics & Metrics", "AI Knowledge Base Article Generator"])

with tab1:
    st.header("Support Ticket Summary")
    if not df.empty:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Tickets Logged", len(df))
        with col2:
            st.metric("Resolved Tickets", len(df[df['status'] == 'Resolved']))
        with col3:
            st.metric("Open Tickets", len(df[df['status'] == 'Open']))
            
        st.subheader("Ticket Volume by Category")
        counts = get_category_counts(df)
        st.bar_chart(counts)
        
        st.subheader("Recent Support Tickets")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No support ticket data found.")

with tab2:
    st.header("Knowledge Base & SOP Generator")
    st.markdown("Select a support category to automatically synthesize recent user issues into a structured troubleshooting guide.")
    
    if not df.empty:
        categories = df['category'].unique().tolist()
        selected_category = st.selectbox("Select Support Category", categories)
        
        if st.button("Generate Knowledge Base Article"):
            kb_content = generate_kb_article(selected_category, df)
            st.markdown("---")
            st.markdown(kb_content)
            st.download_button(
                label="Download KB Article (.md)",
                data=kb_content,
                file_name=f"KB_{selected_category.replace(' ', '_')}.md",
                mime="text/markdown"
            )
    else:
        st.warning("No data available to generate knowledge base articles.")
