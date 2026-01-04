import streamlit as st
import math

# --- 1. 完整保留原本的函數與數據 (完全未動) ---

def Spower(power,c,d,buffatk,buffdef,criticle,light,typatk,typem,typdef,status,buff,debuff,plus,move):
    listdamage=[]
    c*=buffatk ; d*=buffdef
    inner=math.floor(22*power*c/d)
    base=math.floor(inner/72)+2
    damagemin=math.floor(base*0.85)
    damagemax=math.floor(base*1)
    if criticle==True:
        damagemin*=1.5 ; damagemax*=1.5
        light=False
    if light==True:
        damagemin=damagemin*2/3 ;  damagemax=damagemax*2/3 
    if buff==True:
        damagemin*=2 ; damagemax*=2
    if debuff==True:
        damagemin/=2 ; damagemax/=2   
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    dmin=damagemin ; dmax=damagemax
    if typem==typatk[0] or (len(typatk)>1 and typem==typatk[1]):   
       damagemin=math.floor(damagemin*1.5) ; damagemax=math.floor(damagemax*1.5)
    for k in  range(0,len(typdef)):
            if typem=="normal":
                if item1=="一般寶石":
                     damagemin*=1.2 ; damagemax*=1.2                  
                if typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="fighting":
                if item1=="黑帶":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["normal", "steel", "rock", "ice", "dark"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "bug", "flying", "psychic", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="flying":
                if item1=="銳利鳥嘴":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["fighting", "bug", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["rock", "steel", "thunder"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="poison":
                if item1=="毒針":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["grass", "fairy"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "ground", "rock", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="steel":
                     damagemin*=0 ; damagemax*=0
            elif typem=="ground":
                if item1=="柔軟沙子":
                     damagemin*=1.2 ; damagemax*=1.2
                if move=="千箭齊發":
                    if "flying" in typdef: continue
                elif typdef[k] in ["poison", "rock", "steel", "fire", "electric"]:
                    damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["bug", "grass"]:
                    damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="flying":
                    damagemin*=0 ; damagemax*=0
            elif typem=="rock":
                if item1=="硬石頭":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["flying", "bug", "fire", "ice"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "ground", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="bug":
                if item1=="銀粉":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["dark", "psychic", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "flying", "poison", "steel", "fire", "fairy", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="ghost":
                if item1=="詛咒之符":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k]=="dark":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="normal":
                     damagemin*=0 ; damagemax*=0
            elif typem=="steel":
                 if item1=="金屬膜":
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ice", "fairy", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["electric", "fire", "water", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="water":
                 if item1=="神秘水滴":
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "fire", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "water"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="grass":
                 if item1=="奇跡種子":
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "water", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "fire", "steel", "flying", "bug", "poison"]: 
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fire":
                  if item1=="木炭":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["grass", "ice", "bug", "steel"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["fire", "dragon", "water", "rock"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="electric":
                  if item1=="磁鐵":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["water", "flying"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["electric", "dragon", "grass"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k]=="ground":
                     damagemin*=0 ; damagemax*=0
            elif typem=="psychic":
                  if item1=="彎曲的湯匙":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["fighting", "poison"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["steel", "psychic"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k]=="dark":
                      damagemin*=0 ; damagemax*=0
            elif typem=="dragon":
                  if item1=="龍之牙":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k]=="dragon":
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k]=="fairy":
                     if move!="歸無之光":
                        damagemin*=0 ; damagemax*=0 
            elif typem=="ice":
                  if item1=="不融冰":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["flying", "ground", "dragon", "grass"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k]=="water":
                      if move=="冷凍乾燥":
                         damagemin*=2 ; damagemax*=2
                      else:
                         damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k] in ["steel", "fire", "ice"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="dark":
                  if item1=="黑色眼鏡":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["dark", "fighting", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fairy":
                  if item1=="妖精之羽":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["dragon", "dark", "fighting"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["steel", "poison", "fire"]:
                     damagemin*=0.5 ; damagemax*=0.5     
          
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    if plus==True:
        if damagemin>(dmin*1.7) and damagemax>(dmax*1.7):
            damagemin*=1.3 ; damagemax*=1.3
        else:
            damagemin*=1.2 ; damagemax*=1.2
    listdamage.append(damagemin) ; listdamage.append(damagemax)
    return listdamage

def Ppower(power,a,b,buffatk,buffdef,criticle,reflect,typatk,typem,typdef,status,buff,debuff,plus,move):
    listdamage=[]
    a*=buffatk ; b*=buffdef
    inner=math.floor(22*power*a/b)
    base=math.floor(inner/72)+2
    damagemin=math.floor(base*0.85)
    damagemax=math.floor(base*1)
    if criticle==True:
        damagemin*=1.5 ; damagemax*=1.5
        reflect=False
    if reflect==True:
        damagemin=damagemin*2/3 ;  damagemax=damagemax*2/3
    if status==True:
        damagemin*=0.5 ; damagemax*=0.5
    if buff==True:
        damagemin*=2 ; damagemax*=2
    if debuff==True:
        damagemin/=2 ; damagemax/=2
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    dmin=damagemin ; dmax=damagemax
    if typem==typatk[0] or (len(typatk)>1 and typem==typatk[1]):
       damagemin=math.floor(damagemin*1.5) ; damagemax=math.floor(damagemax*1.5)
    
    for k in  range(0,len(typdef)):
            if typem=="normal":
                if item1=="一般寶石":
                     damagemin*=1.2 ; damagemax*=1.2                  
                if typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="fighting":
                if item1=="黑帶":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["normal", "steel", "rock", "ice", "dark"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "bug", "flying", "psychic", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="flying":
                if item1=="銳利鳥嘴":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["fighting", "bug", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["rock", "steel", "thunder"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="poison":
                if item1=="毒針":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["grass", "fairy"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "ground", "rock", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="steel":
                     damagemin*=0 ; damagemax*=0
            elif typem=="ground":
                if item1=="柔軟沙子":
                     damagemin*=1.2 ; damagemax*=1.2
                if move=="千箭齊發":
                    if "flying" in typdef: continue
                elif typdef[k] in ["poison", "rock", "steel", "fire", "electric"]:
                    damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["bug", "grass"]:
                    damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="flying":
                    damagemin*=0 ; damagemax*=0
            elif typem=="rock":
                if item1=="硬石頭":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["flying", "bug", "fire", "ice"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "ground", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="bug":
                if item1=="銀粉":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["dark", "psychic", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "flying", "poison", "steel", "fire", "fairy", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="ghost":
                if item1=="詛咒之符":
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k]=="dark":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="normal":
                     damagemin*=0 ; damagemax*=0
            elif typem=="steel":
                 if item1=="金屬膜":
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ice", "fairy", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["electric", "fire", "water", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="water":
                 if item1=="神秘水滴":
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "fire", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "water"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="grass":
                 if item1=="奇跡種子":
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "water", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "fire", "steel", "flying", "bug", "poison"]: 
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fire":
                  if item1=="木炭":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["grass", "ice", "bug", "steel"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["fire", "dragon", "water", "rock"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="electric":
                  if item1=="磁鐵":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["water", "flying"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["electric", "dragon", "grass"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k]=="ground":
                     damagemin*=0 ; damagemax*=0
            elif typem=="psychic":
                  if item1=="彎曲的湯匙":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["fighting", "poison"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["steel", "psychic"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k]=="dark":
                      damagemin*=0 ; damagemax*=0
            elif typem=="dragon":
                  if item1=="龍之牙":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k]=="dragon":
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k]=="fairy":
                     if move!="歸無之光":
                        damagemin*=0 ; damagemax*=0 
            elif typem=="ice":
                  if item1=="不融冰":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["flying", "ground", "dragon", "grass"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k]=="water":
                      if move=="冷凍乾燥":
                         damagemin*=2 ; damagemax*=2
                      else:
                         damagemin*=0.5 ; damagemax*=0.5 
                  elif typdef[k] in ["steel", "fire", "ice"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="dark":
                  if item1=="黑色眼鏡":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["dark", "fighting", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fairy":
                  if item1=="妖精之羽":
                     damagemin*=1.2 ; damagemax*=1.2
                  if typdef[k] in ["dragon", "dark", "fighting"]:
                     damagemin*=2 ; damagemax*=2
                  elif typdef[k] in ["steel", "poison", "fire"]:
                     damagemin*=0.5 ; damagemax*=0.5
    if plus==True:
        if damagemin>(dmin*1.7) and damagemax>(dmax*1.7):
            damagemin*=1.3 ; damagemax*=1.3
        else:
            damagemin*=1.2 ; damagemax*=1.2
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    listdamage.append(damagemin) ; listdamage.append(damagemax)
    return listdamage

pokemon={"噴火龍":[78,84,78,109,85,100,["fire","flying"]],"巨沼怪":[100,110,90,85,90,65,["water","ground"]],"巨鉗螳螂":[70,130,100,55,80,65,["bug","steel"]],
                     "龍頭地鼠":[110,130,60,50,65,88,["ground","steel"]],"賽富豪": [87, 60, 95, 133, 91, 84, ["steel", "ghost"]],"烈咬陸鯊": [108, 130, 95, 80, 85, 102, ["dragon", "ground"]],
                     "水伊布": [130, 65, 60, 110, 95, 65, ["water", "none"]],"冰伊布": [65, 60, 110, 130, 95, 65, ["ice", "none"]]}
Move={"熱風":["s","fire",95],"爆炸烈焰":["s","fire",150],"日光束":["s","grass",120],"近身戰":["p","fighting",120],"暴風":["s","flying",110],"大字爆炎":["s","fire",110]}
Item=["無","絲綢圍巾","黑帶","銳利鳥嘴","毒針","柔軟沙子","硬石頭","銀粉","詛咒之符","金屬膜","木炭", "神秘水滴","奇跡種子","磁鐵","彎曲的湯匙","不融冰","龍之牙","黑色眼鏡",
            "妖精之羽","生命寶珠","達人帶","力量頭帶","博識眼鏡","突擊背心"]

# 25種性格對應表
nature_effects = {
    "怕寂寞 (Lonely):攻擊↑ 防禦↓": ("A", "B"),"固執 (Adamant):攻擊↑ 特攻↓": ("A", "C"),"頑皮 (Naughty):攻擊↑ 特防↓": ("A", "D"),"勇敢 (Brave):攻擊↑ 速度↓": ("A", "S"), 
    "大膽 (Bold):防禦↑ 攻擊↓": ("B", "A"),"淘氣 (Impish):防禦↑ 特攻↓": ("B", "C"),"樂天 (Lax):防禦↑ 特防↓": ("B", "D"),"悠閒 (Relaxed):防禦↑ 速度↓": ("B", "S"),
    "內斂 (Modest):特攻↑ 攻擊↓": ("C", "A"), "慢吞吞 (Mild):特攻↑ 防禦↓": ("C", "B"),"馬虎 (Rash):特攻↑ 特防↓": ("C", "D"),"冷靜 (Quiet):特攻↑ 速度↓": ("C", "S"),
    "溫和 (Calm):特防↑ 攻擊↓": ("D", "A"), "溫順 (Gentle):特防↑ 防禦↓": ("D", "B"),"慎重 (Careful):特防↑ 特攻↓": ("D", "C"),"自大 (Sassy):特防↑ 速度↓": ("D", "S"),
    "膽小 (Timid):速度↑ 攻擊↓": ("S", "A"), "急躁 (Hasty):速度↑ 防禦↓": ("S", "B"),"爽朗 (Jolly):速度↑ 特攻↓": ("S", "C"), "天真 (Naive):速度↑ 特防↓": ("S", "D"),
    "認真 (Serious):不變": ("-", "-"), "害羞 (Bashful):不變": ("-", "-"),"浮躁 (Quirky):不變": ("-", "-"),"勤奮 (Hardy):不變": ("-", "-"),"坦率 (Docile):不變": ("-", "-")
          
}

# --- 2. Streamlit 介面渲染 ---

st.set_page_config(page_title="Pokémon ZA 傷害計算器", layout="wide")
st.title("⚔️ Pokémon ZA 傷害計算器")

# 側邊欄設定
st.sidebar.header("⚙️ 詳細數值設定")

def get_stats_input(prefix):
    st.sidebar.subheader(f"{prefix}方設定")
    selected_nature = st.sidebar.selectbox(f"{prefix}性格", list(nature_effects.keys()), key=f"nat_{prefix}")
    
    # 性格修正邏輯
    n_mod = {"A":1.0, "B":1.0, "C":1.0, "D":1.0, "S":1.0}
    up, down = nature_effects[selected_nature]
    if up != "-": n_mod[up] = 1.1
    if down != "-": n_mod[down] = 0.9

    col_iv, col_ev = st.sidebar.columns(2)
    ivs = {k: col_iv.number_input(f"{k} 個體", 0, 31, 31, key=f"iv_{prefix}_{k}") for k in ["H", "A", "B", "C", "D", "S"]}
    evs = {k: col_ev.number_input(f"{k} 努力", 0, 252, 0, key=f"ev_{prefix}_{k}") for k in ["H", "A", "B", "C", "D", "S"]}
    
    return ivs, evs, n_mod

iv_atk, ev_atk, n_atk = get_stats_input("攻擊")
iv_def, ev_def, n_def = get_stats_input("防守")

# 固定等級為 50
LvAtk = 50
LvDef = 50

# 主畫面選擇
c1, c2 = st.columns(2)
with c1:
    pa = st.selectbox("選擇攻擊方寶可夢", list(pokemon.keys()))
    item1 = st.selectbox("攻擊方道具", Item)
    move_name = st.selectbox("選擇招式", list(Move.keys()))
    criticlehit = st.checkbox("擊中要害 (Crit)")
    Plus = st.checkbox("是否要Plus (C+)?")

with c2:
    pd = st.selectbox("選擇防守方寶可夢", list(pokemon.keys()))
    item2 = st.selectbox("防守方道具", Item)
    Reflection = st.checkbox("反射壁 (物理減半)")
    Lightscreen = st.checkbox("光牆 (特殊減半)")
    is_burn = st.checkbox("攻擊方處於灼傷狀態")

# 計算能力值 (公式完全保留)
def calc_stat(base, iv, ev, lv, nature_mod, is_hp=False):
    if is_hp:
        return int((((math.floor(base*2+iv+(ev/4)))*lv)/100)+10+lv)
    else:
        return int(((((math.floor(base*2+iv+(ev/4)))*lv)/100)+5)*nature_mod)

# 建立原始數據結構以配合原本函數
abAtk = {
    "H": calc_stat(pokemon[pa][0], iv_atk["H"], ev_atk["H"], LvAtk, 1, True),
    "A": calc_stat(pokemon[pa][1], iv_atk["A"], ev_atk["A"], LvAtk, n_atk["A"]),
    "B": calc_stat(pokemon[pa][2], iv_atk["B"], ev_atk["B"], LvAtk, n_atk["B"]),
    "C": calc_stat(pokemon[pa][3], iv_atk["C"], ev_atk["C"], LvAtk, n_atk["C"]),
    "D": calc_stat(pokemon[pa][4], iv_atk["D"], ev_atk["D"], LvAtk, n_atk["D"]),
    "S": calc_stat(pokemon[pa][5], iv_atk["S"], ev_atk["S"], LvAtk, n_atk["S"]),
    "Type": pokemon[pa][6]
}

abDef = {
    "H": calc_stat(pokemon[pd][0], iv_def["H"], ev_def["H"], LvDef, 1, True),
    "A": calc_stat(pokemon[pd][1], iv_def["A"], ev_def["A"], LvDef, n_def["A"]),
    "B": calc_stat(pokemon[pd][2], iv_def["B"], ev_def["B"], LvDef, n_def["B"]),
    "C": calc_stat(pokemon[pd][3], iv_def["C"], ev_def["C"], LvDef, n_def["C"]),
    "D": calc_stat(pokemon[pd][4], iv_def["D"], ev_def["D"], LvDef, n_def["D"]),
    "S": calc_stat(pokemon[pd][5], iv_def["S"], ev_def["S"], LvDef, n_def["S"]),
    "Type": pokemon[pd][6]
}

# 觸發計算
if st.button("🔮 執行計算", use_container_width=True):
    move = Move[move_name]
    if move[0] == "s":
        listdamage = Spower(move[2], abAtk["C"], abDef["D"], 1, 1, criticlehit, Lightscreen, abAtk["Type"], move[1], abDef["Type"], is_burn, False, False, Plus, move_name)
    else:
        listdamage = Ppower(move[2], abAtk["A"], abDef["B"], 1, 1, criticlehit, Reflection, abAtk["Type"], move[1], abDef["Type"], is_burn, False, False, Plus, move_name)

    # 結果輸出區
    st.divider()
    permin = listdamage[0]/abDef["H"]
    permax = listdamage[1]/abDef["H"]
    
    st.subheader(f"📊 {pa} 對 {pd} 的傷害分析")
    st.write(f"對手 HP: {abDef['H']} | 造成傷害: **{listdamage[0]} ~ {listdamage[1]}**")
    st.write(f"傷害百分比: **{permin:.1%} ~ {permax:.1%}**")

    # 擊殺判斷邏輯
    if permin >= 1:
        st.success("🏆 確定一擊擊倒 (確一)")
    elif permin < 1 and permax >= 1:
        killper = (listdamage[1]-abDef["H"])/(listdamage[1]-listdamage[0]) if listdamage[1] != listdamage[0] else 1.0
        st.warning(f"🎲 亂數一擊擊倒 (擊殺率: {killper:.1%})")
    elif permin >= 0.5:
        st.info("🎯 確定二擊擊倒 (確二)")
    elif permax >= 0.5:
        st.info("⚖️ 亂數二擊擊倒 (亂二)")
    else:
        st.error("📉 傷害不足 (不夠痛)")

    with st.expander("查看實際能力面板 (Lv.50)"):
        st.write("攻擊方:", abAtk)
        st.write("防守方:", abDef)
