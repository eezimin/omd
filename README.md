## Task 1
python -m doctest -o NORMALIZE_WHITESPACE -v task_1_doctest_morse.py
![image](https://user-images.githubusercontent.com/77446049/194842367-358c2e92-0354-44d7-8c91-30a36c5445d3.png)


## Task 2
python -m pytest -v task_2_parametrize_morse.py
![image](https://user-images.githubusercontent.com/77446049/194842380-c1562e7d-ae0b-4bf2-bcad-516b3c875aa9.png)

## Task 3
python -m unittest task_3_unittest_onehot.py
![image](https://user-images.githubusercontent.com/77446049/194842391-b50c0fc8-1119-4b1b-8bdf-f04d2d2cfb49.png)

## Task 4
python -m pytest task_4_pytest_onehot.py|cat
![image](https://user-images.githubusercontent.com/77446049/194842403-ceaa913c-8d1d-4cf0-a773-61c3bfb1fb93.png)

## Task 5
python -m pytest -v -s task_5_mock_yearnow.py --cov=what_is_year_now

python -m pytest --cov . --cov-report html
![image](https://user-images.githubusercontent.com/77446049/194842420-9aad781c-0690-433d-9d99-5f2097bde402.png)
