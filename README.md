# Q CLI 활용 실습 워크샵 - RNA 분석 코드 개선 실습 파일들

이 저장소는 **Q CLI 활용 실습 워크샵 - RNA 분석 코드 개선하기** 워크샵의 실습용 파일들을 포함하고 있습니다.

## 사전 요구사항
이 워크샵은 **Amazon Q Developer CLI가 설치되고 설정된 환경**에서 진행됩니다. Q CLI가 설치되어 있지 않다면 먼저 설치 및 설정을 완료해주세요.

## 워크샵 개요
제약사 R&D 조직을 위한 Q CLI 실습 워크샵으로, RNA 분석에서 자주 발생하는 세 가지 상황을 Q CLI로 해결하는 방법을 학습합니다.

## 실습 파일 설명

### 실습 1: 코드 리팩토링
- **`rna_preprocessing_old.py`** - 비효율적인 RNA-seq 전처리 코드 (개선 대상)
  - 중복된 필터링 코드
  - 비효율적인 정규화 방법
  - 하드코딩된 값들
  - 반복적인 통계 계산 코드

### 실습 2: 업데이트된 값 적용
- **`gene_annotation_analysis.py`** - 유전자 어노테이션 분석 도구 (업데이트 대상)
  - 오래된 유전자 어노테이션 정보 사용
  - pathway 정보 확장 필요
  - 분석 임계값 조정 필요

- **`updated_gene_annotations.json`** - 최신 유전자 어노테이션 데이터 (실습 2용)
  - 새로운 유전자 정보
  - 확장된 pathway 정보
  - 업데이트된 분석 임계값
  - 최신 하우스키핑 유전자 목록

### 실습 3: 히스토리 업데이트
- **`legacy_rna_pipeline.py`** - 레거시 RNA 분석 파이프라인 (현대화 대상)
  - 오래된 정규화 방법 (CPM)
  - 구식 통계 방법 (t-test)
  - 제한적인 QC 메트릭

- **`modern_rna_methods.py`** - 최신 RNA 분석 방법론 (참조용)
  - TMM/DESeq2 정규화
  - 현대적 통계 방법
  - 확장된 QC 메트릭

### 기타 파일
- **`requirements.txt`** - Python 패키지 의존성 목록

## 워크샵 학습 목표
1. **코드 리팩토링**: 비효율적인 RNA-seq 전처리 코드를 개선
2. **업데이트된 값 적용**: 최신 유전자 어노테이션 정보를 기존 코드에 반영
3. **히스토리 업데이트**: 여러 프로젝트의 오래된 분석 방법을 최신 방법으로 업데이트

## 설치 방법

1. 저장소 클론:
```bash
git clone https://github.com/awsshin/q-cli-for-rna-analysis.git
cd q-cli-for-rna-analysis
```

2. uv를 사용한 가상환경 생성 및 활성화:
```bash
# uv가 설치되어 있지 않다면 먼저 설치
curl -LsSf https://astral.sh/uv/install.sh | sh

# 가상환경 생성
uv venv

# 가상환경 활성화 (Linux/macOS)
source .venv/bin/activate

# 가상환경 활성화 (Windows)
# .venv\Scripts\activate
```

3. 의존성 패키지 설치:
```bash
# uv를 사용한 패키지 설치 (권장)
uv pip install -r requirements.txt

# 또는 일반 pip 사용
pip install -r requirements.txt
```

4. Amazon Q Developer CLI 로그인 및 환경 진입:
```bash
# Q CLI 로그인 (브라우저를 통한 인증)
q login

# Q CLI 채팅 환경 진입
q chat
```

이제 Q CLI 환경에서 실습을 시작할 수 있습니다!

## Q CLI 실습 예시

### 실습 1: 코드 리팩토링 명령어

#### 1단계: 현재 코드 분석
```bash
rna_preprocessing_old.py 파일을 분석해서 개선이 필요한 부분들을 찾아줘
```

#### 2단계: 리팩토링 제안 받기
```bash
이 RNA-seq 전처리 코드를 더 효율적이고 유지보수하기 쉽게 리팩토링해줘. 특히 중복 코드 제거, 함수 분리, 설정값 외부화에 집중해줘
```

#### 3단계: 성능 최적화 제안
```bash
pandas와 numpy를 더 효율적으로 사용해서 이 코드의 성능을 개선할 수 있는 방법을 제안해줘
```

#### 4단계: 코드 품질 검증
```bash
리팩토링된 코드에 대해 코드 리뷰를 해주고, 추가 개선사항이 있다면 제안해줘
```

### 실습 2: 업데이트된 값 적용 명령어

#### 1단계: 현재 어노테이션 정보 확인
```bash
gene_annotation_analysis.py 파일에서 사용하고 있는 유전자 어노테이션 정보를 분석해줘
```

#### 2단계: 업데이트 정보 적용
```bash
updated_gene_annotations.json 파일의 최신 정보를 gene_annotation_analysis.py 코드에 적용해줘. 기존 기능은 유지하면서 새로운 정보를 추가해줘
```

#### 3단계: 새로운 pathway 분석 기능 추가
```bash
업데이트된 pathway 정보를 활용해서 RAS_SIGNALING과 PI3K_AKT pathway 분석 기능을 추가해줘
```

#### 4단계: 임계값 업데이트 검증
```bash
새로운 임계값들이 분석 결과에 어떤 영향을 미치는지 비교 분석 코드를 작성해줘
```

### 실습 3: 히스토리 업데이트 명령어

#### 1단계: 레거시 코드 분석
```bash
legacy_rna_pipeline.py 파일을 분석해서 현재 사용하고 있는 방법들이 얼마나 오래된 것인지, 어떤 부분을 업데이트해야 하는지 알려줘
```

#### 2단계: 현대적 방법론 적용
```bash
modern_rna_methods.py 파일의 최신 방법론을 참고해서 legacy_rna_pipeline.py를 현대적인 방법으로 업데이트해줘
```

#### 3단계: 성능 및 정확도 개선
```bash
업데이트된 파이프라인에서 성능을 개선하고 분석 정확도를 높일 수 있는 방법들을 적용해줘
```

#### 4단계: 호환성 및 마이그레이션 가이드
```bash
기존 레거시 파이프라인 사용자들이 새로운 파이프라인으로 쉽게 마이그레이션할 수 있도록 가이드와 변환 도구를 만들어줘
```

### 추가 실습 시나리오

#### 시나리오 A: 에러 디버깅
```bash
이 RNA 분석 코드에서 발생하는 에러를 찾아서 수정해줘
```

#### 시나리오 B: 문서화 개선
```bash
이 코드에 대한 상세한 문서화와 사용 예시를 작성해줘
```

#### 시나리오 C: 테스트 코드 작성
```bash
이 RNA 분석 함수들에 대한 단위 테스트를 작성해줘
```

#### 시나리오 D: 설정 파일 외부화
```bash
하드코딩된 설정값들을 YAML 설정 파일로 분리해줘
```

## 개발 환경
- Python 3.x
- Amazon Q Developer CLI
- 생물정보학 분석 라이브러리들 (requirements.txt 참조)

## 워크샵 후 활용 방안
- 일상 업무에서의 코드 리뷰 및 리팩토링
- 신기술 학습 및 적용
- 팀 차원의 코딩 표준 수립
- 지식 공유 및 교육 자료 작성

이 실습 파일들을 통해 Q CLI를 RNA 분석 업무에 효과적으로 활용하는 방법을 익혀보세요!
