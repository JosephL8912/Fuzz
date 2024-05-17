# Fuzz
## 2024 CLHS Cybersecurity
## Rubric (25/25)
- [x] Usage of GitHub (3)
- [x] Create a data mutator program (10)
- [x] Create the fuzzing program (10)
- [x] Includes README.md wtih dependencies (2)

## How it Works

* Imports a html parse and python fuzz libraries
* Using the @ sign adds the fuzz method into PythonFuzz
* Decodes Buf input and inputs into HTML Parser
* Recoes Buf and writes it to a file
* When it crahses the crash is saved to a folder which shows what crashed HTML parser

## Dependencies:
`HTML Parser`
`PythonFuzzer`

