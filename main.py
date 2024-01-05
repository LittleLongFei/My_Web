

import streamlit as st

from PIL import Image

# page Configuration

st.set_page_config(
    page_title="Hui-Zhang",
    page_icon="🏡",
    layout="wide",
)


# 头像
col11, col12, col13, col14 = st.columns([1, 1, 1.5, 1.5])
with col13:
    image = Image.open(r'./Resource/1.png')
    st.image(image, width=300)

st.markdown("# Hui-Zhang")

st.markdown("山东大学 控制科学与工程学院, 中国, 济南. ")
st.markdown("E-mail: 202234949@mail.sdu.edu.cn, bigserendipty@gmail.com")

# 研究兴趣

st.success("Research Interest")


st.markdown("机器学习, 深度学习, 对比学习, 神经架构搜索, 强化学习, 迁移学习, 域适应, 随机特征, 科学机器学习...")
st.markdown("卷积神经网络(CNN), 长短期记忆网络(LSTM), 残差神经网络(RNN), 宽度学习系统(BLS), 区间二型模糊逻辑系统(IT2FLS), TSK模糊逻辑系统, 深度模糊系统(DFS), Transformer, 物理信息神经网络...")
st.markdown("自适应优化算法, 进化算法, 梯度下降算法, 前向自动微分, 反向传播算法...")
st.markdown("新能源—负荷长序列预测, 综合能源系统规划设计, 综合能源系统优化控制, 机器学习回归任务, 机器学习分类任务, 机器学习聚类任务...")
st.markdown("软件开发, 硬件设计, 算法实现, Vue框架, SpringBoot框架, PyQt5框架, Streamlit框架, JAX框架, PyTorch框架...")
st.markdown("C语言, C++, Python, Java, Java Web...")


# 研究论文

st.success("Research Articles")
st.caption("已发表")
st.markdown("[1] **H.Zhang**, W.Peng. Time Series Forecasting Based on Interval Type-2 Fuzzy Logic System with PSO, 2021 China Automation Congress (CAC), Beijing, China, 2021, pp. 3090-3097, doi: 10.1109/CAC53003.2021.9727414. ***EI***")
st.markdown("[2] **H.Zhang**, B.Sun .et al. Interval Type-2 Fuzzy Logic System Based on Batch Normalization and Uniform Regularization with Application to Time Series Forecasting, 2023 China Automation Congress (CAC), Chongqing, China, 2023. ***EI***")
st.markdown("[3] **H.Zhang**, B.Sun and W.Peng*. A novel hybrid deep fuzzy model based on gradient descent algorithm with application to time series forecasting, ***Expert Systems with Applications***, 2023, doi:10.1016/j.eswa.2023.121988, ***SCI-Q1***, ***TOP***, IF=8.5")
st.caption("已投稿")
st.markdown("[4] L.Zhang, **H.Zhang**, F.Li and B.Sun*. Bi-level Optimal Design of Integrated Energy System with Synergy of Renewables, Conversion, Storage and Demand, ***IEEE TRANSACTIONS ON INDUSTRY APPLICATIONS***, SCI-Q2, IF=4.4")
st.header("待投稿")
st.markdown("[5] **H.Zhang**, W.Peng*. Mini-Batch Forward Automatic Differentiation based on Efficient Adaptive Optimization Algorithm for TSK Fuzzy Systems, ***IEEE TRANSACTIONS ON FUZYY SYSTEMS***, SCI-Q1, ***TOP***, IF=11.9")
st.markdown("[6] H.Ming, **H.Zhang**, N.Cui*. Battery life estimation method based on forward adaptive width learning, ***Energy***, SCI-Q1, ***TOP***, IF=9")
st.caption("进行中")
st.markdown("[7] MR.Qi, **H.Zhang**, XY.Li*. ***International Journal of Nursing Studies***, SCI-Q1, ***TOP***, IF=8.1")
st.markdown("[8] JW.Zhu, **H.Zhang**, H.Jiang*. ***LWT***, SCI-Q1, ***TOP***, IF=6")
st.markdown("[9] **H.Zhang**, L.Zhang, B.Sun*. ***Engineering Applications Of Artificial Intelligence***, SCI-Q2, ***TOP***, IF=8")
st.markdown("[10] **H.Zhang**, LZ.Zhang, B.Sun*. ***IEEE TRANSACTIONS ON SMART GRID***, SCI-Q1, ***TOP***, IF=9.6")
st.markdown("[11] **H.Zhang**, B.Sun*. ***NATURE METHODS***, SCI-Q1, ***TOP***, IF=48")


st.success("Patent")
st.caption("已投稿")
st.markdown("[1] 孙波, **张辉**, 张立志, 一种集成结构—容量—运行的综合能源系统架构搜索方法, ***国家发明专利***")
st.caption("待投稿")
st.markdown("[2] 孙波, **张辉**, 一种适用于氢气泄漏扩散路径演化问题的物理约束指导的建模框架及系统, ***国家发明专利***")
st.markdown("[1] 孙波, 李志龙, **张辉**, 一种基于物理信息神经网络的供热管网建模方法, ***国家发明专利***")
st.markdown("[1] 孙波, 张良, **张辉**, 基于改进自适应物理信息网络的综合能源系统数字孪生建模方法, ***国家发明专利***")
            
st.success("Standard")
st.markdown(
    "[1] 潘凤文, 孙波, 张立志, 张全军, 刘洋, **张辉**, 吴睿, 杨锋, 王迎波, 秦顺顺, 冯美丽, 含氢分布式综合能源系统运行优化指南, ***地方/行业标准***")

st.success("Participate In Projects")
st.markdown(
    "[1] **国家重点研发计划项目**, 管道氢气在城镇供能领域关键技术研究与规模应用, **项目骨干**, 经费**5.15亿**元")
st.markdown(
    "[2] **国家重点研发计划项目**, 氢能多场景深度融合及智慧管控技术研究与示范应用, **项目骨干**, 经费**2.05亿**元")
st.markdown("[3] **国家电网科技项目**, 多能互补综合能源系统协同优化控制研究, **项目骨干**, 经费**300万**元")

col1, col2, col3, col4 = st.columns([1, 1, 1, 1.5])

with col3:
    image = Image.open(r'./Resource/4.png')
    st.image(image)

col1, col2, col3, col4 = st.columns([1, 1, 1.1, 1.5])

with col3:
    st.caption('Copyright @ 2023, 山东大学 中国·济南')
