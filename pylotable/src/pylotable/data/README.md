
```csv
nom,age
moi,42
toi,41
```

developed form

```json
[
  {
    "nom": "moi",
    "age": 42
  },
  {
    "nom": "toi",
    "age": 41
  }
]
```

header form

```json
{
  "header": ["nom", "age"],
  "data": [
      ["moi", 42],
      ["moi", 41]
    ]
}
```

implicit form

```json
[
  ["nom", "age"],
  ["moi", 42],
  ["toi", 41]
]
```

descriptive form

```json
{
  "content": [
    ["nom", "age"],
    ["moi", 42],
    ["toi", 41]
  ],
  "metadata": {
    "header": 0,
    "data": 1
  }
}

```

```json
{
  "content": [
    ["moi", 42],
    ["toi", 41]
  ],
  "metadata": {
    "header": ["nom", "age"]
  }
}

```
