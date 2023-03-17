#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

select = st.selectbox("最初に絶対えらぼう", ("物理武器", "属性武器", ))
kisoct = st.number_input("基礎CT",min_value=0.0,step=0.1,format="%.1f")
level = st.number_input("レベル",min_value=0,step=1)
agi  = st.number_input("敏捷",min_value=0,step=1,help="ステータス画面に表示されている敏捷")
ss = st.number_input("攻撃速度or詠唱速度",min_value=0,step=1,help="ステータス画面に表示されている詠唱速度")
ssp = st.number_input("攻撃速度(%)or詠唱速度(%)",min_value=0,step=1,help="ペット・ルーン・パッシブの合計を入力。ペット14%,ルーン5%,パッシブ15%なら34を入力")
ctgen = st.number_input("スキルによるCT減少(%)",min_value=0,step=1,help="スキルによるCT減少を入力。コンダクターのスパークチャージLv5なら30を入力")
add = st.number_input("追加の敏捷・攻撃速度or詠唱速度",min_value=0,step=1,help="敏捷か詠唱が増えたらどうなるかチェック用。例)熟練で敏捷が60増えたらどうなるかな？等")
addp = st.number_input("追加の攻撃速度(%)or詠唱速度(%)",min_value=0,step=1,help="詠唱速度(%)が増えたらどうなるかチェック用。例)2%のルーンをはったらどうなるかな？等")

if st.button("計算"):
    if select == "物理武器":
        dssp = 1 + ssp/100    
        dss = ss/dssp - agi/2
        daddssp = addp/100
        dctgen = ctgen/100
        ct = round(kisoct*(1-(((agi+dss+add)*(dssp+daddssp))/(level*0.4+1))*0.01-dctgen),2)
        nadd = (level*0.4+1) * (1 - 0.8/kisoct - dctgen) / (0.01*(dssp+daddssp)) - dss - add-agi
        nssp  = ((level*0.4+1) * (1 - 0.8/kisoct - dctgen) / (0.01 * (agi + dss+add)) - dssp - daddssp)*100
    elif select == "属性武器":
        dssp = 1 + ssp/100    
        dss = ss/dssp
        daddssp = addp/100
        dctgen = ctgen/100
        ct = round(kisoct*(1-(((dss+add)*(dssp+daddssp))/(level*0.4+1))*0.01-dctgen),2)
        nadd = round((level*0.4+1) * (1 - 0.8/kisoct - dctgen) / (0.01*(dssp+daddssp)) - dss - add,0)
        nssp  = round(((level*0.4+1) * (1 - 0.8/kisoct - dctgen) / (0.01 * (dss+add)) - dssp - daddssp)*100,0)
    
    st.write("減少後CT",round(ct,2))
    st.write("必要な敏捷or攻撃速度or詠唱速度",int(nadd))
    st.write("必要な攻撃速度(%)or詠唱速度(%)",int(nssp))

