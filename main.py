

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

st.markdown("人工智能")
st.caption("机器学习, 深度学习, 对比学习, 表征学习, 神经架构搜索, 自动机器学习, 强化学习, 迁移学习, 模糊逻辑, 域适应, 随机特征, 科学机器学习")

st.markdown("神经网络")
st.caption("卷积神经网络(CNN), 长短期记忆网络(LSTM), 残差神经网络(RNN), 宽度学习系统(BLS), Transformer, 物理信息神经网络, 深度置信网络")

st.markdown("模糊逻辑系统")
st.caption("区间二型模糊逻辑系统(IT2-FLS), TSK模糊逻辑系统(TSK-FLS), 深度模糊系统(DFS)")

st.markdown("算法")
st.caption("自适应优化算法, 进化算法(启发式算法), 梯度下降算法, 前向自动微分, 反向传播算法")

st.markdown("其他")
st.caption("随机特征, 泛化性能")

st.markdown("任务")
st.caption("分类, 回归, 聚类, 时间序列预测, 特征工程, 长序列预测(LSTP)")

st.markdown("综合能源系统")
st.caption("新能源—负荷长序列预测, 综合能源系统规划设计, 综合能源系统优化控制")

st.markdown("氢安全")
st.caption("氢气泄漏扩散演化路径建模")

st.markdown("计算机")
st.caption("软件开发, 硬件设计, 算法实现, Vue框架, SpringBoot框架, PyQt5框架, Streamlit框架, JAX框架, PyTorch框架, C语言, C++, Python, Java, JS")


# 研究论文

st.success("Research Articles")
st.markdown("已发表")
st.caption("[1] **H.Zhang**, W.Peng. Time Series Forecasting Based on Interval Type-2 Fuzzy Logic System with PSO, 2021 China Automation Congress (CAC), Beijing, China, 2021, pp. 3090-3097, doi: 10.1109/CAC53003.2021.9727414. ***EI***")
st.caption("[2] **H.Zhang**, B.Sun .et al. Interval Type-2 Fuzzy Logic System Based on Batch Normalization and Uniform Regularization with Application to Time Series Forecasting, 2023 China Automation Congress (CAC), Chongqing, China, 2023. ***EI***")
st.caption("[3] **H.Zhang**, B.Sun and W.Peng*. A novel hybrid deep fuzzy model based on gradient descent algorithm with application to time series forecasting, ***Expert Systems with Applications***, 2023, doi:10.1016/j.eswa.2023.121988, ***SCI-Q1***, ***TOP***, IF=8.5")
st.markdown("已投稿")
st.caption("[4] L.Zhang, **H.Zhang**, F.Li and B.Sun*. Bi-level Optimal Design of Integrated Energy System with Synergy of Renewables, Conversion, Storage and Demand, ***IEEE TRANSACTIONS ON INDUSTRY APPLICATIONS***, SCI-Q2, IF=4.4")
st.markdown("待投稿")
st.caption("[5] **H.Zhang**, W.Peng*. Mini-Batch Forward Automatic Differentiation based on Efficient Adaptive Optimization Algorithm for TSK Fuzzy Systems, ***IEEE TRANSACTIONS ON FUZYY SYSTEMS***, SCI-Q1, ***TOP***, IF=11.9")
st.caption("[6] H.Ming, **H.Zhang**, N.Cui*. Battery life estimation method based on forward adaptive width learning, ***Energy***, SCI-Q1, ***TOP***, IF=9")
st.markdown("进行中")
st.caption("[7] MR.Qi, **H.Zhang**, XY.Li*. ***International Journal of Nursing Studies***, SCI-Q1, ***TOP***, IF=8.1")
st.caption("[8] JW.Zhu, **H.Zhang**, H.Jiang*. ***LWT***, SCI-Q1, ***TOP***, IF=6")
st.caption("[9] **H.Zhang**, L.Zhang, B.Sun*. ***Engineering Applications Of Artificial Intelligence***, SCI-Q2, ***TOP***, IF=8")
st.caption("[10] **H.Zhang**, LZ.Zhang, B.Sun*. ***IEEE TRANSACTIONS ON SMART GRID***, SCI-Q1, ***TOP***, IF=9.6")
st.caption("[11] **H.Zhang**, B.Sun*. ***NATURE METHODS***, SCI-Q1, ***TOP***, IF=48")


