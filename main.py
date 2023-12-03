




import streamlit as st

from PIL import Image

# page Configuration

st.set_page_config(
    page_title="Hui-Zhang",
    page_icon="🏡",
    layout="wide",
)


# 头像
col11, col12, col13, col14 = st.columns([1,1,1.5,1.5])
with col13:
    image = Image.open(r'./Resource/1.png')
    st.image(image, width=300)

st.markdown("# Hui-Zhang")
    
st.markdown("Shandong University, Jinan, China. ")
st.markdown("E-mail: 202234949@mail.sdu.edu.cn, bigserendipty@gmail.com")

st.success("Research Interest")
st.markdown("Machine learning, Deep learning, Contrastive learning, Neural network architecture search, Reinforcement learning...")
st.markdown("Convolutional neural network(CNN), Long short-term memory network(LSTM), Residual neural network(RNN), Broad learning system(BLS), Interval type-2 fuzzy logic system(IT2FLS), TSK fuzzy logic system, Deep fuzzy system(DFS), Transformer, Encoder-decoder architecture...")
st.markdown("Adaptive optimization algorithm, Evolutionary algorithm, Gradient descent algorithm, Forward automatic differentiation technology, Backpropagation algorithm...")
st.markdown("Long-term forecasting of new energy and load, Integrated energy system planning and design, Integrated energy system optimization control...")
st.markdown("Software development, Hardware design, Algorithm design, Vue framework, SpringBoot framework, PyQt5 framework, Streamlit framework, JAX framework, PyTorch framework...")
st.success("Research Articles")

st.markdown("[1] **H.Zhang**, W.Peng. Time Series Forecasting Based on Interval Type-2 Fuzzy Logic System with PSO, 2021 China Automation Congress (CAC), Beijing, China, 2021, pp. 3090-3097, doi: 10.1109/CAC53003.2021.9727414.")
st.markdown("[2] **H.Zhang**, B.Sun .et al. Interval Type-2 Fuzzy Logic System Based on Batch Normalization and Uniform Regularization with Application to Time Series Forecasting, 2023 China Automation Congress (CAC), Chongqing, China, 2023")
st.markdown("[3] **H.Zhang**, B.Sun and W.Peng*. A novel hybrid deep fuzzy model based on gradient descent algorithm with application to time series forecasting, ***Expert Systems with Applications***, 2023, doi:10.1016/j.eswa.2023.121988, SCI-Q1, TOP")
st.markdown("[4] L.Zhang, **H.Zhang**, F.Li and B.Sun*. Bi-level Optimal Design of Integrated Energy System with Synergy of Renewables, Conversion, Storage and Demand, ***IEEE TRANSACTIONS ON INDUSTRY APPLICATIONS***, SCI-Q2")
st.markdown("[5] **H.Zhang**, W.Peng*. Mini-Batch Forward Automatic Differentiation based on Efficient Adaptive Optimization Algorithm for TSK Fuzzy Systems, ***IEEE TRANSACTIONS ON FUZYY SYSTEMS***, SCI-Q1, TOP")
st.markdown("[6] H.Ming, **H.Zhang**, N.Cui*. Battery life estimation method based on forward adaptive width learning, ***Energy***, SCI-Q1, TOP")

st.success("Patent")
st.markdown("[1] 孙波, **张辉**, 张立志, 一种集成结构—容量—运行的综合能源系统架构搜索方法, ***国家发明专利***")

st.success("Standard")
st.markdown("[1] 潘凤文, 孙波, 张立志, 张全军, 刘洋, **张辉**, 吴睿, 杨锋, 王迎波, 秦顺顺, 冯美丽, 含氢分布式综合能源系统运行优化指南, ***地方/行业标准***")

st.success("Participate In Projects")
st.markdown("**国家重点研发计划项目**, 管道氢气在城镇供能领域关键技术研究与规模应用, **项目骨干**, 经费**5.15亿**元")
st.markdown("**国家重点研发计划项目**, 氢能多场景深度融合及智慧管控技术研究与示范应用, **项目骨干**, 经费**2.05亿**元")
st.markdown("**国家电网科技项目**, 多能互补综合能源系统协同优化控制研究, **项目骨干**, 经费**300万**元")

col1, col2, col3, col4 = st.columns([1,1,1,1.5])

with col3:
    image = Image.open(r'./Resource/4.png')
    st.image(image)

col1, col2, col3, col4 = st.columns([1,1,1.1,1.5])

with col3:
    st.caption('Copyright @ 2023, 山东大学 中国·济南')

