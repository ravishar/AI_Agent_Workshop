import streamlit as st
from Agents.websearchagent import SearchAgent

st.markdown("# Welcome to Agent Workshop at ACM San Francisco Bay Area!")

input_query = st.text_input("Query:")

agent=SearchAgent(delay=0)

if input_query:
    # show progress bar
    updated_agent = None
    with st.spinner("Calling Agent...", show_time=True):
        updated_agent = agent.call(query=input_query)

    for i, step in enumerate(updated_agent.memory.steps):
        try:
            st.markdown(f"Step ({i}): (thinking for {step.duration:.2f} seconds)\n")
            with st.expander(f"Facts for Step ({i})", expanded=False):
                st.json(step.dict())
            st.markdown(step.model_output)

        except Exception as e:
            #st.markdown(f"Error: {e}")
            pass
    
    


