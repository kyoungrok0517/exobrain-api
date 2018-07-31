# exobrain-api

[![Build Status](https://travis-ci.org/kyoungrok0517/exobrain-api.svg?branch=master)](https://travis-ci.org/kyoungrok0517/exobrain-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Exobrain API. Check out the project's [documentation](http://kyoungrok0517.github.io/exobrain-api/).

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Docker Compose](https://docs.docker.com/compose/)
- [httpie](https://httpie.org) (Optional)

## How to Run
```bash
cd exobrain-api
# start API server
docker-compose up -d
# download & insert data (it will take some time)
docker-compose exec web ./manage.py setup
```

## API

### KCG (Korean CG Triples)

Returns json data about triples that match the given criteria.

- **URL**

  `/api/v1/kcg`

* **Method**

  `GET`

* **URL Params**

  **Criteria:**

  `sbj=[str]`, `rel=[str]`, `obj=[str]` : plain Korean text (e.g. "자동차")

  `sbj_id=[str]`, `rel_id=[str]`, `obj_id=[str]` : Wikipedia ID (e.g. Q001144312, P279)

  **Pagination:**

  `page=[str]` : 페이지 번호. 기본값 1.

  `limit=[str]` : 페이지 당 triple 최대 개수. 기본값 10.

* **Data Params**

  None

* **Success Response**

  - **Code**: 200 <br>
    **Content**: 주어진 조건에 맞는 triple 이 `rel.confidence`가 높은 순으로 반환됨
    ```json
    {
    "count": 2202002,
    "next": "http://irel.kaist.ac.kr:8100/api/v1/kcg?limit=2&page=2",
    "previous": null,
    "results": [
            {
                "confidence": 0.06517528,
                "context": "kowiki/아이패드 (1세대) /// 발매",
                "obj": {
                    "attribute": "",
                    "id": "Q000000038",
                    "link": "kowiki/이탈리아",
                    "mention": "이탈리아",
                    "name": "이탈리아",
                    "type": [
                        "LCP_COUNTRY",
                        "PS_NAME"
                    ]
                },
                "rel": {
                    "confidence": 0.06517528,
                    "id": "P530",
                    "name": "diplomatic relation"
                },
                "sbj": {
                    "attribute": "",
                    "id": "Q000000016",
                    "link": "kowiki/캐나다",
                    "mention": "캐나다",
                    "name": "캐나다",
                    "type": [
                        "LCP_COUNTRY",
                        "PS_NAME"
                    ]
                },
                "source": {
                    "doc": {
                        "id": "Q000059802",
                        "link": "kowiki/아이패드 (1세대)",
                        "name": "아이패드 (1세대)"
                    },
                    "sect": "발매",
                    "sent": "4월 말에는 영국과 일본, 호주, 캐나다, 프랑스, 독일, 이탈리아, 스페인, 스위스 등에서 판매가 될 예정이며, 대한민국의 출시 일정은 아직 잡히지 않았다."
                },
                "uid": "1004867|02|0002|캐나다 |AND| 이탈리아"
            },
            {
                "confidence": 0.06517528,
                "context": "kowiki/아이패드 (1세대) /// 발매",
                "obj": {
                    "attribute": "",
                    "id": "Q000000038",
                    "link": "kowiki/이탈리아",
                    "mention": "이탈리아",
                    "name": "이탈리아",
                    "type": [
                        "LCP_COUNTRY",
                        "PS_NAME"
                    ]
                },
                "rel": {
                    "confidence": 0.06517528,
                    "id": "P530",
                    "name": "diplomatic relation"
                },
                "sbj": {
                    "attribute": "",
                    "id": "Q000000016",
                    "link": "kowiki/캐나다",
                    "mention": "캐나다",
                    "name": "캐나다",
                    "type": [
                        "LCP_COUNTRY",
                        "PS_NAME"
                    ]
                },
                "source": {
                    "doc": {
                        "id": "Q000059802",
                        "link": "kowiki/아이패드 (1세대)",
                        "name": "아이패드 (1세대)"
                    },
                    "sect": "발매",
                    "sent": "4월 말에는 영국과 일본, 호주, 캐나다, 프랑스, 독일, 이탈리아, 스페인, 스위스 등에서 판매가 될 예정이며, 대한민국의 출시 일정은 아직 잡히지 않았다."
                },
                "uid": "1004867|02|0002|캐나다 |AND| 이탈리아"
            }
        ]
    }
    ```

* **Error Response**

  - **Code**: 404 NOT FOUND <br>
    **Content**:
    ```json
    { "error": "Triple doesn't exist" }
    ```

* **Sample Call**
  ```sh
  curl 'http://localhost:8100/api/v1/kcg?sbj=자동차' 
  ```
