# exobrain-api

[![Build Status](https://travis-ci.org/kyoungrok0517/exobrain-api.svg?branch=master)](https://travis-ci.org/kyoungrok0517/exobrain-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Exobrain API. Check out the project's [documentation](http://kyoungrok0517.github.io/exobrain-api/).

# How to Run
```bash
cd exobrain-api
# start API server
docker-compose up -d
# download & insert data (it will take some time)
docker-compose exec web ./manage.py setup
```

# API

## Show Triple

Returns json data about triples that match the given criteria.

- **URL**

  `/kcg/api/v1`

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
    "count": 12,
    "next": null,
    "previous": null,
      "triples": [{
        "id": "0002717|00|0001|승용차 |AND| 역사",
        "sbj": {
          "id": "Q001144312",
          "link": "kowiki/승용차",
          "name": "승용차",
          "type": ["AF_TRANSPORT"],
          "mention": "승용차",
          "attribute": ""
        },
        "rel": {
          "id": "P279",
          "name": "subclass of",
          "confidence": 0.012006174
        },
        "obj": {
          "id": "Q000000309",
          "link": "kowiki/역사",
          "name": "역사",
          "type": ["FD_ART", "CV_POSITION"],
          "mention": "역사",
          "attribute": ""
        },
        "source": {
          "sent": "현재 현대자동차의 승용차 중에서 가장 긴 역사를 가지고 있다.",
          "sect": "__TOP_SECTION__",
          "doc": {
            "id": "Q000482458",
            "link": "kowiki/현대 쏘나타",
            "name": "현대 쏘나타"
          }
        },
        "context": "kowiki/현대 쏘나타 /// __TOP_SECTION__"
      }, ...]
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
  curl 'http://localhost:8100/api/v1/kcg' 
  ```

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Docker Compose](https://docs.docker.com/compose/)

# Local Development

Start the dev server for local development:

```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
