## Task 1
python -m doctest -o NORMALIZE_WHITESPACE -v task_1_doctest_morse.py

## Task 2
python -m pytest -v task_2_parametrize_morse.py

## Task 3
python -m unittest task_3_unittest_onehot.py

## Task 4
python -m pytest task_4_pytest_onehot.py|cat

## Task 5
python -m pytest -v -s task_5_mock_yearnow.py --cov=what_is_year_now

python -m pytest --cov . --cov-report html
