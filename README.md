# Calculator API

This is a simple calculator API built with Sanic.

![License](https://img.shields.io/badge/license-MIT-green) ![Data da última versão](https://img.shields.io/badge/release%20date-march-blue)

## Table of Contents

-   [Resume](#pushpin-resume)
-   [Technology](#zap-technology)
-   [Installation](#wrench-installation)
-   [Endpoints](#round_pushpin-endpoints)
    1.   [Addition](#addition)
    1.   [Subtraction](#subtraction)
    1.   [Multiplication](#multiplication)
    1.   [Square root](#square-root)
    1.   [Arithmetic mean](#arithmetic-mean)
    1.   [Harmonic mean](#harmonic-mean)
    1.   [Moda](#moda)
-   [Usage](#hammer_and_wrench-usage)
-   [Authors](#gem-authors)
-   [License](#scroll-license)

## :pushpin: Resume

>   This is a simple calculator API built using the Sanic framework in Python. It provides endpoints for performing basic arithmetic operations, calculating square roots and powers, calculating mean, harmonic mean and moda.

## :zap: Technology

Technology used within the project:

-   [Sanic](https://sanic.dev): Version 22.12.0

## :wrench: Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/joao-coimbra/calculator-api.git
    ```

2. Install the dependencies:

    ```bash
    cd calculator-api
    pip install -r requirements.txt
    ```

3. Start the API server:

    ```bash
    python server.py
    ```

    sanic CLI

    ```bash
    sanic server.app
    ```

    The server will start running at `http://localhost:8000.`

## :round_pushpin: Endpoints

### Addition

Takes list of numbers and returns the sum.

```http
POST /api/add
```

| Parameter | Type    | Description                  |
| :-------- | :------ | :--------------------------- |
| `nums`    | `array` | **Required**. list of numbers |

Request Body:

```json
{
  "nums": [2, 3, 7]
}
```

Response Body:

```json
{
  "result": 12
}
```

---

### Subtraction

Takes list of numbers and returns the subtract.

```http
POST /api/subtract
```

| Parameter | Type    | Description                  |
| :-------- | :------ | :--------------------------- |
| `nums`    | `array` | **Required**. list of numbers |

Request Body:

```json
{
  "nums": [10, 7]
}
```

Response Body:

```json
{
  "result": 3
}
```

---

### Multiplication

Takes list of numbers and returns the multiply.

```http
POST /api/multiply
```

| Parameter | Type    | Description                  |
| :-------- | :------ | :--------------------------- |
| `nums`    | `array` | **Required**. list of numbers |

Request Body:

```json
{
  "nums": [10, 7, 3]
}
```

Response Body:

```json
{
  "result": 210
}
```

---

### Division

Divides one number by another.

```http
POST /api/divide
```

| Parameter | Type    | Description                       |
| :-------- | :------ | :-------------------------------- |
| `num`     | `float` | **Required**. number to be divided |
| `divisor` | `int`   | **Required**. divisor number       |

Request Body:

```json
{
  "num": 7,
  "divisor": 2
}
```

Response Body:

```json
{
  "result": 3.5
}
```
---
### Square Root
Calculates the square root of a number.

```http
POST /api/sqrt
```

| Parameter | Type  | Description                            |
| :-------- | :---- | :------------------------------------- |
| `num`     | `int` | **Required**. number to get square root |

Request Body:

```json
{
  "num": 9
}
```

Response Body:

```json
{
  "result": 3
}
```

---

### Power

Raises one number to the power of another.

```http
POST /api/power
```

| Parameter  | Type    | Description                       |
| :--------- | :------ | :-------------------------------- |
| `base`     | `float` | **Required**. number to get its power  |
| `exponent` | `int`   | **Required**. calculation exponent |

Request Body:

```json
{
  "base": 5,
  "exponent": 3
}
```

Response Body:

```json
{
  "result": 125
}
```

---

### Arithmetic Mean

Calculates the arithmetic mean of a list of numbers.

```http
POST /api/hmean
```

| Parameter | Type    | Description                  |
| :-------- | :------ | :--------------------------- |
| `nums`    | `array` | **Required**. list of numbers |

Request Body:

```json
{
  "nums": [5, 3, 7, 2]
}
```

Response Body:

```json
{
  "result": 4.25
}
```

---

### Harmonic Mean

Calculates the harmonic mean of a list of numbers.

```http
POST /api/mean
```

| Parameter | Type    | Description                  |
| :-------- | :------ | :--------------------------- |
| `nums`    | `array` | **Required**. list of numbers |

Request Body:

```json
{
  "nums": [5, 3, 7, 2]
}
```

Response Body:

```json
{
  "result": 3.2098765432098764
}
```

---

### Moda

Calculates the mode (most frequent values) of a list of numbers.

```http
POST /api/moda
```

| Parameter | Type    | Description                  |
| :-------- | :------ | :--------------------------- |
| `nums`    | `array` | **Required**. list of numbers |

Request Body:

```json
{
  "nums": [5, 3, 7, 2, 5, 2]
}
```

Response Body:

```json
{
  "result": [5, 2]
}
```

## :hammer_and_wrench: Usage

To use this API, you can send HTTP requests to the appropriate endpoints. For example, to add two numbers together, you can send a ***POST*** request to the _/api/add_ endpoint with a JSON body like this:

```json
{
  "nums": [5, 3, 7]
}
```

And the API will respond with a JSON body like this:

```json
{
  "result": 15
}
```

## :gem: Authors

[![name](https://avatars.githubusercontent.com/u/61300191?s=80&v=4)](https://github.com/joao-coimbra)
[![name](https://avatars.githubusercontent.com/u/64169738?s=80&v=4)](https://github.com/alvarezfelipe)

## :scroll: License

This project is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license.
