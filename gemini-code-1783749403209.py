import streamlit as st

# 페이지 설정
st.set_page_config(page_title="국어과 서·논술형 형성평가 시스템", layout="wide")

# 세션 상태 초기화 (처음부터 다시 풀기 기능용)
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# 타이틀 및 안내
st.title("국어과 서·논술형 형성평가 및 자동 채점 시스템")
st.markdown("---")

# ---------------------------------------------------------------------------
# [자료실] 지문 및 데이터 세팅
# ---------------------------------------------------------------------------
set1_keywords = {
    "target_a": ["인공지능", "ai", "인공 지능"],
    "target_b": ["딥러닝", "딥 러닝", "인공신경망"],
    "target_c": ["머신러닝", "기계학습", "기계 학습"],
    "content_all": ["인공지능", "ai", "딥러닝", "머신러닝", "기계학습", "데이터", "학습", "컴퓨터"]
}

# 1. 자료 (파란 상자 안에 배치)
st.info("""
### 읽기 자료: 다음 글을 읽고 문항에 답하시오.

인공지능(AI)의 발전과 머신러닝, 딥러닝의 구조적 관계 및 영상 매체 활용에 대한 글이 제시되어 있다고 가정합니다.

- 핵심 정의: 인공지능이란 인간의 지능적 행동을 컴퓨터로 구현하는 기술을 뜻한다.
- 하위 분류: 인공지능은 포함 관계에 따라 머신러닝과 딥러닝으로 구분할 수 있다.
- 매체 특성: 어려운 과제나 복잡한 지식을 전달할 때는 시청자의 인지 과부하를 줄이기 위해 차분하고 집중되는 환경을 조성하는 복합양식성 연출이 필요하다.
""")

st.write("")
st.subheader("1번 세트: 서·논술형 답안 작성 연습")
st.write("")

# ---------------------------------------------------------------------------
# [서·논술형 1] 표 빈칸 채우기 문항
# ---------------------------------------------------------------------------
# 2. 문제 발문 (바탕 텍스트로 분리)
st.write("서·논술형 1: 다음은 윗글의 내용을 바탕으로 정리한 표입니다. 빈칸 ㉠, ㉡, ㉢에 들어갈 알맞은 단어를 찾아 쓰시오. (각 1점, 총 3점)")

