

import openai
import streamlit as st
from streamlit_chat import message
# 设置标题, 功能介绍
st.title("和ChatGPT聊天")
st.sidebar.header("功能介绍")
st.sidebar.info(
    '''这是一个web应用程序，通过OpenAI的API和ChatGPT模型实现交互(聊天)功能。在文本框中输入问题，然后按Enter键查询，接收ChatGPT的回答'''
)

#申请的api_key
openai.api_key = ""
def generate_response(prompt):
    completion=openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        temperature=0.6
    )
    message=completion.choices[0].text
    return message
 
st.markdown("#### 我是ChatGPT聊天机器人,我可以回答您的任何问题！")
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input=st.text_input("请输入您的问题:",key='input')
if user_input:
    output=generate_response(user_input)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], 
                is_user=True, 
                key=str(i)+'_user')