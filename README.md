# able-reference-data

ABLE Labs 공통 참조 데이터 저장소. Labware / Module / Liquid 스펙을 버전 관리합니다.

## 구조

```
able-reference-data/
├── labware/
│   ├── schema.json      # 필드 정의 + 유효성 규칙
│   └── records.json     # 실제 데이터
├── modules/
│   ├── schema.json
│   └── records.json
├── liquid/
│   ├── schema.json
│   └── records.json
├── scripts/
│   └── validate.py      # 유효성 검사
└── CHANGELOG.md
```

## 데이터 추가/수정 방법

1. `records.json` 편집
2. 유효성 검사: `python scripts/validate.py`
3. PR 생성 → 리뷰 → merge → 버전 태그

```bash
git tag v1.1.0
git push origin v1.1.0
```

## 긴급 상황 (데모/고객사)

현장에서 즉시 필요한 Labware는 각 제품의 **Local Labware** 기능을 사용합니다.  
나중에 공식화가 필요하면 이 저장소에 PR을 올려주세요.

## 제품별 연동 버전

| 제품 | 버전 | 비고 |
|------|------|------|
| notable-96ch | v1.0.0 | |
| suitable | - | 미연동 |

## 유효성 검사 자동화 (pre-commit)

```bash
pip install pre-commit jsonschema
pre-commit install
```

이후 commit 시 자동으로 `validate.py`가 실행됩니다.