# 3. 조건 (회색 박스 및 이모지 배치)
st.markdown("""
<div style="background-color: #f0f2f6; padding: 15px; border-radius: 5px; margin-bottom: 15px;">
    📌 지문에 명시된 어구를 바탕으로 정확한 개념어를 찾아 작성해야 합니다.<br>
    📌 문맥상 통하는 유사 표현이나 조사가 붙은 경우도 정답 범위로 인정됩니다.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    ans_1_1 = st.text_input("㉠ 입력란", placeholder="지문 속 단어 추출").strip()
with col2:
    ans_1_2 = st.text_input("㉡ 입력란", placeholder="지문 속 단어 추출").strip()
with col3:
    ans_1_3 = st.text_input("㉢ 입력란", placeholder="지문 속 단어 추출").strip()

st.markdown("---")

# ---------------------------------------------------------------------------
# [서·논술형 2] 설명 방법 문장 쓰기 문항
# ---------------------------------------------------------------------------
# 2. 문제 발문 (바탕 텍스트로 분리)
st.write("서·논술형 2: 윗글에 제시된 내용만을 활용하여 서로 다른 2가지의 설명 방법을 사용한 문장을 각각 작성하시오. (각 2.5점, 총 5점)")

# 3. 조건 (회색 박스 및 이모지 배치)
st.markdown("""
<div style="background-color: #f0f2f6; padding: 15px; border-radius: 5px; margin-bottom: 15px;">
    ⚠️ 반드시 윗글에 제시된 내용만을 활용하여 서술해야 합니다.<br>
    ⚠️ 문장 (1)과 문장 (2)에 동일한 설명 방법을 중복하여 사용할 수 없습니다.<br>
    🚨 괄호 안에 선택한 설명 방법의 명칭과 실제 문장의 서술 방식(형식적 속성)이 반드시 일치해야 합니다.
</div>
""", unsafe_allow_html=True)

method_options = ["선택하세요", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"]

c1, c2 = st.columns(2)
with c1:
    st.write("문장 (1)")
    choice_1 = st.selectbox("설명 방법 선택 (1)", method_options, key="choice1")
    ans_2_1 = st.text_area("문장 (1) 답안 작성", placeholder="예: ~란 ~이다 형식을 준수하여 작성", key="ans21").strip()

with c2:
    st.write("문장 (2)")
    choice_2 = st.selectbox("설명 방법 선택 (2)", method_options, key="choice2")
    ans_2_2 = st.text_area("문장 (2) 답안 작성", placeholder="선택 (1)과 다른 설명 방법을 사용하여 서술", key="ans22").strip()

st.markdown("---")

# ---------------------------------------------------------------------------
# [서·논술형 3] 영상 기획안 및 효과 서술 문항
# ---------------------------------------------------------------------------
# 2. 문제 발문 (바탕 텍스트로 분리)
st.write("서·논술형 3: 윗글에 제시된 개념적 특성을 반영하여, 이를 설명하는 영상 매체의 시각 요소(Ⓐ)와 청각 요소(Ⓑ)를 기획하고, 그에 따른 효과를 본문 근거를 들어 서술하시오. (총 6점)")

# 3. 조건 (회색 박스 및 이모지 배치)
st.markdown("""
<div style="background-color: #f0f2f6; padding: 15px; border-radius: 5px; margin-bottom: 15px;">
    🔍 시각 요소와 청각 요소 기획은 지문 속 개념의 속성과 분위기를 충족해야 합니다.<br>
    🎯 효과 서술 시 주관적 감상이 아닌 본문에 기반한 구체적인 사실 근거를 포함해야 합니다.<br>
    🔗 앞서 기획한 시각·청각 요소의 연출 내용과 효과 서술이 논리적(인과적)으로 연결되어야 합니다.
</div>
""", unsafe_allow_html=True)

ans_3_a = st.text_input("Ⓐ 시각 요소 기획 (2점)", placeholder="예: 화면에 핵심 키워드 자막을 크게 배치한다.").strip()
ans_3_b = st.text_input("Ⓑ 청각 요소 기획 (2점)", placeholder="예: 차분한 톤의 내레이션을 깔아 연출한다.").strip()
ans_3_effect = st.text_area("연출 효과 서술 (2점)", placeholder="예: 지문의 근거를 바탕으로 연출 효과를 인과적으로 서술").strip()

st.markdown("---")

# ---------------------------------------------------------------------------
# 채점 로직 및 실행 엔진
# ---------------------------------------------------------------------------
if st.button("답안 제출 및 자동 채점하기", type="primary"):
    st.session_state.submitted = True
    
    score_1 = 0
    score_2 = 0
    score_3 = 0
    
    feedback_1 = []
    feedback_2 = []
    feedback_3 = []
    
    # [서·논술형 1] 채점
    if any(k in ans_1_1.lower() for k in set1_keywords["target_a"]) if ans_1_1 else False: score_1 += 1
    else: feedback_1.append("빈칸 ㉠: 필수 핵심 개념어가 누락되었거나 지문 외 단어입니다.")
        
    if any(k in ans_1_2.lower() for k in set1_keywords["target_b"]) if ans_1_2 else False: score_1 += 1
    else: feedback_1.append("빈칸 ㉡: 개념의 구조적 선후 관계나 대상어가 일치하지 않습니다.")
        
    if any(k in ans_1_3.lower() for k in set1_keywords["target_c"]) if ans_1_3 else False: score_1 += 1
    else: feedback_1.append("빈칸 ㉢: 지문에서 분류한 핵심 제재가 아닙니다.")

    # [서·논술형 2] 채점
    triggers = {
        "정의": ["란", "이다", "의미한다", "뜻한다"],
        "예시": ["예를 들어", "예로", "등이 있다", "사례", "예시"],
        "인과": ["때문에", "왜냐하면", "원인은", "결과로", "하므로"],
        "분석": ["구성되다", "이루어지다", "요소", "부품", "구조"],
        "비교와 대조": ["공통점", "차이점", "달리", "비해", "반면"],
        "분류와 구분": ["나뉘다", "구분되다", "종류", "유형", "묶다"]
    }
    
    if choice_1 == "선택하세요" or choice_2 == "선택하세요":
        feedback_2.append("오답 사유: 설명 방법 명칭을 모두 선택해야 합니다.")
    elif choice_1 == choice_2:
        feedback_2.append(f"자동 오답 처리: 서로 다른 2가지 방법을 써야 하나, 동일한 항목을 중복 선택했습니다.")
    else:
        # 문장 (1) 검증
        has_content_1 = any(k in ans_2_1 for k in set1_keywords["content_all"])
        has_trigger_1 = any(t in ans_2_1 for t in triggers[choice_1])
        wrong_concept_1 = False
        for alt_method, alt_trigs in triggers.items():
            if alt_method != choice_1 and any(at in ans_2_1 for at in alt_trigs) and not has_trigger_1:
                wrong_concept_1 = True
        
        if not has_content_1: feedback_2.append("문장 (1) 오답: 윗글에 제시된 핵심 내용을 활용하지 않았습니다.")
        elif not has_trigger_1 or wrong_concept_1: feedback_2.append(f"문장 (1) 오답: 선택한 명칭의 서술 특성이 문장에 나타나지 않았거나 타 개념과 혼동했습니다.")
        else: score_2 += 2.5
            
        # 문장 (2) 검증
        has_content_2 = any(k in ans_2_2 for k in set1_keywords["content_all"])
        has_trigger_2 = any(t in ans_2_2 for t in triggers[choice_2])
        wrong_concept_2 = False
        for alt_method, alt_trigs in triggers.items():
            if alt_method != choice_2 and any(at in ans_2_2 for at in alt_trigs) and not has_trigger_2:
                wrong_concept_2 = True
                
        if not has_content_2: feedback_2.append("문장 (2) 오답: 윗글에 제시된 핵심 내용을 활용하지 않았습니다.")
        elif not has_trigger_2 or wrong_concept_2: feedback_2.append(f"문장 (2) 오답: 선택한 명칭의 서술 특성이 문장에 나타나지 않았거나 타 개념과 혼동했습니다.")
        else: score_2 += 2.5

    # [서·논술형 3] 채점
    visual_ok = any(word in ans_3_a for word in ["자막", "화면", "이미지", "시각", "영상", "그래프", "띄우다", "보여준다"])
    audio_ok = any(word in ans_3_b for word in ["음악", "소리", "내레이션", "효과음", "목소리", "톤", "틀다", "재생"])
    has_ground = any(g in ans_3_effect for g in ["지문", "본문", "언급", "과부하", "집중", "어려운"])
    has_link = any(l in ans_3_effect for l in ["통해", "효과", "인해", "만든다", "돕는다"])
    
    if visual_ok: score_3 += 2.0
    else: feedback_3.append("시각 요소: 지문 속 개념의 분위기를 구현할 구체적 매체 표현이 부족합니다.")
        
    if audio_ok: score_3 += 2.0
    else: feedback_3.append("청각 요소: 음악의 템포, 톤 등 청각 양식을 자극하는 서술이 누락되었습니다.")
        
    if has_ground and has_link: score_3 += 2.0
    else:
        if not has_ground: feedback_3.append("연출 효과: 본문에 기반한 구체적인 사실 근거가 제시되지 않아 0점 처리됩니다.")
        elif not has_link: feedback_3.append("연출 효과: 기획한 연출 행위와 최종 효과 간의 인과적 연결이 성립하지 않아 0점 처리됩니다.")

    # 4. 피드백 기호 정리 (AI 흔적 제거 및 깔끔한 출력)
    total_score = score_1 + score_2 + score_3
    st.write("")
    st.success(f"채점 결과: 총점 {total_score}점 / 14점 만점")
    
    tab1, tab2, tab3 = st.tabs(["문항 1 결과", "문항 2 결과", "문항 3 결과"])
    
    with tab1:
        st.metric(label="서·논술형 1 점수", value=f"{score_1} / 3 점")
        if feedback_1:
            for f in feedback_1: st.error(f)
        else: st.info("정답입니다. 지문의 사실적 정보를 정확히 찾아 썼습니다.")
            
    with tab2:
        st.metric(label="서·논술형 2 점수", value=f"{score_2} / 5 점")
        if feedback_2:
            for f in feedback_2: st.error(f)
        else: st.info("정답입니다. 명칭과 문장 형식이 완벽히 일치하며 지문 정보가 올바르게 녹아있습니다.")
            
    with tab3:
        st.metric(label="서·논술형 3 점수", value=f"{score_3} / 6 점")
        if feedback_3:
            for f in feedback_3: st.error(f)
        else: st.info("정답입니다. 매체 양식의 속성이 개념과 부합하며, 명확한 본문 근거를 갖춘 완벽한 서술입니다.")

# 복습 레이아웃
if st.session_state.submitted:
    st.markdown("---")
    col_info, col_btn = st.columns([4, 1])
    with col_info:
        st.caption("모든 문제를 제출하면 위 탭에서 틀린 개념 오답 피드백을 확인할 수 있어요. 답안을 초기화하고 다시 풀고 싶다면 오른쪽 버튼을 누르세요.")
    with col_btn:
        if st.button("처음부터 다시 풀기", type="secondary"):
            st.session_state.submitted = False
            st.rerun()
