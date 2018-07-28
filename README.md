# exobrain-api

[![Build Status](https://travis-ci.org/kyoungrok0517/exobrain-api.svg?branch=master)](https://travis-ci.org/kyoungrok0517/exobrain-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Exobrain API. Check out the project's [documentation](http://kyoungrok0517.github.io/exobrain-api/).

# API

## Show Triple

Returns json data about triples that match the given criteria.

- **URL**

  `/triples`

* **Method**

  `GET`

* **URL Params**

  `subj`, `rel`, `obj` : plain Korean text (e.g. "자동차")

  `sub_id`, `rel_id`, `obj_id` : Wikipedia ID (e.g. Q001144312, P279)

  **Optional:**

  `subj=[str]`

  `subj_id=[str]`

  `rel=[str]`

  `rel_id=[str]`

  `obj=[str]`

  `obj_id=[str]`

* **Data Params**

  None

* **Success Response**

  - **Code**: 200 <br>
    **Content**:
    ```
    {}
    ```

* **Error Response**

  - **Code**: 404 NOT FOUND <br>
    **Content**:
    ```
    {error : "Triple doesn't exist"}
    ```

* **Sample Call**
  ```
  {}
  ```

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)

# Local Development

Start the dev server for local development:

```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
