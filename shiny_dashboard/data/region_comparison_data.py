# shiny_dashboard/data/region_comparison_data.py

def create_dummy_data():
    # 지원 정책 데이터
    policies = {
        "영천시": {
            "정착지원금": "가구당 500만원(보조 400만원, 자부담 100만원)",
            "주택지원": "경증 및 측산분야 영농규모 확대 및 시설 개보수 등 지원",
            "농지지원": "세대당 최고 3억원 융자지원",
            "교육지원": "금리 1.5%, 5년거치 10년 분할상환",
            "농기계지원": "농지구입, 농업관련시설 등 지원",
            "판로지원": "세대당 최고 7천5백만원 융자지원",
            "컨설팅": "구입, 신축(시업 신청시 본인 소유의 대지 소유지에 한함), 증축, 개축",
            "세금혜택": "주택구입, 신축자금은 나이제한 없음",
            "추가혜택": "농가기술 및 품질관리, 경영마케팅, 창업 등에 필요한 단계별 현장실습교육"
        },
        "의성군": {
            "정착지원금": "가구원 수에 따라 차등 지급(1인 40만원, 2인 60만원, 3인 80만원, 4인 이상 100만원)",
            "주택지원": "주택수리비 지원 가능", 
            "농지지원": "귀농 농업창업 자금 융자 지원", 
            "교육지원": "귀농·영농 교육 8시간 이상 이수 필요",
            "농기계지원": "농기계 임대사업 지원", 
            "판로지원": "소규모 창업 지원",
            "컨설팅": "귀농 영농 활동 증빙 및 컨설팅",
            "세금혜택": "귀농인 대상 세제 혜택",
            "추가혜택": "귀농창업 지원사업(사업비 5백만원, 보조 80%, 자부담 20%)"
        },
        "상주시": {
            "정착지원금": "보조 400만원/자부담 100만원",
            "주택지원": "주택수리비(보조 600만원, 자부담 600만원), 주거임대료 지원(1인 연 120만원~4인 연 300만원)",
            "농지지원": "귀농 농업창업 융자 최대 3억원, 농지임차료 세대당 최대 100만원 지원", 
            "교육지원": "신규농업인 현장실습교육 지원(멘토-멘티 관계 형성)",
            "농기계지원": "농기계 임대료 50% 할인", 
            "판로지원": "귀농인 안정적 정착 지원",
            "컨설팅": "귀농 농업창업 및 주택구입 정책자금 이차보전(당해 납부이자 50% 지원, 세대당 최대 100만원)",
            "세금혜택": "경상북도 농어민수당 상주화폐 60만원(상반기 1회 지급)",
            "추가혜택": "일반 전입지원금(상주화폐 20만원), 학생전입지원금(상주화폐 20만원, 6개월마다 최대 8회), 전입 고등대학교 기숙사비(학기당 30만원 이내)"
        }
    }
    
    # 정책 점수 데이터 (영천시가 더 높게 설정)
    policy_scores = {
        "영천시": {
            "정착지원": 8.5,  # 보조금 비율이 높고 총액 500만원으로 양호
            "주택지원": 7.0,  # 영농규모 확대 및 시설 개보수 지원 제공
            "농지지원": 9.0,  # 최고 3억원 융자 지원으로 높은 점수
            "교육지원": 7.5,  # 금리 조건이 양호하고 상환 기간이 긴 편
            "농기계지원": 7.5,  # 농지 구입과 농업 관련 시설 지원이 포함
            "판로지원": 8.5,  # 높은 융자 한도(7천5백만원)로 점수 높음
            "종합평가": 8.3   # 평균 + 전체적인 프로그램 완성도
        },
        "의성군": {
            "정착지원": 6.5,  # 가구원 수에 따른 차등 지급, 최대 100만원으로 낮은 편
            "주택지원": 8.0,  # 주택 수리비 지원 제공이 명확함
            "농지지원": 7.5,  # 융자 지원 금액이 명시되어 있지 않아 중간 평가
            "교육지원": 7.0,  # 교육 이수 요건만 있고 실질적 지원금 언급 없음
            "농기계지원": 7.0,  # 임대사업만 지원으로 실질적 지원 한계
            "판로지원": 7.0,  # 소규모 창업 지원으로 판로 지원은 간접적
            "종합평가": 7.2   # 전반적으로 중간 수준의 지원
        },
        "상주시": {
            "정착지원": 8.0,  # 보조 400만원 + 자부담 100만원으로 영천시와 동일
            "주택지원": 9.5,  # 주택수리비와 임대료까지 지원하는 종합적 프로그램
            "농지지원": 9.5,  # 최대 3억원 융자와 농지임차료 직접 지원
            "교육지원": 8.5,  # 현장실습교육의 멘토링 시스템이 실질적 도움
            "농기계지원": 8.0,  # 임대료 50% 할인으로 실질적 비용 절감
            "판로지원": 6.5,  # "안정적 정착 지원"으로 구체성 부족
            "지원금혜택": 9.0,  # 이차보전, 농어민수당, 전입지원금 등 다양한 지원
            "종합평가": 8.5   # 다양한 영역에서 균형 잡힌 지원
        }
    }
    
    # 지원 대상 정보
    target_info = {
        "영천시": {
            "귀농정착 지원금": "영천시가 아닌 타 도시 동지역(市)에 1년이상 거주, 읍면지역으로 전입한지(단독세대가능) 5년이내인 만65세 이하, 농업을 전업으로 하면서 귀농신고가 통과된 귀농인",
            "귀농 농업창업 자금 융자": "도시 동지역(市)에 1년이상 거주, 읍면지역에 전입한지(단독세대 가능), 5년 이내인 만 65세 이하, 농업을 전업으로 하는 자",
            "주택구입 및 신축자금 융자": "도시 동지역(市)에 1년이상 거주, 읍면지역에 전입한지(단독세대 가능), 5년 이내인 만 65세 이하, 농업을 전업으로 하는 자",
            "신규농업인 현장실습 교육": "①우리시 농촌지역으로 전입한 지 5년 이내인 귀농인 ②우리시 농촌지역에 거주하며, 농업경영체를 등록한지 5년 이내인 자 ③우리시 농촌지역에 거주하는 만40세 미만 청장년",
            "귀농인 농가계 입대료 할인": "영천시에 전입한지 3년 이내인 귀농인"
        },
        "의성군": {
            "정착지원": "의성군으로 전입 후 5년 이내의 귀농인",
            "주택지원": "의성군으로 전입 후 5년 이내의 귀농인",
            "농지지원": "의성군으로 전입 후 5년 이내의 귀농인"
        },
        "상주시": {
            "정착지원": "상주시로 전입 후 5년 이내의 귀농인",
            "주택지원": "상주시로 전입 후 5년 이내의 귀농인",
            "농지지원": "상주시로 전입 후 5년 이내의 귀농인"
        }
    }
    
    # 성공 사례 수
    success_cases = {
        "영천시": 156,
        "의성군": 98,
        "상주시": 127
    }
    
    # 연간 귀농인 수 (최근 5년)
    yearly_migrants = {
        "연도": [2020, 2021, 2022, 2023, 2024],
        "영천시": [78, 92, 115, 138, 156],
        "의성군": [52, 60, 72, 85, 98],
        "상주시": [65, 75, 94, 110, 127]
    }
    
    # 작물별 소득 데이터
    crop_income = {
        "작물": ["사과", "포도", "복숭아", "배", "딸기", "참외", "고추", "마늘"],
        "영천시": [3800, 4200, 3600, 3400, 4500, 3900, 3200, 3700],
        "의성군": [3200, 3600, 3100, 3000, 3800, 3300, 3300, 4000],
        "상주시": [3500, 3900, 3400, 3200, 4100, 3600, 3000, 3500]
    }
    
    # 추가 정보
    extra_info = {
        "영천시": {
            "담당부서": "농촌지도과 (☎339-7648)",
            "연수생 교육": "연수생 교육 훈련비 지급(월 최대 80만원x5개월) ※신의를 통해 대상자 선정"
        },
        "의성군": {
            "담당부서": "농업기술센터",
            "연락처": "054-830-6116"
        },
        "상주시": {
            "담당부서": "농업기술센터",
            "연락처": "054-537-7544"
        }
    }
    
    # 지원 혜택 추가
    benefits = {
        "영천시": {
            "농가계 입대료": "농가계 입대료 50%할인",
            "귀농학교": "무료 귀농학교 운영",
            "영농체험": "단기 영농체험 프로그램"
        },
        "의성군": {
            "주택수리": "주택수리비 지원",
            "창업지원": "소규모 창업지원",
            "농기계 임대": "농기계 임대사업"
        },
        "상주시": {
            "농지은행": "농지은행 연계 지원",
            "농산물 판매": "농산물 판매장 입점 지원",
            "멘토링": "선도농가 멘토링 지원"
        }
    }
    
    return {
        "policies": policies,
        "policy_scores": policy_scores,
        "target_info": target_info,
        "success_cases": success_cases,
        "yearly_migrants": yearly_migrants,
        "crop_income": crop_income,
        "extra_info": extra_info,
        "benefits": benefits
    }

def get_data():
    return create_dummy_data()