st.success("Patent")
st.markdown("已投稿")
st.caption("[1] 孙波, **张辉**, 张立志, 一种集成结构—容量—运行的综合能源系统架构搜索方法, ***国家发明专利***")
st.markdown("待投稿")
st.caption("[2] 孙波, **张辉**, 一种适用于氢气泄漏扩散路径演化问题的物理约束指导的建模框架及系统, ***国家发明专利***")
st.caption("[1] 孙波, 李志龙, **张辉**, 一种基于物理信息神经网络的供热管网建模方法, ***国家发明专利***")
st.caption("[1] 孙波, 张良, **张辉**, 基于改进自适应物理信息网络的综合能源系统数字孪生建模方法, ***国家发明专利***")
            
st.success("Standard")
st.caption("[1] 潘凤文, 孙波, 张立志, 张全军, 刘洋, **张辉**, 吴睿, 杨锋, 王迎波, 秦顺顺, 冯美丽, 含氢分布式综合能源系统运行优化指南, ***地方/行业标准***")



# 项目

st.success("Participate In Projects")

st.markdown("已结题")
st.caption("[1] **国家电网科技项目**, 多能互补综合能源系统协同优化控制研究, **项目骨干**, 经费**300万**元")
st.markdown("在研")
st.caption("[2] **国家重点研发计划项目**, 管道氢气在城镇供能领域关键技术研究与规模应用, **项目骨干**, 经费**5.15亿**元")
st.caption("[3] **国家重点研发计划项目**, 氢能多场景深度融合及智慧管控技术研究与示范应用, **项目骨干**, 经费**2.05亿**元")



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.info("大学经历")

st.caption("张辉，男，汉族，1999年12月生，山东沂水人，中共党员，中国自动化学会会员，信息与电气工程学院物联网工程专业182班，现已保送至山东大学控制科学与工程学院免试攻读硕士学位，曾获得国家奖学金、第二届泉城奖学金等十余项奖学金，以及 “十大自强不息优秀学生”等荣誉称号13项，在专业学习、科技创新和科研方面做出了卓越的成绩，累计获得综合性奖励62项（国家级11项、省级16项、校院级35项）。")

col31, col32 = st.columns([1, 1])
with col31:
    st.markdown("一、坚定信念，筑牢信仰之基")
    st.caption("“行事有为，立信仰之杆”。张辉积极投身于学生工作，一直担任班级副班长兼科创委员一职，曾担任信息楼实验室项目负责人、智能变配电实验室负责人以及信电学院创新基地学生负责人，尽心尽力做好自己的本职工作，积极地带领团队以及组织实验室同学参加科技类竞赛。曾为学院以及物联网工程专业同学作《读万卷书，行万里路——深入领会十九届五中全会精神》等学科竞赛报告六次，相关内容多次被学院、学校公众号推送，并被《大众日报》报导，获得山东建筑大学2020年度“十大自强不息优秀学生”、校优秀学生干部标兵、“建业之星”校级先进个人等荣誉13项。积极向党组织靠拢，于2021年6月23日成为一名预备党员并于2022年6月24日转为中共正式党员，坚定不移的政治信仰使其在工作事务和日常生活中时刻充满热忱。")
    st.markdown("二、夯实学业基础，以格物致知为所求")
    st.caption("“四年前的我，初入校园的迷茫让我像一个渡河的行者丢了满捆的柴火，像那浩瀚的夜空失去了璀璨的星火。可是在银杏叶铺满金黄色的秋色中，一个又一个不懈拼搏的身影又像是灯塔一样，为我指明了方向，他们在路上急匆匆的走着，每个人都怀着自己的希望，每个人都握紧自己的心事”。")
