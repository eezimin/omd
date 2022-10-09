# Task 1
python -m doctest -o NORMALIZE_WHITESPACE -v task_1_doctest_morse.py > result1.txt

# Task 2
python -m pytest -v task_2_parametrize_morse.py > result2.txt

# Task 3
python -m unittest task_3_unittest_onehot.py >> result3.txt

# Task 4
python -m pytest task_4_pytest_onehot.py|cat > result4.txt

# Task 5
python -m pytest -v -s task_5_mock_yearnow.py --cov=what_is_year_now > result5.txt
python -m pytest --cov . --cov-report html