with col32:
    st.caption("“岁月不居，时节如流，“记忆都留给了实验室和图书馆”。在大学期间，张辉连续四年学习成绩（智育）专业排名第一，在2020-2021学年综合测评中以绩点5.528在本专业中排名第一，成为信息与电气工程学院（所有专业、所有年级）最高绩点，在2021年推免研究生中成绩学院排名第一，此外，张辉的毕业论文《基于深度模糊系统方法的多变量时间序列预测方法研究及应用》以2022届信息与电气工程学院最高分获评山东建筑大学2022届优秀学士学位论文。曾获得第二届“泉城奖学金”以及“国家奖学金”、“国家励志奖学金”，是2021年度“校长奖学金”候选人以及首届“泉城奖学金”候选人。")
    st.caption("“四年前的我，初入校园的迷茫让我像一个渡河的行者丢了满捆的柴火，像那浩瀚的夜空失去了璀璨的星火。可是在银杏叶铺满金黄色的秋色中，一个又一个不懈拼搏的身影又像是灯塔一样，为我指明了方向，他们在路上急匆匆的走着，每个人都怀着自己的希望，每个人都握紧自己的心事”。")
col31, col32 = st.columns([1, 1])
with col31:
    st.markdown("三、笃实笃行，躬身实践探索")
    st.caption("“纸上得来终觉浅，绝知此事要躬行”。学习之余，张辉积极参加与专业领域相关的学科竞赛，努力成为一名品学兼优，综合素质过硬，专业素质突出的优秀大学生。")
    st.caption("“在2020年全国大学生电子设计竞赛中获得山东赛区一等奖，最终结果“总谐波失真度值”的检测误差控制在了0.01%以下，三位专家评委测评均为满分；作为项目负责人在iCAN国际创新创业大赛山东赛区获得二等奖，在中国总决赛中获得国家级三等奖；作为项目负责人在中国数字经济优秀项目（大赛）获得三等奖以及春苗奖奖金；作为项目负责人在第七届山东省物联网创造力大赛中获得省级二等奖；在其他科技类竞赛中获得省级一等奖三项，省级二等奖一项，省级三等奖一项，另获诸多校级、院级奖项。")
    st.caption("“每个时代最深的刻痕，总有奋斗者笃行的足迹。在这些成绩的背后，有着太多的辛酸，“我大学二年级第一次进入实验室，在学科竞赛上发奋图强努力了一整年没有成果，成绩大都是大三获得的，深刻体会过努力与付出不成正比的感受，好在没有放弃”。“这苦难与背负的尽头，必然是行云流水的此世光阴”，也正如《百年孤独》中“没有任何理想值得以沉沦作为代价”，当晦暗散尽，终星河长明。")
with col32:
    st.markdown("四、热爱科研，追求卓越")
    st.caption("“一定要爱着点什么，恰似草木对光阴的钟情”。出于对科研的向往以及渴望，张辉参加泰山学者青年专家李成栋教授科研团队的研究工作，积极与团队里老师们展开交流合作，主要针对一些随机性强、预测难度大的问题，提出了一种用于时间序列预测的区间二型模糊逻辑系统，使用粒子群优化算法对所设计的区间二型模糊逻辑系统的参数进行优化，前件和后件隶属函数均选择为标准偏差不确定的高斯隶属函数。在上述研究基础上，作为第一作者发表科研论文《Time Series Forecasting Based on Interval Type-2 Fuzzy Logic System with PSO》(EI，已收录，DOI: 10.1109/CAC53003.2021.9727414)。另外，主持一项课题为《基于实景投影的农药残留检测技术》省级大学生创新创业项目，研究成果已申请国家发明专利《一种手持式智能残留农药检测仪及检测方法》(专利号：202010993963.1)，并获得国家知识产权局公开；主持或参与开放性实验项目课题三项《简易无接触温度测量与身份识别防疫装置》(立项编号：2020yzkf092)、《基于STM32的智能晾衣控制系统》(立项编号：2019yzkf099)、《基于Arduino的创新机器人开发平台》(立项编号：2020yzkf093)，现均已优秀评价结题。")
    st.caption("在深入学习审视物联网相关领域的技术之下，作为第一发明人，张辉撰写《一种基于物联网的快递收发系统》(专利号：202022664124.3)和《一种基于物联网的安防系统》(专利号：202022989514.8)两项实用新型专利并提交国家知识产权局，现均已授权。")


col1, col2, col3, col4 = st.columns([1, 1, 1, 1.5])

with col3:
    image = Image.open(r'./Resource/4.png')
    st.image(image)

col1, col2, col3, col4 = st.columns([1, 1, 1.1, 1.5])

with col3:
    st.caption('Copyright @ 2023, 山东大学 中国·济南')
